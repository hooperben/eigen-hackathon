// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@eigenlayer/contracts/interfaces/IServiceManager.sol";
import "@eigenlayer/contracts/interfaces/IDelegationManager.sol";
import "@eigenlayer/contracts/interfaces/IStrategyManager.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ZarathustraEigenLayerServiceManager is IServiceManager, Ownable, Pausable, ReentrancyGuard {

    IDelegationManager public delegationManager;
    IStrategyManager public strategyManager;

    mapping(address => bool) public registeredOperators;
    address[] public operatorList;

    string public avsMetadataURI;
    uint256 public constant QUORUM_THRESHOLD = 2;
    // Minimum stake, can be changed
    uint256 public constant MIN_STAKE = 1 ether;

    IServiceManager.MiddlewareTimes[] public middlewareTimesList;

    event OperatorRegistered(address operator);
    event OperatorDeregistered(address operator);
    event AVSMetadataURIUpdated(string newMetadataURI);

    constructor(IDelegationManager _delegationManager, IStrategyManager _strategyManager) {
        delegationManager = _delegationManager;
        strategyManager = _strategyManager;
    }

    function initialize(
        IDelegationManager _delegationManager,
        IStrategyManager _strategyManager
    ) external onlyOwner {
        delegationManager = _delegationManager;
        strategyManager = _strategyManager;
    }

    function middlewareTimesLength() external view returns (uint32) {
        return uint32(middlewareTimesList.length);
    }

    function middlewareTimes(uint256 index) external view returns (IServiceManager.MiddlewareTimes memory) {
        require(index < middlewareTimesList.length, "Index out of bounds");
        return middlewareTimesList[index];
    }

    function isActiveOperator(address operator) public view returns (bool isActive) {
        return registeredOperators[operator] && 
               delegationManager.isOperator(operator) && 
               strategyManager.stakedInStrategy(operator, address(this)) >= MIN_STAKE;
    }

    function getActiveOperators() external view returns (address[] memory) {
        uint256 activeCount = 0;
        for (uint256 i = 0; i < operatorList.length; i++) {
            if (isActiveOperator(operatorList[i])) {
                activeCount++;
            }
        }

        address[] memory activeOperators = new address[](activeCount);
        uint256 index = 0;
        for (uint256 i = 0; i < operatorList.length; i++) {
            if (isActiveOperator(operatorList[i])) {
                activeOperators[index] = operatorList[i];
                index++;
            }
        }

        return activeOperators;
    }

    function registerOperator(address operator, string calldata operatorMetadataURI) external nonReentrant {
        require(!registeredOperators[operator], "Operator already registered");
        require(delegationManager.isOperator(operator), "Not an EigenLayer operator");
        
        registeredOperators[operator] = true;
        operatorList.push(operator);

        emit OperatorRegistered(operator);
    }

    function deregisterOperator(address operator) external nonReentrant {
        require(registeredOperators[operator], "Operator not registered");
        
        registeredOperators[operator] = false;
        for (uint256 i = 0; i < operatorList.length; i++) {
            if (operatorList[i] == operator) {
                operatorList[i] = operatorList[operatorList.length - 1];
                operatorList.pop();
                break;
            }
        }

        emit OperatorDeregistered(operator);
    }

    function updateAVSMetadataURI(string calldata _newMetadataURI) external onlyOwner {
        avsMetadataURI = _newMetadataURI;
        emit AVSMetadataURIUpdated(_newMetadataURI);
    }

    // Additional helper functions

    function addMiddlewareTimes(IServiceManager.MiddlewareTimes memory newTimes) external onlyOwner {
        middlewareTimesList.push(newTimes);
    }

    function removeMiddlewareTimes(uint256 index) external onlyOwner {
        require(index < middlewareTimesList.length, "Index out of bounds");
        middlewareTimesList[index] = middlewareTimesList[middlewareTimesList.length - 1];
        middlewareTimesList.pop();
    }
}