#!/usr/bin/env python3

import networkx as nx
from networkx import *  # type: ignore


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results

import argparse


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
    return parser.parse_args()


args = get_args()
filename = args.dataset
n = args.iteration

# filename = sys.argv[1]
# n = int(sys.argv[2])

avg_times: dict[str, float] = {}

print('''\033[91m=================================\033[0m''')
print(f"""Profiling \033[96mnetworkx\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading_undirected\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.Graph())' contains quotes
avg_times |= {'loading_undirected': benchmark_autorange('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.Graph())', globals=globals(), n=n) }


# loading* only
g = eval('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.Graph())')




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
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()




# remove self loop from graph g before doing k-core

g.remove_edges_from(nx.selfloop_edges(g))







# 'core.core_number(g)' contains quotes
avg_times |= {'k-core': benchmark_autorange('core.core_number(g)', globals=globals(), n=n) }







profile_script_insert_results(__file__, filename, avg_times, args.iteration)