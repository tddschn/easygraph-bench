#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-10-30
Purpose: Generate ER random graph datasets
"""

import argparse
from pathlib import Path


# n_nodes = [200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
n_nodes = [200, 500, 1000, 2000, 5000, 10000]


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
        '-p', help='Probability of edge', metavar='float', type=float, default=0.05
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()

    import easygraph as eg

    er = eg.erdos_renyi_P

    num_nodes = args.nodes if args.nodes != n_nodes else n_nodes

    Path('dataset/random-erdos-renyi').mkdir(parents=True, exist_ok=True)
    total_graph_count = len(num_nodes) * 2
    idx = 1
    for num in num_nodes:
        for directed in (True, False):
            filepath = f'dataset/random-erdos-renyi/{num}{"_directed" if directed else ""}.edgelist'
            print(
                f'Generating {filepath} ({"directed" if directed else "undirected"}) {idx} / {total_graph_count}...'
            )
            er(num, args.p, directed, filepath)


if __name__ == '__main__':
    main()
