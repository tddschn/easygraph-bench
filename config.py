#!/usr/bin/env python3

from functools import cache
import sys
from pathlib import Path
from typing import Union
from utils_other import get_dataset_list_sorted_by_nodes_and_edges

DATASET_DIR = Path(__file__).parent / "dataset"
graph_info_json_path = Path(__file__).parent / 'graph_info.json'
graph_info_table_name = 'graph_info'
bench_results_table_name = 'bench_results'
bench_results_db_path = Path(__file__).parent / 'bench-results.db'
# BENCH_CSV_DIR = Path('~/Downloads/bench-csv').expanduser()
BENCH_CSV_DIR = Path(__file__).parent / 'output'
eg_master_dir = Path('~/testdir/Easy-Graph-master').expanduser()
TIMLRX_DIR = Path(__file__).parent / 'timlrx'
profile_preparation_yaml_path = TIMLRX_DIR / 'profile-preparation-code.yaml'
graph_benchmark_code_json_path = TIMLRX_DIR / 'graph-benchmark-code.json'

# loading first, k-core last because it mutates graph by removing self loops
graph_benchmark_method_order = [
    'loading',
    'loading_undirected',
    'shortest path',
    'page rank',
    'betweenness centrality',
    'closeness centrality',
    'k-core',
    'strongly connected components',  # tim put this last
]

# not deprecated
# directly editing the ordereddict yaml is easier than rewriting a lot of code
graph_benchmark_code_yaml_path = TIMLRX_DIR / 'graph-benchmark-code.yaml'
graph_benchmark_code_ordereddict_yaml_path = (
    TIMLRX_DIR / 'graph-benchmark-code-ordereddict.yaml'
)

tool_order = ['nx', 'eg', 'eg (C++)']

# (`eg.average_clustering` vs `nx.average_clustering`, ...)
# clustering_methods = ["average_clustering", "clustering"]
clustering_methods = ["clustering"]

# (`eg.Dijkstra` vs `nx.single_source_dijkstra_path`)
shortest_path_methods = [('Dijkstra', 'single_source_dijkstra_path')]

