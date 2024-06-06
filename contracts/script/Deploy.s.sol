// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Script, console} from "forge-std/src/Script.sol";

import "../src/BensContract.sol";

// to run:
// forge script script/Deploy.s.sol:Deploy --rpc-url localhost:8545 --broadcast -vvvv

contract Deploy is Script {
    function setUp() public {}

    function run() public {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");

        vm.startBroadcast(deployerPrivateKey);

        BensContract bensContract = new BensContract();

        vm.stopBroadcast();
    }
}
