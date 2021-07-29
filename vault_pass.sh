#!/bin/bash
set -e

if [ -f "/etc/ansible/.vault_pass.txt" ]; then
    cat "/etc/ansible/.vault_pass.txt"
elif [ -f "./.vault_pass.txt" ]; then
    cat "./.vault_pass.txt"
else
    exit 1
fi
