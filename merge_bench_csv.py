#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-05
Purpose: Why not?
"""

import argparse
from pathlib import Path
from typing import Iterator, KeysView
from config import BENCH_CSV_DIR, tool_name_mapping
import csv
from io import StringIO


def get_dataset_name_to_path_mapping_from_csv_dir(
    csv_dir: Path,
) -> Iterator[tuple[str, Path]]:
    for csv_path in csv_dir.rglob('*.csv'):
        file_name = csv_path.name
        dataset_name = file_name.split()[0].split('.')[0]
        yield dataset_name, csv_path


def add_dataset_name_column_to_csv(
    dataset_name: str, csv_path: Path
) -> tuple[str, KeysView]:
    r = csv.DictReader(csv_path.read_text().splitlines())
    rows_with_dataset_name = [{'dataset': dataset_name} | x for x in r]
    for row in rows_with_dataset_name:
        row['tool'] = tool_name_mapping[row['tool']]
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
        get_dataset_name_to_path_mapping_from_csv_dir(args.csv_dir)
    ):
        csv_s, h = add_dataset_name_column_to_csv(d, p)
        if n == 0:
            csv_s_l.append(','.join(h) + '\n')
        csv_s_l.append(csv_s)
    if args.outfile is not None:
        args.outfile.read_text(''.join(csv_s_l))
    else:
        print(''.join(csv_s_l))


if __name__ == '__main__':
    main()
