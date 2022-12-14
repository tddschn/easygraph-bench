#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-20
Purpose: Why not?
"""

import argparse
from itertools import takewhile
import json
from pathlib import Path
from tempfile import mkstemp
from tomark import Tomark
from config import dataset_homepage_mapping

BEGIN_MARKER = '<!-- BEGIN DATASET TABLE -->'
END_MARKER = '<!-- END DATASET TABLE -->'


def get_markdown_content() -> str:
    json_path = Path('./graph_info.json')
    graph_info_d = json.loads(json_path.read_text())
    data: list[dict[str, str | int | bool]] = []
    for graph_name, graph_info in graph_info_d.items():
        if graph_name.startswith('stub'):
            continue
        if graph_name in dataset_homepage_mapping:
            homepage = dataset_homepage_mapping[graph_name]
            data.append({'Dataset Name': f'[{graph_name}]({homepage})', **graph_info})
        else:
            data.append({'Dataset Name': graph_name, **graph_info})

    sorted_data = sorted(data, key=lambda x: ((n := x['Dataset Name']).startswith('er_') or n.startswith('[er_'), x['nodes'], 'sampled' in n, n.endswith('_directed')))  # type: ignore
    # from icecream import ic

    # ic(sorted_data)
    markdown = Tomark.table(sorted_data)  # type: ignore
    return markdown


def update_content_between_markers_for_file(
    file_path: Path, begin_marker: str, end_marker: str, new_content: str, new_file
) -> None:
    with open(file_path) as f:
        lines_before = list(takewhile(lambda line: begin_marker not in line, f))
        list(takewhile(lambda line: end_marker not in line, f))
        next(f)
        lines_after = f
        with open(new_file, 'w') as f_new:
            f_new.writelines(lines_before)
            f_new.write(f'\n{begin_marker}\n')
            f_new.write(f'\n{new_content}\n')
            f_new.write(f'\n{end_marker}\n')
            f_new.writelines(lines_after)


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?', formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-u',
        '--update-readme',
        help='Update the dataset table in the README.md',
        action='store_true',
    )

    parser.add_argument(
        '-P',
        '--no-print',
        help='Do not print the markdown content',
        action='store_true',
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    markdown_content = get_markdown_content()
    if not args.no_print:
        print(markdown_content)

    if args.update_readme:
        temp_file = Path(mkstemp()[1])
        readme = Path(__file__).parent / 'README.md'
        update_content_between_markers_for_file(
            readme, BEGIN_MARKER, END_MARKER, markdown_content, temp_file
        )

        temp_file.rename(readme)


if __name__ == '__main__':
    main()
