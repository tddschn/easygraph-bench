#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-03
Purpose: EasyGraph & NetworkX side-by-side benchmarking
"""

from hr_tddschn import hr

from config import (
    eg_master_dir,
    load_functions_name,
    di_load_functions_name,
    clustering_methods,
    shortest_path_methods,
    # connected_components_methods,
    connected_components_methods_G,
    connected_components_methods_G_node,
    mst_methods,
    other_methods,
    method_groups,
    dataset_names,
)
from utils import nx2eg, eg2ceg, get_first_node, eval_method


import easygraph as eg
import networkx as nx
from dataset_loaders import load_bio, load_cheminformatics, load_eco, load_soc, load_pgp, load_pgp_undirected  # type: ignore

load_func_name = 'load_pgp'
G_nx = load_pgp()
G_eg = nx2eg(G_nx)
G_ceg = eg2ceg(G_eg)
first_node_eg = get_first_node(G_eg)
first_node_nx = get_first_node(G_nx)
first_node_ceg = get_first_node(G_ceg)

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='EasyGraph & NetworkX side-by-side benchmarking',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # parser.add_argument(
    #     '-d',
    #     '--dataset',
    #     type=str,
    #     choices=dataset_names,
    #     nargs='+',
    # )

    parser.add_argument(
        '-G', '--method-group', type=str, choices=method_groups, nargs='+'
    )

    parser.add_argument(
        '-C',
        '--skip-cpp-easygraph',
        '--skip-ceg',
        action='store_true',
        help='Skip benchmarking cpp_easygraph methods',
    )

    # parser.add_argument('-n', '--dry-run', action='store_true', help='Dry run')

    return parser.parse_args()


args = get_args()


def main(args):
    method_groups = args.method_group
    flags = {}
    flags |= {'skip_ceg': args.skip_cpp_easygraph}
    cost_dict = {}
    first_node_args = {
        'call_method_args_eg': ['first_node_eg'],
        'call_method_args_nx': ['first_node_nx'],
        'call_method_args_ceg': ['first_node_ceg'],
    }
    if method_groups is None or 'clustering' in method_groups:
        # bench: clustering
        for method_name in clustering_methods:
            eval_method(
                cost_dict,
                load_func_name,
                method_name,
                **flags,
            )

    if method_groups is None or 'shortest-path' in method_groups:
        # bench: shortest path
        # bench_shortest_path(cost_dict, g, load_func_name)
        eval_method(
            cost_dict,
            load_func_name,
            ('Dijkstra', 'single_source_dijkstra_path'),
            **first_node_args,
            **flags,
        )
    if method_groups is None or 'connected-components' in method_groups:
        # bench: connected components
        for method_name in connected_components_methods_G:
            eval_method(
                cost_dict,
                load_func_name,
                method_name,
                **flags,
            )
        for method_name in connected_components_methods_G_node:
            eval_method(
                cost_dict,
                load_func_name,
                method_name,
                **first_node_args,
                **flags,
            )
    if method_groups is None or 'mst' in method_groups:
        # bench: mst
        for method_name in mst_methods:
            eval_method(
                cost_dict,
                load_func_name,
                method_name,
                # **flags,
                **(flags | {'skip_ceg': True}),
            )

    if method_groups is None or 'other' in method_groups:
        # bench: other
        for method_name in other_methods:
            eval_method(
                cost_dict,
                load_func_name,
                method_name,
                **flags,
            )

    print()


if __name__ == "__main__":
    main(args)
