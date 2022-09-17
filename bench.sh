#!/usr/bin/env bash

# mkdir -p bench && cd bench || return
# cp ../entrypoint_*.py . -v

./entrypoint_normal.py -D
./entrypoint_large.py -D
./entrypoint_coauthorship.py -D

./process-and-release-results.sh
