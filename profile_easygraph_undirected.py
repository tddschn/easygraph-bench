#!/usr/bin/env python3

import easygraph as eg
import easygraph
# from easygraph import *  # type: ignore
from easygraph import Dijkstra, pagerank, strongly_connected_components, read_edgelist, multi_source_dijkstra, k_core, betweenness_centrality, closeness_centrality, connected_components, connected_components_directed
# disable warnings
import warnings
warnings.filterwarnings("ignore")


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results

import argparse


def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser(
        description='Benchmark easygraph', formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
print(f"""Profiling \033[96measygraph\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading_undirected\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.Graph()).cpp()' contains quotes
avg_times |= {'loading_undirected': benchmark_autorange('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.Graph()).cpp()', globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.Graph()).cpp()')





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
print(f"""Profiling \033[92mpage rank\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'pagerank(g)' contains quotes
avg_times |= {'page rank': benchmark_autorange('pagerank(g)', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mbetweenness centrality\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'betweenness_centrality(g)' contains quotes
avg_times |= {'betweenness centrality': benchmark_autorange('betweenness_centrality(g)', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mcloseness centrality\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'closeness_centrality(g)' contains quotes
avg_times |= {'closeness centrality': benchmark_autorange('closeness_centrality(g)', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()




# remove self loop from graph g before doing k-core


# if tool is easygraph

# give eg access to a python version of Graph first, so that removing self loops is possible
# eval code.removesuffix('.cpp()')

g_og = g
g_python = g.py()
g = g_python
g.remove_edges(easygraph.selfloop_edges(g))
g = g.cpp()











# 'k_core(g)' contains quotes
avg_times |= {'k-core': benchmark_autorange('k_core(g)', globals=globals(), n=n) }







profile_script_insert_results(__file__, filename, avg_times, args.iteration)