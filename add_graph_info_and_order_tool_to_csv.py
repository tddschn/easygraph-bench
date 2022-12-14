#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-16
Purpose: Add graph info and order tool for an all.csv file
"""

import argparse
from io import StringIO
from pathlib import Path
import json
import csv
from typing import TypeVar
from collections.abc import Iterable
from utils_other import get_autorange_count
from config import (
    get_method_order,
    tool_order,
    dataset_name_mapping,
    dataset_homepage_mapping,
)


T = TypeVar('T')


def ordered_dedupe(seq: Iterable[T]) -> list[T]:
    # https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def add_graph_info_and_order_tool_to_csv(
    csv_path: Path,
    tool_order: list[str] = tool_order,
    add_graph_info: bool = True,
    expand_dataset_name: bool = False,
    add_autorange_iteration_count: bool = False,
) -> list[dict]:
    r = csv.DictReader(csv_path.read_text().splitlines())

    rows = list(r)

    # expand dataset names
    dataset_name_mapping_reversed = {v: k for k, v in dataset_name_mapping.items()}
    for row in rows:
        if row['dataset'] in dataset_name_mapping_reversed:
            row['dataset'] = dataset_name_mapping_reversed[row['dataset']]

    # add graph info
    if add_graph_info:
        gi = Path(__file__).parent / 'graph_info.json'
        gi_d = json.loads(gi.read_text())

        for row in rows:
            if row['dataset'] in gi_d:
                row |= gi_d[row['dataset']]
            if row['dataset'] in dataset_homepage_mapping:
                row['dataset_homepage'] = dataset_homepage_mapping[row['dataset']]

    # add autorange iteration count
    if add_autorange_iteration_count:
        for row in rows:
            row['iteration count'] = get_autorange_count(float(row['avg time']))

    # order the records
    method_order = get_method_order()
    dataset_order = ordered_dedupe([x['dataset'] for x in rows])

    rows_sorted = sorted(
        filter(lambda x: not x['dataset'].startswith('stub'), rows),
        key=(
            lambda row: (
                dataset_order.index(row['dataset']),
                method_order.index(row['method'])
                if row['method'] in method_order
                else 999,
                tool_order.index(row['tool']),
            )
        ),
    )
    # revert to abbreviated dataset names
    if not expand_dataset_name:
        for row in rows_sorted:
            if row['dataset'] in dataset_name_mapping:
                row['dataset'] = dataset_name_mapping[row['dataset']]
    return rows_sorted


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add graph info and order tool for an all.csv file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'all_csv_path',
        metavar='CSV PATH',
        help='Path to the all.csv file generated by merge_bench_csv.py',
        type=Path,
    )

    parser.add_argument(
        '-A',
        '--no-add-graph-info',
        help='Do not add graph info to the outputted csv',
        action='store_false',
    )

    parser.add_argument(
        '-a',
        '--abbreviated-dataset-names',
        help='Use abbreviated dataset names',
        action='store_true',
    )

    parser.add_argument(
        '-c',
        '--autorange-iteration-count',
        help='Add autorange iteration count',
        action='store_true',
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    all_csv_path = args.all_csv_path
    new_rows = add_graph_info_and_order_tool_to_csv(
        all_csv_path,
        add_graph_info=args.no_add_graph_info,
        expand_dataset_name=not args.abbreviated_dataset_names,
        add_autorange_iteration_count=args.autorange_iteration_count,
    )
    header = new_rows[0].keys()
    s = StringIO()
    w = csv.DictWriter(s, header)
    w.writeheader()
    w.writerows(new_rows)
    print(s.getvalue().strip())


if __name__ == '__main__':
    main()
