#!/usr/bin/env python3

import easygraph as eg
from easygraph import *  # type: ignore


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

print(f"""Profiling dataset \033[34m{filename}\033[0m""")




# ===========================
print(f"""Profiling \033[92mloading\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# 'read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.DiGraph()).cpp()' contains quotes
avg_times |= {'loading': benchmark_autorange('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.DiGraph()).cpp()', globals=globals(), n=n) }


# loading* only
g = eval('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.DiGraph()).cpp()')




# networkx & easygraph only, after loading*
from utils import get_first_node
nodeid = 'first_node'
first_node = get_first_node(g)




# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# f'Dijkstra(g, {nodeid})' contains quotes
avg_times |= {'shortest path': benchmark_autorange(f'Dijkstra(g, {nodeid})', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mstrongly connected components\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# '[i for i in strongly_connected_components(g)]' contains quotes
avg_times |= {'strongly connected components': benchmark_autorange('[i for i in strongly_connected_components(g)]', globals=globals(), n=n) }







profile_script_insert_results(__file__, filename, avg_times, args.iteration)