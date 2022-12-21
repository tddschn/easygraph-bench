#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-21
Purpose: generate bench scripts from jinja template
"""

import argparse
from datetime import date
from jinja2 import FileSystemLoader, Environment, Template
from pathlib import Path
from config import (
    er_dataset_names_for_paper_20221213,
    er_dataset_edges_count_for_paper_20221213,
)
from stat import S_IEXEC
from utils_other import autorange_count_generator

# ENTRYPOINT_SH_PATH = Path(__file__).parent / 'entrypoint.sh'
# ENTRYPOINT_SH_PAPER_PATH = Path(__file__).parent / 'entrypoint_paper.sh'
# # cSpell:disable
# ENTRYPOINT_SH_M_PATH = Path(__file__).parent / 'mentrypoint.sh'
# ENTRYPOINT_SH_M_PAPER_PATH = Path(__file__).parent / 'mentrypoint_paper.sh'
# # cSpell:enable
# ENTRYPOINT_SH_ER_PATH = Path(__file__).parent / 'entrypoint_er.sh'


def gen_gen_er_paper(
    nodes_and_edges_list: list[dict[str, str]],
    date_s: str,
    extra_args: str,
    template: Template,
) -> str:
    return template.render(
        nodes_and_edges_list=nodes_and_edges_list, date_s=date_s, extra_args=extra_args
    )


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='generate bench scripts from jinja template',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '--date-string',
        help='Date string',
        metavar='str',
        type=str,
        # today's date in YYYYMMDD
        default=date.today().strftime('%Y%m%d'),
    )

    # parser.add_argument(
    #     '--sparse',
    #     help='Generate sparse graphs with nx.fast_gnp_random_graph()',
    #     action='store_true',
    # )

    parser.add_argument(
        '--extra-args', help='Extra arguments', metavar='str', type=str, default=''
    )

    parser.add_argument(
        '--experiment-20221221',
        help='Generate scripts for experiment 20221221',
        action='store_true',
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    # extra_args = ''
    # if args.sparse:
    #     extra_args += ' --sparse'
    e = Environment(loader=FileSystemLoader('templates'))
    # Load the Jinja2 template.
    template = e.get_template('gen-er-paper.jinja.sh')
    nodes_and_edges_list = []
    if args.experiment_20221221:
        for nodes in (10_000, 100_000, 1_000_000):
            for edges in autorange_count_generator(nodes):
                if edges <= 5 * nodes:
                    nodes_and_edges_list.append({'nodes': nodes, 'edges': edges})
    else:
        for i, dataset_name in enumerate(er_dataset_names_for_paper_20221213):
            nodes_and_edges_list.append(
                {
                    'nodes': dataset_name.split('_')[1],
                    'edges': str(er_dataset_edges_count_for_paper_20221213[i]),
                }
            )

    script_content = gen_gen_er_paper(
        date_s=args.date_string,
        nodes_and_edges_list=nodes_and_edges_list,
        extra_args=args.extra_args,
        template=template,
    )
    output_path = Path(f'gen-er-paper-{args.date_string}.sh')
    output_path.write_text(script_content)
    output_path.chmod(output_path.stat().st_mode | S_IEXEC)
    print(f'gen-er-paper script for {args.date_string} is generated at {output_path}')


if __name__ == '__main__':
    main()
