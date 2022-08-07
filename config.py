#!/usr/bin/env python3

import sys
from pathlib import Path
from typing import Union

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
    "is_biconnected",
    "biconnected_components",
]

# methods takes G and a node as args
connected_components_methods_G_node = [
    # ("connected_component_of_node", 'node_connected_component'),
]

# connected_components_methods: list['Union[str, tuple[str, str]]'] = (
#     connected_components_methods_G + connected_components_methods_G_node
# )

mst_methods = ['minimum_spanning_tree']

load_functions_name = [
    "load_cheminformatics",
    "load_bio",
    "load_eco",
    # "load_soc"
]

di_load_functions_name = ["load_soc"]

dataset_names = [x.removeprefix('load_') for x in load_functions_name]
method_groups = ['clustering', 'shortest-path', 'connected-components', 'mst']
known_individual_bench_scripts = ['bench_cheminfo.py', 'bench_eco.py', 'bench_bio.py']
