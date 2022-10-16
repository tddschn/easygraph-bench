#!/usr/bin/env python3

import networkit as nk

from benchmark import benchmark_autorange

avg_times: list[float] = []

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

nk.engineering.setNumberOfThreads(16)

if "pokec" in filename:
    nodeid = 1
else:
    nodeid = 0

print(f"Profiling dataset {filename}")
print(f"using {nk.getMaxNumberOfThreads()} threads")

print("Profiling loading")
print("=================")
print()

avg_times.append(
    benchmark_autorange(
        "nk.graphio.EdgeListReader(separator='\t', firstNode=0, continuous=True, directed =True).read(filename)",
        globals=globals(),
        n=n,
    )
)
g = nk.graphio.EdgeListReader(
    separator="\t", firstNode=nodeid, continuous=True, directed=True
).read(filename)

print("Profiling shortest path")
print("=======================")
print()

avg_times.append(
    benchmark_autorange(
        "nk.distance.BFS(g, 0, storePaths=False).run().getDistances(False)",
        globals=globals(),
        n=n,
    )
)

print("Profiling PageRank")
print("==================")
print()

avg_times.append(
    benchmark_autorange(
        "nk.centrality.PageRank(g, damp=0.85, tol=1e-3).run().scores()",
        globals=globals(),
        n=n,
    )
)

print("Profiling k-core")
print("================")
print()

avg_times.append(
    benchmark_autorange(
        "nk.centrality.CoreDecomposition(g).run().scores()", globals=globals(), n=n
    )
)

print("Profiling strongly connected components")
print("=======================================")
print()

avg_times.append(
    benchmark_autorange(
        "nk.components.StronglyConnectedComponents(g).run().getPartition().getVector()",
        globals=globals(),
        n=n,
    )
)

profile_script_insert_results(__file__, filename, avg_times, args.iteration)
