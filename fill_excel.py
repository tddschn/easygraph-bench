#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-09-23
Purpose: Fill Min Gao's bench results template Excel file
"""

import argparse
from pathlib import Path
from config import (
    tool_name_mapping,
    dataset_homepage_mapping,
    bench_results_table_name,
    graph_info_table_name,
)
import openpyxl
from openpyxl.cell.cell import Cell, MergedCell
from openpyxl.worksheet.worksheet import Worksheet
from utils_db import get_graph_property_to_excel_field_mapping
import sqlite3
from copy import copy

bench_results_sqlite_db_path = Path(__file__).parent / 'bench-results.db'
template_workbook_path = (
    '/Users/tscp/Downloads/easygraph-benchmark-results-template.xlsx'
)
new_workbook_path = '/Users/tscp/Downloads/easygraph-benchmark-results.xlsx'

dataset_name_col = 'A'
tool_col = 'A'
# cSpell:disable
avg_time_cols = list('BCDEF')
graph_property_cols = list('GHIJK')
# cSpell:enable


def copy_cell_style(cell: Cell) -> dict:
    return {
        'font': copy(cell.font),
        'border': copy(cell.border),
        'fill': copy(cell.fill),
        'number_format': copy(cell.number_format),
        'protection': copy(cell.protection),
        'alignment': copy(cell.alignment),
    }


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Fill Min Gao\'s bench results template Excel file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-t',
        '--template-file',
        help='Template Excel file',
        metavar='PATH',
        type=str,
        default=template_workbook_path,
    )

    parser.add_argument(
        '-o',
        '--output-file',
        help='Output Excel file',
        metavar='PATH',
        type=str,
        default=new_workbook_path,
    )

    parser.add_argument(
        '-G', '--fill-graph-info-only', help='Fill graph info only', action='store_true'
    )

    return parser.parse_args()


def get_dataset_name_to_row_number_mapping(worksheet: Worksheet) -> dict[str, int]:
    rd = worksheet.row_dimensions
    max_row = len(rd)
    row_range = range(1, max_row + 1, 5)
    dataset_name_to_row_number_mapping: dict[str, int] = {
        worksheet[f'{dataset_name_col}{str(row_number)}'].value: row_number
        for row_number in row_range
    }
    return dataset_name_to_row_number_mapping


def query_average_time(
    cursor: sqlite3.Cursor, database_name: str, tool_abbr: str, method: str
) -> float:
    query = f"""
    SELECT "average_time" FROM "{bench_results_table_name}" WHERE "dataset" = :dataset AND "tool" = :tool_abbr and "method" = :method ORDER BY "iteration_count" DESC, "id" DESC LIMIT 1
    """
    cursor.execute(
        query, {'dataset': database_name, 'tool_abbr': tool_abbr, 'method': method}
    )
    try:
        return float(cursor.fetchone()[0])
    except:
        print(
            f'No result for {database_name}, {tool_abbr}, {method}, filled with -100.0 .'
        )
        # raise
        return -100.0


def main() -> None:
    args = get_args()
    workbook = openpyxl.load_workbook(args.template_file)
    print(f'Loaded template file: {args.template_file}')
    worksheet = workbook.active
    dataset_name_to_row_number_mapping = get_dataset_name_to_row_number_mapping(
        worksheet=worksheet
    )
    with sqlite3.connect(bench_results_sqlite_db_path) as conn:
        cursor = conn.cursor()
        for dataset_name, row_number in dataset_name_to_row_number_mapping.items():
            # add hyperlinks to the dataset name cells
            if (
                dataset_name in dataset_homepage_mapping
                and not args.fill_graph_info_only
            ):
                dataset_homepage = dataset_homepage_mapping[dataset_name]
                cell = worksheet[f'{dataset_name_col}{str(row_number)}']
                dataset_name_cell_styles = copy_cell_style(cell)
                cell.hyperlink = dataset_homepage
                cell.value = dataset_name
                cell.style = 'Hyperlink'
                for k, v in dataset_name_cell_styles.items():
                    setattr(cell, k, v)

            # fill cells
            for i, rn in enumerate(range(row_number + 1, row_number + 4)):
                # fill avg times
                for cn in avg_time_cols:
                    if args.fill_graph_info_only:
                        continue
                    cell = worksheet[f'{cn}{str(rn)}']
                    if isinstance(cell, MergedCell) or cell.value == 'N/A':
                        # print(f'skipped cell {cell}')
                        continue
                    tool = worksheet[f'{tool_col}{str(rn)}'].value
                    tool_abbr = tool_name_mapping[tool]
                    method = worksheet[f'{cn}{str(row_number)}'].value
                    cell.value = query_average_time(
                        cursor, dataset_name, tool_abbr, method
                    )
                    for k, v in copy_cell_style(worksheet['L2']).items():
                        setattr(cell, k, v)
                # fill graph properties
                if i == 0:
                    graph_property_to_excel_field_mapping = (
                        get_graph_property_to_excel_field_mapping()
                    )
                    excel_field_to_graph_property_mapping = {
                        v: k for k, v in graph_property_to_excel_field_mapping.items()
                    }
                    for cn in graph_property_cols:
                        cell = worksheet[f'{cn}{str(rn)}']
                        # if not isinstance(cell, MergedCell):
                        #     print(f'skipped cell {cell}')
                        #     continue
                        excel_graph_property = worksheet[f'{cn}{str(row_number)}'].value
                        graph_property = excel_field_to_graph_property_mapping[
                            excel_graph_property
                        ]
                        query = f"""
                        SELECT "{graph_property}" FROM "{graph_info_table_name}" WHERE "dataset" = :dataset
                        """
                        cursor.execute(query, {'dataset': dataset_name})
                        cell.value = cursor.fetchone()[0]
                        # print(f'filled cell {cell} with {cell.value}')
                        for k, v in copy_cell_style(worksheet['L2']).items():
                            setattr(cell, k, v)
    workbook.save(args.output_file)
    print(f'Saved new file: {args.output_file}')


if __name__ == '__main__':
    main()
