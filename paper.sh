#!/usr/bin/env bash

# use move to backup bench-results.db if exists with a timestamp suffix
if [ -f bench-results.db ]; then
    echo 'Backing up bench-results.db'
    mv -fv bench-results.db "bench-results.db.$(date +%s)"
fi

# create a new db
./create_bench_results_db.py
echo 'Created new bench-results.db'

echo 'Running benchmarks...'
echo 'Benchmarking multiprocessing...'
./mentrypoint_paper.sh
echo 'Benchmarking C++ binding...'
./entrypoint_paper.sh
