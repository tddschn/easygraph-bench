#!/usr/bin/env python3

{{ profile_preparation_code }}

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

{{ profile_code }}

{% for method, code in graph_benchmark_code.items() %}
# ===========================
print(f"""Profiling \033[92m{{ method }}\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()

{% if tool in ('networkx', 'networkit') %}
{% if method == 'k-core' %}

# remove self loop from graph g before doing k-core
{% if tool == 'networkx' %}
g.remove_edges_from(nx.selfloop_edges(g))
{% endif %}

{% if tool == 'networkit' %}
g.removeSelfLoops()
{% endif %}

{% endif %}
{% endif %}

# {{ code }} contains quotes
avg_times |= {'{{ method }}': benchmark_autorange({{ code }}, globals=globals(), n=n) }

{% if method in ('loading', 'loading_undirected') %}
# loading* only
g = eval({{ code }})
{% endif %}

{% if method in ('loading', 'loading_undirected') %}
{% if tool in ('networkx', 'easygraph') %}
# networkx & easygraph only, after loading*
from utils import get_first_node
nodeid = 'first_node'
first_node = get_first_node(g)
{% endif %}
{% endif %}

{% endfor %}

profile_script_insert_results(__file__, filename, avg_times, args.iteration)