# methods that only takes G as arg
connected_components_methods_G = [
    # "is_connected",
    # "number_connected_components",
    # "connected_components",
    # "is_biconnected",
    "biconnected_components",
    # 'strongly_connected_components',
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

# new_methods = ['effective_size', ('hierarchy', 'flow_hierarchy'), 'efficiency']
# new_methods = ['effective_size', 'efficiency']
new_methods = ['effective_size']

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
    # 'load_google',
    # 'load_amazon',
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

tool_name_mapping_for_DTForTools = {
    'networkx': 'nx',
    'eg w/ C++ binding': 'ceg',
    'easygraph': 'eg',
}

dataset_name_mapping = {
    'cheminformatics': 'chem',
    'pgp_undirected': 'pgp (u)',
    'coauthorship': 'coauth',
}


slow_methods = {'constraint', 'effective_size'}

random_erdos_renyi_graphs_dir = Path(__file__).parent / 'dataset' / 'random-erdos-renyi'
random_erdos_renyi_graphs_paths = sorted(
    random_erdos_renyi_graphs_dir.glob('*.edgelist'),
    key=lambda p: int(p.stem.removesuffix('_directed')),
)
random_erdos_renyi_graphs_load_function_names = [
    f'load_er_{p.stem}' for p in random_erdos_renyi_graphs_paths
]

# dataset_names = [x.removeprefix('load_') for x in load_functions_name]
random_erdos_renyi_dataset_names = [
    x.removeprefix('load_') for x in random_erdos_renyi_graphs_load_function_names
]

er_dataset_names_for_paper_20221213 = [
    # 0.5k, 5k, 50k, 500k, 1000k
    f'er_{x}'
    for x in (50000, 500000, 1000000)
]

er_dataset_edges_count_for_paper_20221213 = [60_000, 70_000, 80_000]

# random_erdos_renyi_graphs_dir = Path(__file__).parent / 'dataset' / 'random-erdos-renyi'
random_erdos_renyi_graphs_paths_date_s = sorted(
    DATASET_DIR.glob('er-paper-*/*.*'),
    key=lambda p: (
        int(p.parent.name.removeprefix('er-paper-')),
        int(p.stem.removesuffix('_directed')),
    ),
)

random_erdos_renyi_graphs_load_function_names_date_s = [
    f'load_er_paper_{p.parent.name.removeprefix("er-paper-")}_{p.stem}'
    for p in random_erdos_renyi_graphs_paths_date_s
]
# for sampling graphs
sampled_graph_dir = DATASET_DIR / 'sampled'
default_target_node_number = 10000
sampled_graph_dataset_names = sorted(
    (f'{x.stem}_sampled' for x in sorted(sampled_graph_dir.glob('*.edgelist'))),
    key=lambda dataset_name: get_dataset_list_sorted_by_nodes_and_edges().index(
        dataset_name
    )
    if dataset_name in get_dataset_list_sorted_by_nodes_and_edges()
    else 1000000,
)

easygraph_multipcoessing_methods = [
    'laplacian',
    'betweenness_centrality',
    'closeness_centrality',
    'constraint',
    'hierarchy',
    'effective_size',
]

easygraph_multipcoessing_methods_available_in_networkx = {
    'betweenness_centrality',
    'closeness_centrality',
    "effective_size",
}

easygraph_multipcoessing_methods_for_paper = {
    'betweenness_centrality',
    'closeness_centrality',
    'constraint',
    'hierarchy',
}

easygraph_multiprocessing_n_workers_options = [2, 4, 8]
easygraph_multiprocessing_n_workers_options_for_paper = [2, 4]
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
    **{
        bench_script_name.removeprefix('bench_').removesuffix(
            '.py'
        ): 'https://github.com/tddschn/easygraph-bench/blob/master/dataset_loaders.py'
        for bench_script_name in bench_scripts_stub
    },
    **{
        er_dataset_name: 'https://github.com/tddschn/easygraph-bench/blob/master/dataset_loaders.py'
        for er_dataset_name in random_erdos_renyi_dataset_names
        + [
            x.removeprefix('load_')
            for x in random_erdos_renyi_graphs_load_function_names_date_s
        ]
    },
    **{
        sampled_graph_dataset_name: 'https://github.com/tddschn/easygraph-bench/blob/master/dataset/sampled'
        for sampled_graph_dataset_name in sampled_graph_dataset_names
    },
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


graph_property_to_excel_field_mapping = {
    'is_directed': 'directed?',
}


methods_timlrx = [
    'loading',
    'shortest path',
    'page rank',
    'k-core',
    'strongly connected components',
]
methods6_timlrx = methods_timlrx.copy()
methods6_timlrx.insert(1, '2-hops')

dataset_edgelist_filenames = [
    'cheminformatics',
    'bio',
    'eco',
    'pgp',
    'pgp_undirected',
    'road',
    'uspowergrid',
]
edgelist_filenames = [f'dataset/{x}.edgelist' for x in dataset_edgelist_filenames] + [
    'enron.txt',
    'amazon.txt',
    'google.txt',
    'pokec.txt',
]

edgelist_filenames_lcc = []
for filename in edgelist_filenames:
    if not Path(filename).exists():
        continue
    edgelist_filenames_lcc.append(str(Path(filename).with_stem(f"{Path(filename).stem}_lcc")))


@cache
def read_profile_preparation_code() -> dict[str, str]:
    import yaml

    return yaml.safe_load(profile_preparation_yaml_path.read_text())


# snap doesn't support python 3.10 and it sucks, so
profile_tools_to_drop = {'snap'}

dataset_names_for_paper_multiprocessing = [
    'bio',
    'uspowergrid',
    'enron',
    'coauthorship',
]
er_dataset_names_for_paper_multiprocessing = [
    f'er_{x}' for x in (500, 1000, 5000, 10000)
]

# cSpell:disable
# From gaomin:
# 增加multiprocessing和hybrid programming针对random graph的benckmark， 其中node size分别取0.5k, 5k, 50k, 500k, 1000k的不同algorithm的runtime效果（之前生成ER图的参数p的设定问题可以采用另一个function：erdos_renyi_M， 可以直接设定edge size的大小）
# cSpell:enable
