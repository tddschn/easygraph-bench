#!/usr/bin/env python3

from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results

avg_times: list[float] = []

from graph_tool.all import *  # type: ignore
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


openmp_set_num_threads(16)

print(f"Profiling dataset {filename}")
print(f"using {openmp_get_num_threads()} threads")

print("Profiling loading")
print("=================")
print()

avg_times.append(
    benchmark_autorange(
        '''load_graph_from_csv(filename, directed=True, csv_options={'delimiter': '\t', 'quotechar': '"'})''',
        globals=globals(),
        n=n,
    )
)
g = load_graph_from_csv(
    filename, directed=True, csv_options={'delimiter': '\t', 'quotechar': '"'}
)

print("Profiling 2-hops")
print("================")
print()

avg_times.append(
    benchmark_autorange(
        "shortest_distance(g, g.vertex(0), max_dist=2).a", globals=globals(), n=n
    )
)

print("Profiling shortest path")
print("=======================")
print()

avg_times.append(
    benchmark_autorange("shortest_distance(g, g.vertex(0)).a", globals=globals(), n=n)
)

print("Profiling PageRank")
print("==================")
print()

avg_times.append(
    benchmark_autorange(
        'pagerank(g, damping=0.85, epsilon=1e-3, max_iter=10000000).a',
        globals=globals(),
        n=n,
    )
)

print("Profiling k-core")
print("================")
print()

avg_times.append(
    benchmark_autorange('kcore_decomposition(g).a', globals=globals(), n=n)
)

print("Profiling strongly connected components")
print("=======================================")
print()

avg_times.append(
    benchmark_autorange(
        'cc, _ = label_components(g, vprop=None, directed=True, attractors=False); cc.a',
        globals=globals(),
        n=n,
    )
)


profile_script_insert_results(__file__, filename, avg_times, args.iteration)
