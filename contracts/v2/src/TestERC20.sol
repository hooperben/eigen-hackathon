// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TestERC20 is ERC20 {
    constructor() ERC20("Test", "TEST") {
        _mint(msg.sender, 10000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) external {
        _mint(to, amount);
    }
}
