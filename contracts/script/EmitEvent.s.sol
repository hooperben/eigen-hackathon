// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console} from "forge-std/src/Script.sol";

import "../src/IBensContract.sol";

// to run:
// forge script script/EmitEvent.s.sol:EmitEvent --rpc-url localhost:8545 --broadcast --verify -vvvv

contract EmitEvent is Script {
    function setUp() public {}

    function run() public {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");

        vm.startBroadcast(deployerPrivateKey);

        IBensContract bensContract = IBensContract(
            0x5FbDB2315678afecb367f032d93F642f64180aa3
        );
        bensContract.setNumber(69);

        vm.stopBroadcast();
    }
}
