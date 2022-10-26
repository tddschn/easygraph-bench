#!/usr/bin/env bash

./bench_er_200_directed.py "$@"
./bench_er_200.py "$@"
./bench_er_500_directed.py "$@"
./bench_er_500.py "$@"
./bench_er_1000.py "$@"
./bench_er_1000_directed.py "$@"
./bench_er_2000.py "$@"
./bench_er_2000_directed.py "$@"
./bench_er_5000_directed.py "$@"
./bench_er_5000.py "$@"