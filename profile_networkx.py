#!/usr/bin/env python3

import networkx as nx
import networkx
from networkx import *  # type: ignore


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results
from utils_other import remove_system_resource_limits
import sqlite3
import sys

import argparse

def insert_results():
    try:
        profile_script_insert_results(__file__, filename, avg_times, args.iteration)
    except sqlite3.OperationalError as e:
        print(f"Failed to insert results into database: \n{e}")
        print(f'Please run `./create_bench_results_db.py` to resolve this issue.')

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser(
        description='Benchmark networkx', formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('dataset', help='path to the dataset file in tab-separated edgelist format', metavar='PATH', type=str)
    parser.add_argument(
        '-n',
        '--iteration',
        help='iteration count when benchmarking, auto-determined if unspecified',
        metavar='INT',
        type=int,
    )
    parser.add_argument(
        '--print-graph-info',
        help='get the # of nodes and edges and print',
        action='store_true',
    )
    parser.add_argument(
        '--print-graph-info-only'
        help='get the # of nodes and edges and print, then exit',
        action='store_true',
    )
    return parser.parse_args()


args = get_args()
if args.print_graph_info_only:
    args.print_graph_info = True

remove_system_resource_limits()

filename = args.dataset
n = args.iteration

# filename = sys.argv[1]
# n = int(sys.argv[2])

avg_times: dict[str, float] = {}

print('''\033[91m=================================\033[0m''')
print(f"""Profiling \033[96mnetworkx\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.DiGraph())' contains quotes
avg_times |= {'loading': benchmark_autorange('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.DiGraph())', globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.DiGraph())')

if args.print_graph_info:
    
    print('networkx does not support printing graph info.')
    

    if args.print_graph_info_only:
        sys.exit(0)






# networkx & easygraph only, after loading*
from utils import get_first_node
nodeid = 'first_node'
first_node = get_first_node(g)




# ===========================
print(f"""Profiling \033[92m2-hops\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# f'single_source_shortest_path_length(g, {nodeid}, cutoff=2)' contains quotes
avg_times |= {'2-hops': benchmark_autorange(f'single_source_shortest_path_length(g, {nodeid}, cutoff=2)', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# f'shortest_path_length(g, {nodeid})' contains quotes
avg_times |= {'shortest path': benchmark_autorange(f'shortest_path_length(g, {nodeid})', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mpage rank\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'pagerank(g, alpha=0.85, tol=1e-3, max_iter=10000000)' contains quotes
avg_times |= {'page rank': benchmark_autorange('pagerank(g, alpha=0.85, tol=1e-3, max_iter=10000000)', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mstrongly connected components\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# '[i for i in strongly_connected_components(g)]' contains quotes
avg_times |= {'strongly connected components': benchmark_autorange('[i for i in strongly_connected_components(g)]', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mconnected components\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# '[i for i in connected_components(g)]' contains quotes
avg_times |= {'connected components': benchmark_autorange('[i for i in connected_components(g)]', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()




# remove self loop from graph g before doing k-core


# if tool is easygraph



g.remove_edges_from(networkx.selfloop_edges(g))









# 'core.core_number(g)' contains quotes
avg_times |= {'k-core': benchmark_autorange('core.core_number(g)', globals=globals(), n=n) }







insert_results()