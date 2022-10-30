#!/usr/bin/env bash

./mbench_er_500.py --paper "$@"
./mbench_er_1000.py --paper "$@"
./mbench_er_5000.py --paper "$@"
./mbench_er_10000.py --paper "$@"
./mbench_bio.py --paper "$@"
./mbench_uspowergrid.py --paper "$@"
./mbench_enron.py --paper "$@"
./mbench_coauth.py --paper "$@"