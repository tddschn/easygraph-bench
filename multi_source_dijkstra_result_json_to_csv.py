#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-03-21
Purpose: Why not?
"""

import argparse
from pathlib import Path

import csv
import json

datasets = [
    'enron.txt',
    'amazon.txt',
    'google.txt',
    'pokec.txt',
]


def convert_to_csv(datasets, avg_time, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['dataset', 'num_sources_nodes', 'avg_time'])
        for i, dataset in enumerate(datasets):
            for j, time in enumerate(avg_time[i]):
                num_sources = list(time.keys())[0]
                avg_time_val = time[num_sources]
                writer.writerow([dataset.split('.')[0], num_sources, avg_time_val])


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?', formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i',
        '--input',
        help='Input file, like multi_source_dijkstra_test_result.json',
        type=Path,
        default=Path('multi_source_dijkstra_test_result.json'),
    )
    parser.add_argument(
        '-o',
        '--output',
        help='Output file, like multi_source_dijkstra_test_result.csv',
        type=Path,
        default=Path('multi_source_dijkstra_test_result.csv'),
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    json_data = json.loads(args.input.read_text())
    convert_to_csv(datasets, json_data, args.output)
    print(f'Wrote to {args.output.resolve()}')


if __name__ == '__main__':
    main()
