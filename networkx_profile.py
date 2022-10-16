#!/usr/bin/env python3

import networkx as nx
from networkx import *  # type: ignore

from utils_db import profile_script_insert_results

from utils import get_first_node

avg_times: list[float] = []

from benchmark import benchmark_autorange


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

# if "pokec" in filename:
#     nodeid = '1'
# else:
#     nodeid = '0'
nodeid = 'first_node'


print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

avg_times.append(
    benchmark_autorange(
        'read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.DiGraph())',
        globals=globals(),
        n=n,
    )
)
g = read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.DiGraph())
first_node = get_first_node(g)

print("Profiling 2-hops")
print("================")
print()

avg_times.append(
    benchmark_autorange(
        f'single_source_shortest_path_length(g, {nodeid}, cutoff=2)',
        globals=globals(),
        n=n,
    )
)

print("Profiling shortest path")
print("=======================")
print()

avg_times.append(
    benchmark_autorange(f'shortest_path_length(g, {nodeid})', globals=globals(), n=n)
)

print("Profiling PageRank")
print("==================")
print()

avg_times.append(
    benchmark_autorange(
        'pagerank(g, alpha=0.85, tol=1e-3, max_iter=10000000)', globals=globals(), n=n
    )
)

print("Profiling k-core")
print("================")
print()

avg_times.append(benchmark_autorange('core.core_number(g)', globals=globals(), n=n))

print("Profiling strongly connected components")
print("=======================================")
print()

avg_times.append(
    benchmark_autorange(
        '[i for i in strongly_connected_components(g)]', globals=globals(), n=n
    )
)

profile_script_insert_results(__file__, filename, avg_times, args.iteration)
