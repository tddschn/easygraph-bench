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
    method_groups,
    dataset_names,
)

if eg_master_dir.exists():
    import sys

    sys.path.insert(0, str(eg_master_dir))

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='EasyGraph & NetworkX side-by-side benchmarking',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-d',
        '--dataset',
        type=str,
        choices=dataset_names,
        nargs='+',
    )

    parser.add_argument(
        '-G', '--method-group', type=str, choices=method_groups, nargs='+'
    )

    parser.add_argument('-n', '--dry-run', action='store_true', help='Dry run')

    return parser.parse_args()


def main():
    args = get_args()
    from dataset_loaders import load_bio, load_cheminformatics, load_eco, load_soc  # type: ignore
    from utils import eval_method, eg2nx, get_first_node, eg2ceg

    method_groups = args.method_group
    flags = {}
    flags |= {'dry_run': args.dry_run}
    datasets = args.dataset
    # use_datasets = dataset_names if datasets is None else datasets
    load_func_names = (
        load_functions_name if datasets is None else [f'load_{x}' for x in datasets]
    )
    # load datasets
    for load_func_name in load_func_names:
        cost_dict = dict()
        hr('=')
        print(f'loading dataset {load_func_name.removeprefix("load_")} ...')
        if args.dry_run:
            import easygraph as eg

            eg_graph: eg.Graph = eg.complete_graph(2)  # type: ignore
        else:
            eg_graph = eval(load_func_name)()
        nx_graph = eg2nx(eg_graph)
        ceg_graph = eg2ceg(eg_graph)
        first_node_eg = get_first_node(eg_graph)
        first_node_nx = get_first_node(nx_graph)
        first_node_ceg = get_first_node(ceg_graph)
        if method_groups is None or 'clustering' in method_groups:
            # bench: clustering
            for method_name in clustering_methods:
                eval_method(
                    cost_dict,
                    eg_graph,
                    nx_graph,
                    ceg_graph,
                    load_func_name,
                    method_name,
                    **flags,
                )

        if method_groups is None or 'shortest-path' in method_groups:
            # bench: shortest path
            # bench_shortest_path(cost_dict, g, load_func_name)
            eval_method(
                cost_dict,
                eg_graph,
                nx_graph,
                ceg_graph,
                load_func_name,
                ('Dijkstra', 'single_source_dijkstra_path'),
                call_method_args_eg=[first_node_eg],
                call_method_args_nx=[first_node_nx],
                **flags,
            )
        if method_groups is None or 'connected-components' in method_groups:
            # bench: connected components
            for method_name in connected_components_methods_G:
                eval_method(
                    cost_dict,
                    eg_graph,
                    nx_graph,
                    ceg_graph,
                    load_func_name,
                    method_name,
                    **flags,
                )
            for method_name in connected_components_methods_G_node:
                eval_method(
                    cost_dict,
                    eg_graph,
                    nx_graph,
                    ceg_graph,
                    load_func_name,
                    method_name,
                    call_method_args_eg=[first_node_eg],
                    call_method_args_nx=[first_node_nx],
                    **flags,
                )
        if method_groups is None or 'mst' in method_groups:
            # bench: mst
            for method_name in mst_methods:
                eval_method(
                    cost_dict, eg_graph, nx_graph, load_func_name, method_name, **flags
                )
        print()


if __name__ == "__main__":
    main()
