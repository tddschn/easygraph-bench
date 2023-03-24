#!/usr/bin/env python3

from graph_tool.all import *  # type: ignore


from benchmark import benchmark_autorange
from utils_db import profile_script_insert_results

import argparse


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
    return parser.parse_args()


args = get_args()
filename = args.dataset
n = args.iteration

# filename = sys.argv[1]
# n = int(sys.argv[2])

avg_times: dict[str, float] = {}

print('''\033[91m=================================\033[0m''')
print(f"""Profiling \033[96mgraphtool\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')




# ===========================
print(f"""Profiling \033[92mloading\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# '''load_graph_from_csv(filename, directed=True, csv_options={'delimiter': '\t', 'quotechar': '"'})''' contains quotes
avg_times |= {'loading': benchmark_autorange('''load_graph_from_csv(filename, directed=True, csv_options={'delimiter': '\t', 'quotechar': '"'})''', globals=globals(), n=n) }



# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval('''load_graph_from_csv(filename, directed=True, csv_options={'delimiter': '\t', 'quotechar': '"'})''')








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
print(f"""Profiling \033[92mpage rank\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# 'pagerank(g, damping=0.85, epsilon=1e-3, max_iter=10000000).a' contains quotes
avg_times |= {'page rank': benchmark_autorange('pagerank(g, damping=0.85, epsilon=1e-3, max_iter=10000000).a', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mk-core\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# 'kcore_decomposition(g).a' contains quotes
avg_times |= {'k-core': benchmark_autorange('kcore_decomposition(g).a', globals=globals(), n=n) }






# ===========================
print(f"""Profiling \033[92mstrongly connected components\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()



# 'cc, _ = label_components(g, vprop=None, directed=True, attractors=False); cc.a' contains quotes
avg_times |= {'strongly connected components': benchmark_autorange('cc, _ = label_components(g, vprop=None, directed=True, attractors=False); cc.a', globals=globals(), n=n) }







profile_script_insert_results(__file__, filename, avg_times, args.iteration)