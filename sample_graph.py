#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-10-31
Purpose: Why not?
"""

import argparse
import json
from pathlib import Path
from config import DATASET_DIR, dataset_names, graph_info_json_path

sampled_graph_dir = DATASET_DIR / 'sampled'
default_target_node_number = 10000


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?', formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-n',
        '--target-node-number',
        help='Target node number',
        metavar='int',
        type=int,
        default=default_target_node_number,
    )

    parser.add_argument(
        '-t',
        '--nodes-threshold-to-sample',
        help='Only sample datasets with more nodes than this number',
        metavar='int',
        type=int,
        default=default_target_node_number,
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()

    from littleballoffur import PageRankBasedSampler  # type: ignore
    import dataset_loaders
    import networkx as nx
    from utils import eg2nx

    sampler = PageRankBasedSampler(number_of_nodes=args.target_node_number)
    gi_d = json.loads(graph_info_json_path.read_text())
    for dataset, info in gi_d.items():
        if info['nodes'] > args.nodes_threshold_to_sample:
            print(
                f'sampling {dataset} with {info["nodes"]} nodes and {info["edges"]} edges'
            )
            g = getattr(dataset_loaders, f'load_{dataset}')()
            if not isinstance(g, (nx.Graph, nx.DiGraph)):
                g = eg2nx(g)

            new_graph = sampler.sample(g)
            sampled_graph_dir.mkdir(exist_ok=True)
            new_graph_path = sampled_graph_dir / f'{dataset}.edgelist'
            print(f'saving to {new_graph_path}')
            nx.write_edgelist(new_graph, new_graph_path)


if __name__ == '__main__':
    main()
