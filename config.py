#!/usr/bin/env python3

from functools import cache
import sys
from pathlib import Path
from typing import Union

DATASET_DIR = Path(__file__).parent / "dataset"
graph_info_json_path = Path(__file__).parent / 'graph_info.json'
# BENCH_CSV_DIR = Path('~/Downloads/bench-csv').expanduser()
BENCH_CSV_DIR = Path(__file__).parent / 'output'
eg_master_dir = Path('~/testdir/Easy-Graph-master').expanduser()

tool_order = ['nx', 'eg', 'eg (C++)']

# (`eg.average_clustering` vs `nx.average_clustering`, ...)
clustering_methods = ["average_clustering", "clustering"]

# (`eg.Dijkstra` vs `nx.single_source_dijkstra_path`)
shortest_path_methods = [('Dijkstra', 'single_source_dijkstra_path')]

# methods that only takes G as arg
connected_components_methods_G = [
    # "is_connected",
    # "number_connected_components",
    "connected_components",
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

new_methods = ['strongly_connected_components']

# drop_methods = ['minimum_spanning_tree']
drop_methods = []


load_functions_name = [
    "load_cheminformatics",
    "load_bio",
    "load_eco",
    # "load_soc"
    'load_pgp',
    'load_pgp_undirected',
    'load_road',
    'load_uspowergrid',
    'load_enron',
    'load_google',
    'load_amazon',
    'load_coauthorship',
    # 'load_pokec',
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
    'mst',
    'other',
    'new',
]
bench_scripts_set = [
    'bench_scripts_normal',
    'bench_scripts_large',
    'bench_scripts_other',
    'bench_scripts_stub',
    'bench_scripts_all',
]
bench_scripts_normal = [
    'bench_cheminformatics.py',
    'bench_eco.py',
    'bench_bio.py',
    'bench_pgp.py',
    'bench_pgp_undirected.py',
    'bench_road.py',
    'bench_uspowergrid.py',
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

bench_scripts_other = ['bench_coauthorship.py']
bench_scripts_all = bench_scripts_normal + bench_scripts_large + bench_scripts_other

bench_scripts_stub = [
    'bench_stub.py',
    'bench_stub_with_underscore.py',
    'bench_stub_directed.py',
    'bench_stub_nx.py',
]

tool_name_mapping = {
    'networkx': 'nx',
    'eg w/ C++ binding': 'eg (C++)',
    'easygraph': 'eg',
}

dataset_name_mapping = {
    'cheminformatics': 'chem',
    'pgp_undirected': 'pgp (u)',
    'coauthorship': 'coauth',
}


slow_methods = {'constraint'}

dataset_homepage_mapping = {
    'cheminformatics': 'https://networkrepository.com/ENZYMES-g1.php',
    'bio': 'https://networkrepository.com/bio-yeast.php',
    'eco': 'https://networkrepository.com/econ-mahindas.php',
    'pgp': 'https://github.com/tddschn/easygraph-bench/blob/master/dataset/pgp/pgp.xml',
    'pgp_undirected': 'https://github.com/tddschn/easygraph-bench/blob/master/dataset/pgp/pgp_undirected.xml',
    'enron': 'https://snap.stanford.edu/data/email-Enron.html',
    'amazon': 'https://snap.stanford.edu/data/amazon0302.html',
    'google': 'https://snap.stanford.edu/data/web-Google.html',
    'pokec': 'https://snap.stanford.edu/data/soc-Pokec.html',
    'coauthorship': 'https://github.com/chenyang03/co-authorship-network',
    'road': 'https://networkrepository.com/road-usa.php',
    'uspowergrid': 'https://toreopsahl.com/datasets/#uspowergrid',
}


def get_method_order() -> list[str]:
    methods_list = [
        clustering_methods,
        shortest_path_methods,
        # connected_components_methods,
        connected_components_methods_G,
        connected_components_methods_G_node,
        mst_methods,
        other_methods,
    ]
    method_name_list = []
    for l in methods_list:
        for method_name in l:
            if isinstance(method_name, tuple):
                method_name_list.append(method_name[0])
            else:
                method_name_list.append(method_name)
    return method_name_list


def get_nx_methods_for_method_group(method_group: str) -> list[str]:
    if not method_group in method_groups:
        raise ValueError(f'no method group {method_group}')
    method_group = globals()[f'{method_group}_methods']
    nx_methods = []
    for method_name in method_group:
        if isinstance(method_name, tuple):
            nx_methods.append(method_name[1])
        else:
            nx_methods.append(method_name)
    return nx_methods
