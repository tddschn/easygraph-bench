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

    parser.add_argument(
        '--one',
        '-1',
        help='Only sample one graph',
        action='store_true',
        dest='sample_only_one',
    )

    parser.add_argument(
        '-g',
        '--graph-name',
        help='Requires --one. Graph name as defined in the graph_info_json file',
        metavar='str',
        type=str,
        # default=graph_name,
    )

    parser.add_argument(
        '-o',
        '--output-path',
        help='Requires --one. Output file path to save the sampled graph',
        metavar='str',
        type=str,
        # default=output_path,
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.sample_only_one:
        main_process_one(args)
        return

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


def main_process_one(args):
    """
    give me a modified version of main() so that it accepts a graph name defined in the graph_info_json json file, sample that graph, and let user specify where to save the sampled graph
    https://chat.openai.com/chat/8e2dae3c-17bd-482b-b996-f1fb53e02cfc
    """

    # args = get_args()

    from littleballoffur import PageRankBasedSampler  # type: ignore
    import dataset_loaders
    import networkx as nx
    from utils import eg2nx, randomly_sample_directed_graph
    from get_graph_info import get_graph_info

    # Add the following lines to accept the graph_name and output_path as arguments
    # graph_name = input("Enter the graph name as defined in the graph_info_json file: ")
    # output_path = input("Enter the output file path to save the sampled graph: ")
    graph_name = args.graph_name
    output_path = args.output_path
    assert graph_name is not None
    assert output_path is not None

    sampler = PageRankBasedSampler(number_of_nodes=args.target_node_number)
    gi_d = json.loads(graph_info_json_path.read_text())
    info = gi_d.get(graph_name)
    if info:
        if info['nodes'] > args.nodes_threshold_to_sample:
            print(f'\033[94m{graph_name}\033[0m')
            if info['is_directed']:
                try:
                    g = getattr(dataset_loaders, f'load_{graph_name}')()
                except Exception as e:
                    print(f'''failed to load \033[31m{graph_name}\033[0m: {e}''')
                    return
                if not isinstance(g, (nx.Graph, nx.DiGraph)):
                    g = eg2nx(g)
                print(f'sampling {graph_name}')
                print('before: ')
                print(info)
                print('relabeling...')
                g = nx.convert_node_labels_to_integers(g)

                new_graph = randomly_sample_directed_graph(g, args.target_node_number)
                print(f'sampled {graph_name}')
                print('after: ')
                print(get_graph_info(new_graph))
                print(f'saving to {output_path}')
                nx.write_edgelist(new_graph, output_path)

                return
            if args.directed_only and not info['is_directed']:
                print(
                    f'skipping {graph_name} because it is not directed (--directed-only specified)'
                )
                return
            try:
                g = getattr(dataset_loaders, f'load_{graph_name}')()
            except Exception as e:
                print(f'''failed to load \033[31m{graph_name}\033[0m: {e}''')
                return
            if not isinstance(g, (nx.Graph, nx.DiGraph)):
                g = eg2nx(g)
            print(
                f'sampling {graph_name} with {info["nodes"]} nodes and {info["edges"]} edges'
            )
            print('before: ')
            print(info)
            print('relabeling...')
            g = nx.convert_node_labels_to_integers(g)

            new_graph = sampler.sample(g)
            print(f'sampled {graph_name}')
            print('after: ')
            print(get_graph_info(new_graph))
            print(f'saving to {output_path}')
            nx.write_edgelist(new_graph, output_path)
    else:
        print(f"Graph '{graph_name}' not found in the graph_info_json file.")


if __name__ == '__main__':
    main()
