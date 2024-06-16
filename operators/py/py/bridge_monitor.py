import asyncio
import aiostream
from pathlib import Path
from typing import NoReturn, AsyncGenerator
from eth_typing import ChecksumAddress
import eth_abi

import websockets
from eth_utils import to_checksum_address

from py.config.config import Chain
from py.event_types import Attestation, BridgeRequest


def get_log_sub_msg(address: str, topics: list | None = None) -> str:
    topics = topics or []
    if topics:
        return f'{{"jsonrpc":"2.0","id":1,"method":"eth_subscribe","params":["logs",{{"address":"{address}","topics":{topics}}}]}}'
    else:
        return f'{{"jsonrpc":"2.0","id":1,"method":"eth_subscribe","params":["logs",{{"address":"{address}"}}]}}'


def decode_bridge_event(data: str):
    v = eth_abi.decode(
        ['uint256', 'uint256', 'address', 'address', 'uint256', 'bytes'],
        bytes.fromhex(data[2:])
    )
    return v


def decode_address(data: str) -> ChecksumAddress:
    return to_checksum_address(eth_abi.decode(
        ['address'],
        bytes.fromhex(data[2:])
    )[0])


class BridgeMonitor:
    def __init__(self, chain: Chain):
        self.chain = chain

    async def _monitor(self) -> AsyncGenerator[str, None]:
        async with websockets.connect(self.chain.wss_endpoint) as ws:
            await ws.send(get_log_sub_msg(self.chain.vault_address))
            await ws.recv()
            print(f"Subscribed to {self.chain.vault_address} on {self.chain.name}")
            while True:
                yield await ws.recv()

    async def monitor(self) -> AsyncGenerator[BridgeRequest | Attestation, None]:
        while True:
            try:
                async for message in self._monitor():
                    yield message
            except Exception as e:
                print(e)
                await asyncio.sleep(5)


class CompositeBridgeMonitor:
    def __init__(self, *chain: Chain):
        self.monitors = [BridgeMonitor(c) for c in chain]

    async def monitor(self) -> AsyncGenerator[str, None]:
        merged_stream = aiostream.stream.merge(*(m.monitor() for m in self.monitors))
        async with merged_stream.stream() as stream:
            async for msg in stream:
                yield msg

    async def consume(self):
        async for msg in self.monitor():
            print(msg)
            print(decode_bridge_event(msg))


if __name__ == "__main__":
    from py.config.config import load_config
    config = load_config(Path(__file__).parent / "config" / "config.json")
    monitor = CompositeBridgeMonitor(*config.chains)
    asyncio.run(monitor.consume())
