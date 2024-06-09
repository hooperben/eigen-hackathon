# Makefile for running forge tests

CONTRACTS_DIR=contracts
LIB_PATHS=node_modules

.PHONY: test
test:
	forge test --contracts $(CONTRACTS_DIR) --lib-paths $(LIB_PATHS) --via-ir

.PHONY: deploy
deploy:
	forge script script/Deploy.s.sol:Deploy --rpc-url localhost:8545 --broadcast -vvvv

.PHONY: event
event:
	forge script script/EmitEvent.s.sol:EmitEvent --rpc-url localhost:8545 --broadcast -vvvv