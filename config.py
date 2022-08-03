#!/usr/bin/env python3

import sys
from pathlib import Path

eg_master_dir = Path('~/testdir/Easy-Graph-master').expanduser()

clustering_methods = ["average_clustering", "clustering"]
shortest_path_methods = ['Dijkstra']

load_functions_name = [
    "load_cheminformatics",
    # "load_bio",
    # "load_eco",
    # "load_soc"
]

di_load_functions_name = ["load_soc"]

method_groups = ['clustering', 'shortest-path', 'connected-components', 'MST']
