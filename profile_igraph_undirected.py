#!/usr/bin/env python3

from igraph import *  # type: ignore


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results

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

avg_times: dict[str, float] = {}

print(f"Profiling dataset {filename}")


# ===========================
print("Profiling loading_undirected")
print("=================")
print()

#  contains quotes
avg_times |= {'loading_undirected': benchmark_autorange("Graph.Read(filename, format='edges', directed=False)", globals=globals(), n=n) }


# loading* only
g = eval("Graph.Read(filename, format='edges', directed=False)")






# ===========================
print("Profiling shortest path")
print("=================")
print()

#  contains quotes
avg_times |= {'shortest path': benchmark_autorange("g.shortest_paths([g.vs[0]])", globals=globals(), n=n) }





# ===========================
print("Profiling k-core")
print("=================")
print()

#  contains quotes
avg_times |= {'k-core': benchmark_autorange("g.coreness(mode='all')", globals=globals(), n=n) }






profile_script_insert_results(__file__, filename, avg_times, args.iteration)