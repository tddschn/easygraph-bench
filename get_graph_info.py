#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-23
Purpose: Why not?
"""

import argparse
from config import dataset_names
import dataset_loaders
from pathlib import Path
import json


def get_fully_qualified_type_name(o) -> str:
    klass = o.__class__
    module = klass.__module__
    if module == 'builtins':
        return klass.__qualname__  # avoid outputs like 'builtins.str'
    return module + '.' + klass.__qualname__


def get_graph_info(g):
    d = {}
    d['nodes'] = len(g.nodes)
    d['edges'] = len(g.edges)
    d['type'] = get_fully_qualified_type_name(g)
    d['is_directed'] = g.is_directed()
    return d


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?', formatter_class=argparse.ArgumentDefaultsHelpFormatter
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

    return parser.parse_args()


def main() -> None:
    args = get_args()
    info_dict = {}
    for dataset_name in dataset_names:
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
    graph_info_path = Path(__file__).parent / "graph_info.json"
    graph_info_path.write_text(content)


if __name__ == '__main__':
    main()
