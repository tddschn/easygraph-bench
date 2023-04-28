#!/usr/bin/env python3

import networkit as nk


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
        description='Benchmark networkit', formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
print(f"""Profiling \033[96mnetworkit\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading_undirected\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()


# easygraph constraint doesn't have c bindings
# if method starts with 'constraint', then use python version of graph



    

# "nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)" contains quotes
avg_times |= {'loading_undirected': benchmark_autorange("nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)", globals=globals(), n=n) }

# if tool starts with 'constraint' and

# easygraph constraint doesn't have c bindings
# if method starts with 'constraint', then convert g back



# loading* only, make g in the globals() so the methods after loading methods can access it.
    
g = eval("nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)")
    


if args.print_graph_info:
    
    print('networkit does not support printing graph info.')
    

    if args.print_graph_info_only:
        sys.exit(0)



    




# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()


# easygraph constraint doesn't have c bindings
# if method starts with 'constraint', then use python version of graph



    

# "nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)" contains quotes
avg_times |= {'shortest path': benchmark_autorange("nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)", globals=globals(), n=n) }

# if tool starts with 'constraint' and

# easygraph constraint doesn't have c bindings
# if method starts with 'constraint', then convert g back






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()


# easygraph constraint doesn't have c bindings
# if method starts with 'constraint', then use python version of graph



    

# remove self loop from graph g before doing k-core
        

    
g.removeSelfLoops()
    



# "nk.centrality.CoreDecomposition(g).run().scores()" contains quotes
avg_times |= {'k-core': benchmark_autorange("nk.centrality.CoreDecomposition(g).run().scores()", globals=globals(), n=n) }

# if tool starts with 'constraint' and

# easygraph constraint doesn't have c bindings
# if method starts with 'constraint', then convert g back







insert_results()