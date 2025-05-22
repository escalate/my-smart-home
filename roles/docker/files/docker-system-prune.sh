#!/bin/bash
set -e -E -u -C -o pipefail

exec 1> >(logger --tag "$(basename "$0")") 2>&1

if [[ "$EUID" -ne 0 ]] ; then echo "Please run as root" ; exit 1 ; fi

echo "Start removing of unused data from Docker"

docker system prune \
    --all \
    --volumes \
    --force

echo "Finish removing of unused data from Docker"
