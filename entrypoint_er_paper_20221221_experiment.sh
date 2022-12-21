#!/usr/bin/env bash

./mbench_er_paper_20221221_100000_50000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_100000_100000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_100000_200000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_100000_500000.py --paper --paper-fast "$@"

./mbench_er_paper_20221221_1000000_50000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_1000000_100000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_1000000_200000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_1000000_500000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_1000000_1000000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_1000000_2000000.py --paper --paper-fast "$@"
./mbench_er_paper_20221221_1000000_5000000.py --paper --paper-fast "$@"
