#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-10-31
Purpose: Why not?
"""

import argparse
import json
from pathlib import Path
from config import (
    DATASET_DIR,
    dataset_names,
    graph_info_json_path,
    default_target_node_number,
    sampled_graph_dir,
)


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

    parser.add_argument(
        '-d', '--directed-only', help='Only sample directed graphs', action='store_true'
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()

    from littleballoffur import PageRankBasedSampler  # type: ignore
    import dataset_loaders
    import networkx as nx
    from utils import eg2nx, randomly_sample_directed_graph
    from get_graph_info import get_graph_info

    sampler = PageRankBasedSampler(number_of_nodes=args.target_node_number)
    gi_d = json.loads(graph_info_json_path.read_text())
    for dataset, info in gi_d.items():
        if info['nodes'] > args.nodes_threshold_to_sample:
            print(f'\033[94m{dataset}\033[0m')
            if info['is_directed']:
                # print(f'skipping {dataset} because it is directed')
                try:
                    g = getattr(dataset_loaders, f'load_{dataset}')()
                except Exception as e:
                    print(f'''failed to load \033[31m{dataset}\033[0m: {e}''')
                    continue
                if not isinstance(g, (nx.Graph, nx.DiGraph)):
                    g = eg2nx(g)
                print(f'sampling {dataset}')
                print('before: ')
                print(info)
                # relabel g
                print('relabeling...')
                g = nx.convert_node_labels_to_integers(g)

                new_graph = randomly_sample_directed_graph(g, args.target_node_number)
                sampled_graph_dir.mkdir(exist_ok=True)
                new_graph_path = sampled_graph_dir / f'{dataset}.edgelist'
                print(f'sampled {dataset}')
                print('after: ')
                print(get_graph_info(new_graph))
                print(f'saving to {new_graph_path}')
                nx.write_edgelist(new_graph, new_graph_path)

                continue
            if args.directed_only and not info['is_directed']:
                print(
                    f'skipping {dataset} because it is not directed (--directed-only specified)'
                )
                continue
            try:
                g = getattr(dataset_loaders, f'load_{dataset}')()
            except Exception as e:
                print(f'''failed to load \033[31m{dataset}\033[0m: {e}''')
                continue
            if not isinstance(g, (nx.Graph, nx.DiGraph)):
                g = eg2nx(g)
            print(
                f'sampling {dataset} with {info["nodes"]} nodes and {info["edges"]} edges'
            )
            print('before: ')
            print(info)
            # relabel g
            print('relabeling...')
            g = nx.convert_node_labels_to_integers(g)

            new_graph = sampler.sample(g)
            sampled_graph_dir.mkdir(exist_ok=True)
            new_graph_path = sampled_graph_dir / f'{dataset}.edgelist'
            print(f'sampled {dataset}')
            print('after: ')
            print(get_graph_info(new_graph))
            print(f'saving to {new_graph_path}')
            nx.write_edgelist(new_graph, new_graph_path)


if __name__ == '__main__':
    main()
