#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-03
Purpose: EasyGraph & NetworkX side-by-side benchmarking
"""

import sys

from config import (
    eg_master_dir,
    load_functions_name,
    di_load_functions_name,
    clustering_methods,
    shortest_path_methods,
    method_groups,
)

sys.path.insert(0, str(eg_master_dir))

from dataset_loaders import *
from utils import eval_method, eg2nx, get_first_node
import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='EasyGraph & NetworkX side-by-side benchmarking',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-G', '--method-group', type=str, choices=method_groups, nargs='+'
    )

    return parser.parse_args()


def main():
    args = get_args()
    method_groups = args.method_group
    # load datasets
    for load_func_name in load_functions_name:
        cost_dict = dict()
        print(f'loading dataset with {load_func_name} ...')
        eg_graph = eval(load_func_name)()
        nx_graph = eg2nx(eg_graph)
        first_node_eg = get_first_node(eg_graph)
        first_node_nx = get_first_node(nx_graph)
        if 'clustering' in method_groups or method_groups is None:
            # bench: clustering
            for method_name in clustering_methods:
                eval_method(cost_dict, eg_graph, nx_graph, load_func_name, method_name)

        if 'shortest-path' in method_groups or method_groups is None:
            # bench: shortest path
            # bench_shortest_path(cost_dict, g, load_func_name)
            eval_method(
                cost_dict,
                eg_graph,
                nx_graph,
                load_func_name,
                ('Dijkstra', 'single_source_dijkstra_path'),
                call_method_args_eg=[first_node_eg],
                call_method_args_nx=[first_node_nx],
            )


if __name__ == "__main__":
    main()
