#!/usr/bin/env python3

{{ profile_preparation_code }}

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
        description='Benchmark {{ tool }}', formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
print(f"""Profiling \033[96m{{ tool }}\033[0m on dataset \033[34m{filename}\033[0m""")
print('''\033[91m=================================\033[0m''')

{{ profile_code }}

{% for method, code in graph_benchmark_code.items() %}
# ===========================
print(f"""Profiling \033[92m{{ method }}\033[0m on dataset \033[34m{filename}\033[0m""")
print("=================")
print()

{% if tool in ('networkx', 'networkit', 'easygraph') %}
{% if method == 'k-core' %}

# remove self loop from graph g before doing k-core
{% if tool in ('networkx', 'easygraph') %}

# if tool is easygraph
{% if tool == 'easygraph' %}
# give eg access to a python version of Graph first, so that removing self loops is possible
# eval code.removesuffix('.cpp()')
{# g_python = eval({{ loading_code_str }}.removesuffix('.cpp()')) #}
g_og = g
g_python = g.py()
g = g_python
g.remove_edges({{ tool }}.selfloop_edges(g))
g = g.cpp()
{% endif %}

{% if tool == 'networkx' %}
g.remove_edges_from({{ tool }}.selfloop_edges(g))
{% endif %}

{% endif %}

{% if tool == 'networkit' %}
g.removeSelfLoops()
{% endif %}

{% endif %}
{% endif %}

# {{ code }} contains quotes
avg_times |= {'{{ method }}': benchmark_autorange({{ code }}, globals=globals(), n=n) }

{% if method in ('loading', 'loading_undirected') %}

# loading* only, make g in the globals() so the methods after loading methods can access it.
g = eval({{ code }})

if args.print_graph_info:
    {% if print_graph_info %}
    {{ print_graph_info }}
    {% else %}
    print('{{ tool }} does not support printing graph info.')
    {% endif %}

    if args.print_graph_info_only:
        sys.exit(0)

{# {% set loading_code_str = {{ code }} %} #}
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

insert_results()