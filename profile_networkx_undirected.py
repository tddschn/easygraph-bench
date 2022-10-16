#!/usr/bin/env python3

import networkx as nx
from networkx import *  # type: ignore


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
avg_times |= {'loading_undirected': benchmark_autorange('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.Graph())', globals=globals(), n=n) }


# loading* only
g = eval('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.Graph())')




# networkx & easygraph only, after loading*
from utils import get_first_node
nodeid = 'first_node'
first_node = get_first_node(g)



# ===========================
print("Profiling 2-hops")
print("=================")
print()

#  contains quotes
avg_times |= {'2-hops': benchmark_autorange(f'single_source_shortest_path_length(g, {nodeid}, cutoff=2)', globals=globals(), n=n) }





# ===========================
print("Profiling shortest path")
print("=================")
print()

#  contains quotes
avg_times |= {'shortest path': benchmark_autorange(f'shortest_path_length(g, {nodeid})', globals=globals(), n=n) }





# ===========================
print("Profiling k-core")
print("=================")
print()

#  contains quotes
avg_times |= {'k-core': benchmark_autorange('core.core_number(g)', globals=globals(), n=n) }






profile_script_insert_results(__file__, filename, avg_times, args.iteration)