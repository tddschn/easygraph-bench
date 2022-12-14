#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-08-21
Purpose: generate bench scripts from jinja template
"""

import argparse
import json
from jinja2 import FileSystemLoader, Environment, Template
from pathlib import Path
from config import (
    graph_info_json_path,
    dataset_names,
    bench_scripts_set,
    read_profile_preparation_code,
    graph_benchmark_code_ordereddict_yaml_path,
    edgelist_filenames,
    profile_tools_to_drop,
    random_erdos_renyi_dataset_names,
    dataset_names_for_paper_multiprocessing,
    er_dataset_names_for_paper_multiprocessing,
    random_erdos_renyi_graphs_load_function_names_date_s,
)
from stat import S_IEXEC

ENTRYPOINT_SH_PATH = Path(__file__).parent / 'entrypoint.sh'
ENTRYPOINT_SH_PAPER_PATH = Path(__file__).parent / 'entrypoint_paper.sh'
# cSpell:disable
ENTRYPOINT_SH_M_PATH = Path(__file__).parent / 'mentrypoint.sh'
ENTRYPOINT_SH_M_PAPER_PATH = Path(__file__).parent / 'mentrypoint_paper.sh'
# cSpell:enable
ENTRYPOINT_SH_ER_PATH = Path(__file__).parent / 'entrypoint_er.sh'


def gen_bench_script(dataset_name: str, template: Template) -> str:
    load_func_name = f'load_{dataset_name}'
    return template.render(load_func_name=load_func_name)


def gen_bench_script_entrypoint(script_set: str, template: Template) -> str:
    script_set_list = f'{script_set}'
    return template.render(script_set_list=script_set_list)


def gen_bench_script_entrypoint_bash(
    datasets: list[str],
    bash_arg: str,
    template: Template,
    multiprocessing: bool = False,
) -> str:
    script_body = '\n'.join(
        f'./{"m" if multiprocessing else ""}bench_{d}.py {bash_arg}' for d in datasets
    )
    return template.render(script_body=script_body)


def gen_profile_script(
    tool: str, method_to_code_mapping: dict[str, str], template: Template
) -> str:
    profile_preparation_code = read_profile_preparation_code()[tool]
    return template.render(
        tool=tool,
        profile_preparation_code=profile_preparation_code,
        graph_benchmark_code=method_to_code_mapping,
    )


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
        choices=dataset_names + random_erdos_renyi_dataset_names,
        nargs='+',
        default=dataset_names + random_erdos_renyi_dataset_names,
    )

    parser.add_argument(
        '-e',
        '--entrypoint',
        help='generate entry point scripts instead of individual ones',
        action='store_true',
    )

    parser.add_argument(
        '-E',
        '--entrypoint-bash',
        help='generate entry point script in bash',
        action='store_true',
    )

    parser.add_argument(
        '--entrypoint-bash-paper',
        help='generate entry point script in bash for the paper',
        action='store_true',
    )

    parser.add_argument(
        '-M',
        '--entrypoint-bash-multiprocessing',
        help='generate entry point script in bash for running multiprocessing bench scripts',
        action='store_true',
    )

    parser.add_argument(
        '--entrypoint-bash-multiprocessing-paper',
        help='generate entry point script in bash for running multiprocessing bench scripts (for paper)',
        action='store_true',
    )

    parser.add_argument(
        '--bash-arg',
        help='command line args for entrypoint.sh',
        type=str,
        default='"$@"',
    )

    parser.add_argument(
        '--entrypoint-bash-er',
        help='generate entry point scripts in bash (erdos-renyi)',
        action='store_true',
    )

    parser.add_argument(
        '--bash-arg-er',
        help='command line args for entrypoint_er.sh (erdos-renyi)',
        type=str,
        default='"$@"',
    )

    parser.add_argument(
        '-P', '--profile', help='generate profile scripts', action='store_true'
    )

    parser.add_argument(
        '-Z',
        '--profile-entrypoint',
        help='generate profile entrypoint scripts',
        action='store_true',
    )

    parser.add_argument('-m', '--multiprocessing-bench-scripts', action='store_true')
    parser.add_argument('--er-paper', action='store_true')
    # parser.add_argument(
    #     '--er-paper-date-string', type=str, default=date.today().strftime('%Y%m%d')
    # )

    parser.add_argument('-o', '--output', type=Path, help='output file')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    e = Environment(loader=FileSystemLoader('templates'))
    # Load the Jinja2 template.
    template = e.get_template('bench_template.jinja.py')
    template_m = e.get_template('multiprocessing_bench_template.jinja.py')
    template_entrypoint = e.get_template('entrypoint.jinja.py')
    template_entrypoint_bash = e.get_template('entrypoint.jinja.sh')
    template_profile_script = e.get_template('profile_template.jinja.py')
    if args.entrypoint:
        for script_set in bench_scripts_set:
            script_content = gen_bench_script_entrypoint(
                script_set, template=template_entrypoint
            )
            script_set_name = script_set.removeprefix('bench_scripts_')
            output_path = Path(f'entrypoint_{script_set_name}.py')
            output_path.write_text(script_content)
            output_path.chmod(output_path.stat().st_mode | S_IEXEC)
            print(
                f'Benchmark entrypoint script for {script_set_name} generated at {output_path}'
            )
        return

    if args.entrypoint_bash:
        script_content = gen_bench_script_entrypoint_bash(
            datasets=args.dataset,
            bash_arg=args.bash_arg,
            template=template_entrypoint_bash,
        )
        ENTRYPOINT_SH_PATH.write_text(script_content)
        ENTRYPOINT_SH_PATH.chmod(ENTRYPOINT_SH_PATH.stat().st_mode | S_IEXEC)
        print(f'Benchmark entrypoint shell script generated at {ENTRYPOINT_SH_PATH}')
        return

    if args.entrypoint_bash_paper:
        script_content = gen_bench_script_entrypoint_bash(
            datasets=list(
                filter(
                    lambda x: not x.startswith('stub'),
                    args.dataset + er_dataset_names_for_paper_multiprocessing,
                )
            ),
            bash_arg=f'{args.bash_arg}',
            template=template_entrypoint_bash,
        )
        ENTRYPOINT_SH_PAPER_PATH.write_text(script_content)
        ENTRYPOINT_SH_PAPER_PATH.chmod(
            ENTRYPOINT_SH_PAPER_PATH.stat().st_mode | S_IEXEC
        )
        print(
            f'Benchmark entrypoint shell script generated at {ENTRYPOINT_SH_PAPER_PATH}'
        )
        return

    if args.entrypoint_bash_multiprocessing:
        script_content = gen_bench_script_entrypoint_bash(
            datasets=args.dataset,
            bash_arg=args.bash_arg,
            template=template_entrypoint_bash,
            multiprocessing=True,
        )
        ENTRYPOINT_SH_M_PATH.write_text(script_content)
        ENTRYPOINT_SH_M_PATH.chmod(ENTRYPOINT_SH_M_PATH.stat().st_mode | S_IEXEC)
        # cSpell:disable
        print(
            f'Benchmark entrypoint shell script (for multiprocessing mbench_*.py) generated at {ENTRYPOINT_SH_M_PATH}'
        )
        # cSpell:enable
        return

    if args.entrypoint_bash_multiprocessing_paper:
        script_content = gen_bench_script_entrypoint_bash(
            datasets=er_dataset_names_for_paper_multiprocessing
            + dataset_names_for_paper_multiprocessing,
            bash_arg=f'--paper {args.bash_arg}',
            template=template_entrypoint_bash,
            multiprocessing=True,
        )
        ENTRYPOINT_SH_M_PAPER_PATH.write_text(script_content)
        ENTRYPOINT_SH_M_PAPER_PATH.chmod(
            ENTRYPOINT_SH_M_PAPER_PATH.stat().st_mode | S_IEXEC
        )
        # cSpell:disable
        print(
            f'Benchmark entrypoint shell script (for multiprocessing mbench_*.py) generated at {ENTRYPOINT_SH_M_PAPER_PATH}'
        )
        # cSpell:enable
        return

    if args.entrypoint_bash_er:
        script_content = gen_bench_script_entrypoint_bash(
            datasets=random_erdos_renyi_dataset_names,
            bash_arg=args.bash_arg_er,
            template=template_entrypoint_bash,
        )
        ENTRYPOINT_SH_ER_PATH.write_text(script_content)
        ENTRYPOINT_SH_ER_PATH.chmod(ENTRYPOINT_SH_ER_PATH.stat().st_mode | S_IEXEC)
        print(f'Benchmark entrypoint shell script generated at {ENTRYPOINT_SH_ER_PATH}')
        return

    loading_methods = {'loading': '', 'loading_undirected': '_undirected'}
    import yaml

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
    if args.profile:
        gbc = yaml.load(
            graph_benchmark_code_ordereddict_yaml_path.read_text(), Loader=Loader
        )
        for tool, method_to_code_mapping in gbc.items():
            for loading_method, script_name_suffix in loading_methods.items():
                m = method_to_code_mapping.copy()
                if loading_method not in m:
                    continue
                methods_to_pop = []
                if loading_method == 'loading':
                    methods_to_pop.append('loading_undirected')
                if loading_method == 'loading_undirected':
                    methods_to_pop.append('loading')
                    # methods_to_pop += ['page rank', 'strongly connected components']
                    methods_to_pop += ['strongly connected components']
                [m.pop(method_to_pop, None) for method_to_pop in methods_to_pop]
                script_content = gen_profile_script(tool, m, template_profile_script)
                output_path = Path(f'profile_{tool}{script_name_suffix}.py')
                output_path.write_text(script_content)
                output_path.chmod(output_path.stat().st_mode | S_IEXEC)
                print(f'Profile script for {tool} generated at {output_path}')
        return

    if args.profile_entrypoint:
        output_path = Path('profile_entrypoint.sh')
        script_lines = ['#!/usr/bin/env bash', '']
        gi = json.loads(graph_info_json_path.read_text())
        gbc = yaml.load(
            graph_benchmark_code_ordereddict_yaml_path.read_text(), Loader=Loader
        )
        for edgelist_path in edgelist_filenames:
            p = Path(edgelist_path)
            dataset_name = p.stem
            script_lines += [
                '',
                f'# dataset: {dataset_name}',
                '''echo "\033[35m============================================\033[0m"''',
                f'''echo "dataset: \033[34m{dataset_name}\033[0m"''',
                '''echo "\033[35m============================================\033[0m"''',
                '',
            ]
            # print(dataset_name)
            for tool in gbc:
                # if tool in profile_tool_to_drop:
                #     continue
                is_directed = gi[dataset_name]['is_directed']
                script_name_suffix = '_undirected' if not is_directed else ''
                script_filename = f'profile_{tool}{script_name_suffix}.py'
                script_lines.append(
                    f'{"# " if tool in profile_tools_to_drop else ""}./{script_filename} {edgelist_path} "$@" || echo "./{script_filename} {edgelist_path} failed" >>profile_entrypoint.log'
                )
        output_path.write_text('\n'.join(script_lines))
        output_path.chmod(output_path.stat().st_mode | S_IEXEC)
        print(f'Profile entrypoint script generated at {output_path}')
        return

    if args.output is not None and len(args.dataset) == 1:
        dataset_name = args.dataset[0]
        script_content = gen_bench_script(dataset_name, template=template)
        output_path = args.output
        output_path.write_text(script_content)
        output_path.chmod(output_path.stat().st_mode | S_IEXEC)
        print(f'Benchmark script for {dataset_name} is generated at {output_path}')
    else:
        # ignores -o if dataset > 1
        if args.multiprocessing_bench_scripts:
            dataset_names = args.dataset
            if args.er_paper:
                dataset_names = [
                    load_func_name.removeprefix('load_')
                    for load_func_name in random_erdos_renyi_graphs_load_function_names_date_s
                ]
            for dataset_name in dataset_names:
                script_content = gen_bench_script(dataset_name, template=template_m)
                # cSpell:disable
                output_path = Path(f'mbench_{dataset_name}.py')
                # cSpell:enable
                output_path.write_text(script_content)
                output_path.chmod(output_path.stat().st_mode | S_IEXEC)
                print(
                    f'Multiprocessing benchmark script for {dataset_name} is generated at {output_path}'
                )
            return

        if args.er_paper:
            for load_func_name in random_erdos_renyi_graphs_load_function_names_date_s:
                dataset_name = load_func_name.removeprefix('load_')
                script_content = gen_bench_script(dataset_name, template=template)
                output_path = Path(f'bench_{dataset_name}.py')
                output_path.write_text(script_content)
                output_path.chmod(output_path.stat().st_mode | S_IEXEC)
                print(
                    f'Benchmark script for {dataset_name} is generated at {output_path}'
                )
            return

        for dataset_name in args.dataset:
            script_content = gen_bench_script(dataset_name, template=template)
            output_path = Path(f'bench_{dataset_name}.py')
            output_path.write_text(script_content)
            output_path.chmod(output_path.stat().st_mode | S_IEXEC)
            print(f'Benchmark script for {dataset_name} is generated at {output_path}')


if __name__ == '__main__':
    main()
