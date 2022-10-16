#!/usr/bin/env python3
# ! this script is not used because snap does not support python 3.10.
import sys


print('this script is not used because snap does not support python 3.10.')
sys.exit(0)

import snap  # type: ignore
from benchmark import benchmark, benchmark_autorange
from pathlib import Path
from utils_db import profile_script_insert_results
from config import bench_results_db_path, methods_timlrx, methods6_timlrx
from datetime import datetime
import sqlite3

avg_times: list[float] = []

from benchmark import benchmark


import argparse


def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser(
        description='benchmark', formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('dataset', help='dataset file', metavar='PATH', type=str)
    parser.add_argument(
        '-n',
        '--iteration',
        help='iteration count when benchmarking',
        metavar='INT',
        type=int,
    )
    return parser.parse_args()


args = get_args()
filename = args.dataset
n = args.iteration

# filename = sys.argv[1]
# n = int(sys.argv[2])

print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

avg_times.append(
    benchmark_autorange(
        "snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)", globals=globals(), n=n
    )
)
g = snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)

print("Profiling 2-hops")
print("================")
print()

NodeVec = snap.TIntV()
avg_times.append(
    benchmark_autorange(
        "snap.GetNodesAtHop(g, 0, 2, NodeVec, True)", globals=globals(), n=n
    )
)

print("Profiling shortest path")
print("=======================")
print()

NIdToDistH = snap.TIntH()
avg_times.append(
    benchmark_autorange(
        "snap.GetShortPath(g, 0, NIdToDistH, True)", globals=globals(), n=n
    )
)

print("Profiling PageRank")
print("==================")
print()

PRankH = snap.TIntFltH()
avg_times.append(
    benchmark_autorange(
        "snap.GetPageRank(g, PRankH, 0.85, 1e-3, 10000000)", globals=globals(), n=n
    )
)

print("Profiling k-core")
print("================")
print()

CoreIDSzV = snap.TIntPrV()
avg_times.append(
    benchmark_autorange("snap.GetKCoreNodes(g, CoreIDSzV)", globals=globals(), n=n)
)

print("Profiling strongly connected components")
print("=======================================")
print()

Components = snap.TCnComV()
avg_times.append(
    benchmark_autorange("snap.GetSccs(g, Components)", globals=globals(), n=n)
)
