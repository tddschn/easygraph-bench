#!/usr/bin/env bash

./bench_er_paper_20221213_50000.py --paper "$@"
./bench_er_paper_20221213_500000.py --paper "$@"
./bench_er_paper_20221213_1000000.py --paper "$@"
./mbench_er_paper_20221213_50000.py --paper "$@"
./mbench_er_paper_20221213_500000.py --paper "$@"
./mbench_er_paper_20221213_1000000.py --paper "$@"
