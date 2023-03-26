#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-23
Purpose: Get graph info
"""

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import networkx as nx

import argparse
from config import (
    dataset_names,
    random_erdos_renyi_dataset_names,
    graph_info_json_path,
    sampled_graph_dataset_names,
    random_erdos_renyi_graphs_load_function_names_date_s,
    edgelist_filenames_lcc,
)
from pathlib import Path
import json


def get_fully_qualified_type_name(o) -> str:
    klass = o.__class__
    module = klass.__module__
    if module == 'builtins':
        return klass.__qualname__  # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__


def get_graph_info(g) -> dict:
    import easygraph as eg
    import networkx as nx

    d = {}
    d['nodes'] = len(g.nodes)
    d['edges'] = len(g.edges)
    d['is_directed'] = g.is_directed()
    type_name = get_fully_qualified_type_name(g)
    d['average_degree'] = d['edges'] / d['nodes'] * 2
    d['density'] = (
        eg.density(g) if type_name.startswith('easygraph.') else nx.density(g)
    )
    d['type'] = type_name
    return d

# def get_nx_lcc_graph_info(g: 'nx.Graph') -> dict:
#     import easygraph as eg
#     import networkx as nx

#     d = {}
#     d['nodes'] = len(g.nodes)
#     d['edges'] = len(g.edges)
#     d['is_directed'] = g.is_directed()
#     type_name = get_fully_qualified_type_name(g)
#     d['average_degree'] = d['edges'] / d['nodes'] * 2
#     d['density'] = (
#         nx.density(g)
#     )
#     d['type'] = type_name
#     return d


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Get graph info',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '--remove-er-info-where-dataset-not-present',
        action='store_true',
        help='Remove ER info where dataset not present in dataset/',
    )

    parser.add_argument(
        '-t',
        '--test',
        action='store_true',
        help='Do a test run, only get graph info of the stub datasets',
    )

    parser.add_argument(
        '--stdout', action='store_true', help='Print the graph info to stdout'
    )

    # parser.add_argument(
    #     '-u', '--update', action='store_true', help='Update the graph info for specified dataset only'
    # )

    parser.add_argument(
        '-d',
        '--dataset',
        nargs='+',
        help='Specify the dataset to update',
        type=str,
        choices=dataset_names + random_erdos_renyi_dataset_names,
    )

    parser.add_argument(
        '--all-er',
        help='Update all random erdos renyi datasets, overrides --dataset',
        action='store_true',
    )

    parser.add_argument(
        '--all-sampled',
        help='Update all sampled datasets, overrides --dataset',
        action='store_true',
    )

    parser.add_argument(
        '--er-paper', help='Update ER datasets for paper', action='store_true'
    )

    parser.add_argument(
        '--edgelist-filenames-lcc', help='Update datasets in config.edgelist_filenames_lcc', action='store_true'
    )

    return parser.parse_args()


def main() -> None:
    args = get_args()
    if args.all_sampled:
        import dataset_loaders_sampled

        gi_d = json.loads(graph_info_json_path.read_text())
        for sampled_graph_dataset_name in sampled_graph_dataset_names:
            gi_d[f'{sampled_graph_dataset_name}_sampled'] = get_graph_info(
                getattr(dataset_loaders_sampled, f'load_{sampled_graph_dataset_name}')()
            )
        graph_info_json_path.write_text(json.dumps(gi_d, indent=4))
        return
    if args.remove_er_info_where_dataset_not_present:
        gi_d = json.loads(graph_info_json_path.read_text())
        for dataset in gi_d.copy().keys():
            if (
                dataset.startswith('er_')
                and not Path(
                    f'dataset/random-erdos-renyi/{dataset.removeprefix("er_")}.edgelist'
                ).exists()
            ):
                del gi_d[dataset]
        graph_info_json_path.write_text(json.dumps(gi_d, indent=4))
        return

    import dataset_loaders

    if (
        ((datasets_to_update := args.dataset) is None)
        and (not args.all_er)
        and (not args.er_paper)
        and (not args.edgelist_filenames_lcc)
    ):
        info_dict = {}
        for dataset_name in dataset_names + random_erdos_renyi_dataset_names:
            if not args.test and dataset_name.startswith('stub'):
                continue
            if args.test and not dataset_name.startswith('stub'):
                continue
            load_func_name = f'load_{dataset_name}'
            load_func = getattr(dataset_loaders, load_func_name)
            g = load_func()
            info = get_graph_info(g)
            info_dict[dataset_name] = info

        content = json.dumps(info_dict, indent=4)
        if args.stdout:
            print(content)
            return
        graph_info_json_path.write_text(content)
    else:
        gi = graph_info_json_path
        info_dict = json.loads(gi.read_text())
        if args.all_er:
            datasets_to_update = random_erdos_renyi_dataset_names
        if args.er_paper:
            datasets_to_update = [
                load_func_name.removeprefix('load_')
                for load_func_name in random_erdos_renyi_graphs_load_function_names_date_s
            ]
        if args.edgelist_filenames_lcc:
            import networkx as nx
            for lcc_path in edgelist_filenames_lcc:
                g = nx.read_edgelist(lcc_path, delimiter="\t", nodetype=int, create_using=nx.Graph())
                info = get_graph_info(g)
                info_dict[lcc_path] = info
            content = json.dumps(info_dict, indent=4)
            if args.stdout:
                print(content)
                return
            graph_info_json_path.write_text(content)
            return
        for dataset_name in datasets_to_update:
            if not args.test and dataset_name.startswith('stub'):
                continue
            if args.test and not dataset_name.startswith('stub'):
                continue
            load_func_name = f'load_{dataset_name}'
            load_func = getattr(dataset_loaders, load_func_name)
            g = load_func()
            info = get_graph_info(g)
            info_dict[dataset_name] = info

        content = json.dumps(info_dict, indent=4)
        if args.stdout:
            print(content)
            return
        graph_info_json_path.write_text(content)


if __name__ == '__main__':
    main()
