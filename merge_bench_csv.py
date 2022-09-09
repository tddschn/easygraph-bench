#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-05
Purpose: Why not?
"""

import argparse
from pathlib import Path
from typing import Iterator, KeysView
from config import (
    BENCH_CSV_DIR,
    tool_name_mapping,
    dataset_name_mapping,
    graph_info_json_path,
)
from utils import get_dataset_list_sorted_by_nodes
import csv
from io import StringIO


def get_dataset_name_to_path_mapping_from_csv_dir(
    csv_dir: Path,
) -> Iterator[tuple[str, Path]]:
    for csv_path in csv_dir.rglob('*.csv'):
        file_name = csv_path.name
        dataset_name = file_name.split()[0].split('.')[0]
        yield dataset_name, csv_path


def get_dataset_name_to_path_mapping_from_csv_dir_sorted_by_nodes(
    csv_dir: Path,
) -> list[tuple[str, Path]]:
    def get_index(dataset_name: str) -> int:
        return (
            get_dataset_list_sorted_by_nodes().index(dataset_name)
            if dataset_name in get_dataset_list_sorted_by_nodes()
            else 1000000
        )

    return sorted(
        get_dataset_name_to_path_mapping_from_csv_dir(csv_dir),
        key=lambda x: get_index(x[0]),
    )


def add_dataset_name_column_to_csv(
    dataset_name: str, csv_path: Path
) -> tuple[str, KeysView[str]]:
    r = csv.DictReader(csv_path.read_text().splitlines())
    rows_with_dataset_name = [{'dataset': dataset_name} | x for x in r]
    for row in rows_with_dataset_name:
        row['tool'] = tool_name_mapping[row['tool']]
        if row['dataset'] in dataset_name_mapping:
            row['dataset'] = dataset_name_mapping[row['dataset']]
    s = StringIO()
    h = rows_with_dataset_name[0].keys()
    w = csv.DictWriter(s, rows_with_dataset_name[0].keys())
    # w.writeheader()
    w.writerows(rows_with_dataset_name)
    return s.getvalue(), h


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?', formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-c',
        '--csv-dir',
        help='Path to the bench result csv dir',
        type=Path,
        default=BENCH_CSV_DIR,
    )

    parser.add_argument(
        '-o' '--outfile', type=Path, dest='outfile', help='Path to the output file'
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    csv_s_l = []
    for n, (d, p) in enumerate(
        get_dataset_name_to_path_mapping_from_csv_dir_sorted_by_nodes(args.csv_dir)
    ):
        csv_s, h = add_dataset_name_column_to_csv(d, p)
        if n == 0:
            # write csv header
            csv_s_l.append(','.join(h) + '\n')
        csv_s_l.append(csv_s)
    if args.outfile is not None:
        args.outfile.read_text(''.join(csv_s_l))
    else:
        print(''.join(csv_s_l))


if __name__ == '__main__':
    main()