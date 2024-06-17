#!/bin/bash

ABI_DIR="../abis"
OUTPUT_DIR="./wrappers"

# Find all directories containing ABI files
for dir in $(find $ABI_DIR -type d); do
  # Check if the directory contains any .abi.json files
  if compgen -G "$dir/*json" > /dev/null; then
    echo "Processing directory: $dir"
    abi-gen --abis "$dir/*.json" --output "$OUTPUT_DIR" --language Python
  fi
done
