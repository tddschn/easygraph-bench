#!/usr/bin/env bash

# mkdir -p bench && cd bench || return
# cp ../entrypoint_*.py . -v

./create_bench_results_db.py --force

# ./entrypoint_normal.py -D
# ./entrypoint_large.py -D
# ./entrypoint_coauthorship.py -D

./entrypoint_all.py -D

./process-and-release-results.sh
