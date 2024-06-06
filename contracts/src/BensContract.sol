// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract BensContract {
    event BensEvent(uint256 indexed number);

    function setNumber(uint256 newNumber) public {
        emit BensEvent(newNumber);
    }
}
