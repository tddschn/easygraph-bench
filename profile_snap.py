#!/usr/bin/env python3

import snap  # type: ignore


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results

import argparse


def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser(
        description='Benchmark snap', formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
print(f"""Profiling \033[96msnap\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)" contains quotes
avg_times |= {'loading': benchmark_autorange("snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)", globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval("snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)")








# ===========================
print(f"""Profiling \033[92m2-hops\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "snap.GetNodesAtHop(g, 0, 2, NodeVec, True)" contains quotes
avg_times |= {'2-hops': benchmark_autorange("snap.GetNodesAtHop(g, 0, 2, NodeVec, True)", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mshortest path\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "snap.GetShortPath(g, 0, NIdToDistH, True)" contains quotes
avg_times |= {'shortest path': benchmark_autorange("snap.GetShortPath(g, 0, NIdToDistH, True)", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mpage rank\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "snap.GetPageRank(g, PRankH, 0.85, 1e-3, 10000000)" contains quotes
avg_times |= {'page rank': benchmark_autorange("snap.GetPageRank(g, PRankH, 0.85, 1e-3, 10000000)", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "snap.GetKCoreNodes(g, CoreIDSzV)" contains quotes
avg_times |= {'k-core': benchmark_autorange("snap.GetKCoreNodes(g, CoreIDSzV)", globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mstrongly connected components\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# "snap.GetSccs(g, Components)" contains quotes
avg_times |= {'strongly connected components': benchmark_autorange("snap.GetSccs(g, Components)", globals=globals(), n=n) }







profile_script_insert_results(__file__, filename, avg_times, args.iteration)