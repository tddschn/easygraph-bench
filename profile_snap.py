#!/usr/bin/env python3

import snap  # type: ignore


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

print(f"Profiling dataset {filename}")


# ===========================
print("Profiling loading")
print("=================")
print()

#  contains quotes
avg_times |= {'loading': benchmark_autorange("snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)", globals=globals(), n=n) }


# loading* only
g = eval("snap.LoadEdgeListStr(snap.PNGraph, filename, 0, 1)")






# ===========================
print("Profiling 2-hops")
print("=================")
print()

#  contains quotes
avg_times |= {'2-hops': benchmark_autorange("snap.GetNodesAtHop(g, 0, 2, NodeVec, True)", globals=globals(), n=n) }





# ===========================
print("Profiling shortest path")
print("=================")
print()

#  contains quotes
avg_times |= {'shortest path': benchmark_autorange("snap.GetShortPath(g, 0, NIdToDistH, True)", globals=globals(), n=n) }





# ===========================
print("Profiling page rank")
print("=================")
print()

#  contains quotes
avg_times |= {'page rank': benchmark_autorange("snap.GetPageRank(g, PRankH, 0.85, 1e-3, 10000000)", globals=globals(), n=n) }





# ===========================
print("Profiling k-core")
print("=================")
print()

#  contains quotes
avg_times |= {'k-core': benchmark_autorange("snap.GetKCoreNodes(g, CoreIDSzV)", globals=globals(), n=n) }





# ===========================
print("Profiling strongly connected components")
print("=================")
print()

#  contains quotes
avg_times |= {'strongly connected components': benchmark_autorange("snap.GetSccs(g, Components)", globals=globals(), n=n) }






profile_script_insert_results(__file__, filename, avg_times, args.iteration)