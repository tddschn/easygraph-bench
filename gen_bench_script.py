#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-21
Purpose: generate bench scripts from jinja template
"""

import argparse
from jinja2 import FileSystemLoader, Environment, Template
from pathlib import Path
from config import dataset_names
from stat import S_IEXEC


def gen_bench_script(dataset_name: str, template: Template) -> str:
    load_func_name = f'load_{dataset_name}'
    return template.render(load_func_name=load_func_name)


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='generate bench scripts from jinja template',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '-d',
        '--dataset',
        type=str,
        choices=dataset_names,
        nargs='+',
        default=dataset_names,
    )

    parser.add_argument('-o', '--output', type=Path, help='output file')
    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    e = Environment(loader=FileSystemLoader('templates'))
    # Load the Jinja2 template.
    template = e.get_template('bench_template.jinja.py')
    if args.output is not None and len(args.dataset) == 1:
        dataset_name = args.dataset[0]
        script_content = gen_bench_script(dataset_name, template=template)
        output_path = args.output
        output_path.write_text(script_content)
        output_path.chmod(output_path.stat().st_mode | S_IEXEC)
        print(f'Benchmark script for {dataset_name} is generated at {output_path}')
    else:
        # ignores -o if dataset > 1
        for dataset_name in args.dataset:
            script_content = gen_bench_script(dataset_name, template=template)
            output_path = Path(f'bench_{dataset_name}.py')
            output_path.write_text(script_content)
            output_path.chmod(output_path.stat().st_mode | S_IEXEC)
            print(f'Benchmark script for {dataset_name} is generated at {output_path}')


if __name__ == '__main__':
    main()