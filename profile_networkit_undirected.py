#!/usr/bin/env python3

import networkit as nk


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
print(f"""Profiling \033[92mloading_undirected\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# "nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)" contains quotes
avg_times |= {'loading_undirected': benchmark_autorange("nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)", globals=globals(), n=n) }


# loading* only
g = eval("nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True).read(filename)")







# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# "nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)" contains quotes
avg_times |= {'shortest path': benchmark_autorange("nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mpage rank\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()





# "nk.centrality.PageRank(g, damp=0.85, tol=1e-3).run().scores()" contains quotes
avg_times |= {'page rank': benchmark_autorange("nk.centrality.PageRank(g, damp=0.85, tol=1e-3).run().scores()", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()




# remove self loop from graph g before doing k-core



g.removeSelfLoops()





# "nk.centrality.CoreDecomposition(g).run().scores()" contains quotes
avg_times |= {'k-core': benchmark_autorange("nk.centrality.CoreDecomposition(g).run().scores()", globals=globals(), n=n) }







profile_script_insert_results(__file__, filename, avg_times, args.iteration)