#!/usr/bin/env python3

from igraph import *  # type: ignore


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results
import sqlite3

import argparse


def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser(
        description='Benchmark igraph', formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
print(f"""Profiling \033[96migraph\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "Graph.Read(filename, format='edges')" contains quotes
avg_times |= {'loading': benchmark_autorange("Graph.Read(filename, format='edges')", globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval("Graph.Read(filename, format='edges')")








# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "g.distances(source=[g.vs[0]], weights=[1]*len(g.es), )" contains quotes
avg_times |= {'shortest path': benchmark_autorange("g.distances(source=[g.vs[0]], weights=[1]*len(g.es), )", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mpage rank\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "g.pagerank(damping=0.85)" contains quotes
avg_times |= {'page rank': benchmark_autorange("g.pagerank(damping=0.85)", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mbetweenness centrality\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "g.betweenness()" contains quotes
avg_times |= {'betweenness centrality': benchmark_autorange("g.betweenness()", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mcloseness centrality\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "g.closeness()" contains quotes
avg_times |= {'closeness centrality': benchmark_autorange("g.closeness()", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "g.coreness(mode='all')" contains quotes
avg_times |= {'k-core': benchmark_autorange("g.coreness(mode='all')", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mstrongly connected components\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "[i for i in g.components(mode=STRONG)]" contains quotes
avg_times |= {'strongly connected components': benchmark_autorange("[i for i in g.components(mode=STRONG)]", globals=globals(), n=n) }







try:
    profile_script_insert_results(__file__, filename, avg_times, args.iteration)
except sqlite3.OperationalError as e:
    print(f"Failed to insert results into database: \n{e}")
    print(f'Please run `./create_bench_results_db.py` to resolve this issue.')