#!/usr/bin/env python3

from graph_tool.all import *  # type: ignore


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
        description='Benchmark graphtool', formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
        '--print-graph-info-only',
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
print(f"""Profiling \033[96mgraphtool\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading_undirected\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# '''load_graph_from_csv(filename, directed=False, csv_options={'delimiter': '\t', 'quotechar': '"'})''' contains quotes
avg_times |= {'loading_undirected': benchmark_autorange('''load_graph_from_csv(filename, directed=False, csv_options={'delimiter': '\t', 'quotechar': '"'})''', globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval('''load_graph_from_csv(filename, directed=False, csv_options={'delimiter': '\t', 'quotechar': '"'})''')

if args.print_graph_info:
    
    print('graphtool does not support printing graph info.')
    

    if args.print_graph_info_only:
        sys.exit(0)









# ===========================
print(f"""Profiling \033[92m2-hops\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "shortest_distance(g, g.vertex(0), max_dist=2).a" contains quotes
avg_times |= {'2-hops': benchmark_autorange("shortest_distance(g, g.vertex(0), max_dist=2).a", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "shortest_distance(g, g.vertex(0)).a" contains quotes
avg_times |= {'shortest path': benchmark_autorange("shortest_distance(g, g.vertex(0)).a", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# 'kcore_decomposition(g).a' contains quotes
avg_times |= {'k-core': benchmark_autorange('kcore_decomposition(g).a', globals=globals(), n=n) }







insert_results()