#!/usr/bin/env python3

import easygraph as eg
import easygraph
# from easygraph import *  # type: ignore
from easygraph import Dijkstra, pagerank, strongly_connected_components, read_edgelist, multi_source_dijkstra, k_core, betweenness_centrality, closeness_centrality


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
print(f"""Profiling \033[92mloading\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# 'read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.DiGraph()).cpp()' contains quotes
avg_times |= {'loading': benchmark_autorange('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.DiGraph()).cpp()', globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval('read_edgelist(filename, delimiter="\t", nodetype=int, create_using=eg.DiGraph()).cpp()')





# networkx & easygraph only, after loading*
from utils import get_first_node
nodeid = 'first_node'
first_node = get_first_node(g)




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







profile_script_insert_results(__file__, filename, avg_times, args.iteration)