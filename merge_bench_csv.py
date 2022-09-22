#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-05
Purpose: Why not?
"""

import argparse
from pathlib import Path
from collections.abc import Iterator, KeysView
from config import BENCH_CSV_DIR, tool_name_mapping, dataset_name_mapping, drop_methods
from utils_other import get_dataset_list_sorted_by_nodes_and_edges
import csv
from io import StringIO


def get_dataset_name_to_path_mapping_from_csv_dir(
    csv_dir: Path,
) -> Iterator[tuple[str, Path]]:
    for csv_path in csv_dir.rglob('*.csv'):
        file_name = csv_path.name
        dataset_name = file_name.split()[0].split('.')[0]
        yield dataset_name, csv_path


def get_dataset_name_to_path_mapping_from_csv_dir_sorted_by_nodes_and_edges(
    csv_dir: Path,
) -> list[tuple[str, Path]]:
    def get_index(dataset_name: str) -> int:
        return (
            get_dataset_list_sorted_by_nodes_and_edges().index(dataset_name)
            if dataset_name in get_dataset_list_sorted_by_nodes_and_edges()
            else 1000000
        )

    return sorted(
        get_dataset_name_to_path_mapping_from_csv_dir(csv_dir),
        key=lambda x: get_index(x[0]),
    )


def add_dataset_name_column_to_csv(
    dataset_name: str,
    csv_path: Path,
    remove_records_with_negative_avg_time: bool = True,
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
    rows_to_write = filter(
        lambda x: x['method'] not in drop_methods, rows_with_dataset_name
    )
    if remove_records_with_negative_avg_time:
        rows_to_write = filter(lambda x: float(x['avg time']) > 0, rows_to_write)
    w.writerows(rows_to_write)
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
        '-M',
        '--drop-method',
        help='Do not write lines with this method',
        nargs='*',
        # default=[],
        default=drop_methods,
    )

    parser.add_argument(
        '-N',
        '--remove-records-with-negative-avg-time',
        help='Remove records with negative avg time',
        action='store_true',
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
        get_dataset_name_to_path_mapping_from_csv_dir_sorted_by_nodes_and_edges(
            csv_dir=args.csv_dir
        )
    ):
        csv_s, h = add_dataset_name_column_to_csv(
            d,
            p,
            remove_records_with_negative_avg_time=args.remove_records_with_negative_avg_time,
        )
        if n == 0:
            # write csv header
            csv_s_l.append(','.join(h) + '\n')
        csv_s_l.append(csv_s)
    csv_content = ''.join(csv_s_l).strip()
    if args.outfile is not None:
        args.outfile.write_text(csv_content)
    else:
        print(csv_content)


if __name__ == '__main__':
    main()
