#!/usr/bin/env python3

from functools import partial
import json
from utils import print_with_hr
import networkx as nx
from config import (
    dataset_names,
    graph_info_json_path,
    sampled_graph_dir,
    default_target_node_number,
)
from dataset_loaders import *  # for er graphs

g = globals()
gi_d = json.loads(graph_info_json_path.read_text())


def sampled_dataset_loader(
    dataset: str, directed: bool = False
) -> nx.Graph | nx.DiGraph:
    print_with_hr(f'loading {dataset} from {sampled_graph_dir / f"{dataset}.edgelist"}')
    g = nx.read_edgelist(
        sampled_graph_dir / f'{dataset}.edgelist',
        nodetype=int,
        create_using=nx.DiGraph() if directed else nx.Graph(),
    )
    print(
        f"""loaded \033[33m{dataset} (sampled)\033[0m with {g.number_of_nodes()} nodes and {g.number_of_edges()} edges"""
    )
    return g


for dataset_name in dataset_names:
    if (
        dataset_name in gi_d
        and gi_d[dataset_name]['nodes'] > default_target_node_number
    ):
        g[f'load_{dataset_name}'] = partial(
            sampled_dataset_loader,
            dataset_name,
            directed=gi_d[dataset_name]['is_directed'],
        )
