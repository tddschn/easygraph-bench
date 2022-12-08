#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-10-30
Purpose: Generate ER random graph datasets
"""

import argparse
from pathlib import Path
import sys


# n_nodes = [200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
# n_nodes = [200, 500, 1000, 2000, 5000, 10000]
# n_nodes = [500, 1000, 5000, 10000]

# 0.5k, 5k, 50k, 500k, 1000k
n_nodes = [500, 5000, 50000, 500000, 1000000]


# def get_p(num_nodes: int, edge_to_node_ratio: float | int = 5) -> float:
#     total_possible_edges = num_nodes * (num_nodes - 1) / 2
#     # ratio = tot * p / nodes
#     # p = ratio * nodes / tot
#     return edge_to_node_ratio * num_nodes / total_possible_edges


def get_p(num_nodes: int, edges_number: int) -> float:
    total_possible_edges = num_nodes * (num_nodes - 1) / 2
    # p = edges / total_possible_edges
    return edges_number / total_possible_edges


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generate ER random graph datasets',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-n',
        '--nodes',
        help='Number of nodes',
        metavar='INT',
        type=int,
        nargs='*',
        default=n_nodes,
    )
    parser.add_argument(
        '-p',
        help='Probability of edge, dynamically assign p if not specified',
        metavar='float',
        type=float,
    )

    # parser.add_argument(
    #     '-d', '--dynamic-p', help='Dynamically assign p values', action='store_true'
    # )

    parser.add_argument(
        '--directed', help='Also generate directed graphs', action='store_true'
    )

    return parser.parse_args()


# def main():
#     """Make a jazz noise here"""

#     args = get_args()

#     import easygraph as eg

#     er = eg.erdos_renyi_P

#     num_nodes = args.nodes if args.nodes != n_nodes else n_nodes

#     Path('dataset/random-erdos-renyi').mkdir(parents=True, exist_ok=True)
#     directed_option_list = [False] + ([True] if args.directed else [])
#     total_graph_count = len(num_nodes) * len(directed_option_list)
#     idx = 1
#     for num in num_nodes:
#         for directed in directed_option_list:
#             filepath = f'dataset/random-erdos-renyi/{num}{"_directed" if directed else ""}.edgelist'
#             print(
#                 f'Generating {filepath} ({"directed" if directed else "undirected"}) {idx} / {total_graph_count}...'
#             )
#             if args.p is not None:
#                 p = args.p
#             else:
#                 p = get_p(num)
#             er(num, p, directed, filepath)
#             idx += 1


def main():
    """Make a jazz noise here"""

    args = get_args()

    import easygraph as eg

    er = eg.erdos_renyi_P

    num_nodes = args.nodes if args.nodes != n_nodes else n_nodes

    Path('dataset/random-erdos-renyi').mkdir(parents=True, exist_ok=True)
    directed_option_list = [False] + ([True] if args.directed else [])
    total_graph_count = len(num_nodes) * len(directed_option_list)
    idx = 1
    for num in num_nodes:
        for directed in directed_option_list:
            filepath = f'dataset/random-erdos-renyi/{num}{"_directed" if directed else ""}.edgelist'
            print(
                f'Generating {filepath} ({"directed" if directed else "undirected"}) {idx} / {total_graph_count}...'
            )
            if args.p is not None:
                p = args.p
            elif args.edges_number is not None:
                # Use the specified number of edges to calculate p
                p = get_p(num, args.edges_number)
            else:
                # Use the default edge-to-node ratio to calculate p
                # p = get_p(num)
                sys.exit(f'Error: Either p or edges_number must be specified')
            er(num, p, directed, filepath)
            idx += 1


if __name__ == '__main__':
    main()
