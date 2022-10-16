#!/usr/bin/env python3

from igraph import *  # type: ignore
from utils_db import profile_script_insert_results

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

print(f"Profiling dataset {filename}")

print("Profiling loading")
print("=================")
print()

avg_times.append(
    benchmark_autorange("Graph.Read(filename, format='edges')", globals=globals(), n=n)
)
g = Graph.Read(filename, format='edges')

print("Profiling shortest path")
print("=======================")
print()

avg_times.append(
    benchmark_autorange("g.shortest_paths([g.vs[0]])", globals=globals(), n=n)
)

print("Profiling PageRank")
print("==================")
print()

avg_times.append(
    benchmark_autorange("g.pagerank(damping=0.85)", globals=globals(), n=n)
)

print("Profiling k-core")
print("================")
print()

avg_times.append(benchmark_autorange("g.coreness(mode='all')", globals=globals(), n=n))

print("Profiling strongly connected components")
print("=======================================")
print()

avg_times.append(
    benchmark_autorange(
        "[i for i in g.components(mode=STRONG)]", globals=globals(), n=n
    )
)

profile_script_insert_results(__file__, filename, avg_times, args.iteration)
