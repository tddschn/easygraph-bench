#!/usr/bin/env python3

import networkit as nk


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results
import sqlite3

import argparse


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
    return parser.parse_args()


args = get_args()
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





# "nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)" contains quotes
avg_times |= {'loading_undirected': benchmark_autorange("nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)", globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval("nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)")








# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# "nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)" contains quotes
avg_times |= {'shortest path': benchmark_autorange("nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()




# remove self loop from graph g before doing k-core



g.removeSelfLoops()





# "nk.centrality.CoreDecomposition(g).run().scores()" contains quotes
avg_times |= {'k-core': benchmark_autorange("nk.centrality.CoreDecomposition(g).run().scores()", globals=globals(), n=n) }







try:
    profile_script_insert_results(__file__, filename, avg_times, args.iteration)
except sqlite3.OperationalError as e:
    print(f"Failed to insert results into database: \n{e}")
    print(f'Please run `./create_bench_results_db.py` to resolve this issue.')