#!/usr/bin/env python3

import sys
from pathlib import Path
from typing import Union

eg_master_dir = Path('~/testdir/Easy-Graph-master').expanduser()

clustering_methods = ["average_clustering", "clustering"]
shortest_path_methods = [('Dijkstra', 'single_source_dijkstra_path')]
connected_components_methods_G = [
    "is_connected",
    "number_connected_components",
    "connected_components",
]

connected_components_methods_G_node = [
    ("connected_component_of_node", 'node_connected_component'),
]

# connected_components_methods: list['Union[str, tuple[str, str]]'] = (
#     connected_components_methods_G + connected_components_methods_G_node
# )

load_functions_name = [
    "load_cheminformatics",
    "load_bio",
    "load_eco",
    # "load_soc"
]

di_load_functions_name = ["load_soc"]

dataset_names = [x.removeprefix('load_') for x in load_functions_name]
method_groups = ['clustering', 'shortest-path', 'connected-components', 'MST']
