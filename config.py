#!/usr/bin/env python3

import sys
from pathlib import Path
from typing import Union

DATASET_DIR = Path(__file__).parent / "dataset"
BENCH_CSV_DIR = Path('~/Downloads/bench-csv').expanduser()
eg_master_dir = Path('~/testdir/Easy-Graph-master').expanduser()

# (`eg.average_clustering` vs `nx.average_clustering`, ...)
clustering_methods = ["average_clustering", "clustering"]

# (`eg.Dijkstra` vs `nx.single_source_dijkstra_path`)
shortest_path_methods = [('Dijkstra', 'single_source_dijkstra_path')]

# methods that only takes G as arg
connected_components_methods_G = [
    # "is_connected",
    # "number_connected_components",
    # "connected_components",
    # "is_biconnected",
    "biconnected_components",
]

# methods takes G and a node as args
connected_components_methods_G_node = [
    # ("connected_component_of_node", 'node_connected_component'),
]

# connected_components_methods: list['Union[str, tuple[str, str]]'] = (
#     connected_components_methods_G + connected_components_methods_G_node
# )

# you can't access kruskal by just importing the top level package
# i.e. it's not marked to export
mst_methods = ['minimum_spanning_tree']
# mst_methods = ['kruskal_mst_edges']

other_methods = ['density', 'constraint']

load_functions_name = [
    "load_cheminformatics",
    "load_bio",
    "load_eco",
    # "load_soc"
    'load_pgp',
    'load_pgp_undirected',
    'load_enron',
    'load_google',
    'load_amazon',
    'load_coauthorship',
    'load_pokec',
    'load_stub',
    'load_stub_with_underscore',
    'load_stub_directed',
    'load_stub_nx',
]

di_load_functions_name = ["load_soc"]

dataset_names = [x.removeprefix('load_') for x in load_functions_name]
method_groups = [
    'clustering',
    'shortest-path',
    'connected-components',
    # 'mst',
    'other',
]
bench_scripts_set = [
    'bench_scripts_normal',
    'bench_scripts_large',
    'bench_scripts_stub',
]
bench_scripts_normal = [
    'bench_cheminformatics.py',
    'bench_eco.py',
    'bench_bio.py',
    'bench_pgp.py',
    'bench_pgp_undirected.py',
]

bench_scripts_large = [
    'bench_enron.py',
    # eg throws error with this graph
    # https://github.com/tddschn/easygraph-bench-private/runs/8149890856?check_suite_focus=true
    # 'bench_google.py',
    'bench_amazon.py',
    # too large, got killed by GHA
    # https://github.com/tddschn/easygraph-bench/runs/8166648033?check_suite_focus=true#step:9:408
    # 'bench_pokec.py',
]

ben_scripts_coauthorship = ['bench_coauthorship.py']

bench_scripts_stub = [
    'bench_stub.py',
    'bench_stub_with_underscore.py',
    'bench_stub_directed.py',
    'bench_stub_nx.py',
]

tool_name_mapping = {
    'networkx': 'nx',
    'eg w/ C++ binding': 'eg (C++)',
    'easygraph': 'eg'
}