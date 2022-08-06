#!/usr/bin/env python3

from pathlib import Path
import os
from pathlib import Path
from typing import Generator, Literal, Union, Optional
import easygraph as eg
import networkx as nx
import time
from copy import deepcopy
from easygraph import Graph, DiGraph
import networkx as nx
from itertools import islice
from timeit import Timer
from inspect import getsource
from textwrap import dedent

# from .types import MethodName

from config import (
    eg_master_dir,
    load_functions_name,
    di_load_functions_name,
    clustering_methods,
    shortest_path_methods,
)


def draw(lf_n, data, methods: Optional[tuple[str, str]] = None):
    # import matplotlib
    # from matplotlib import pyplot
    import matplotlib.pyplot as plt

    # matplotlib.rc("font",family='fangsong')
    import seaborn as sns
    import pandas as pd

    dataset_name, _, method_name = lf_n.partition('_')
    fig_dir = Path('images') / dataset_name
    fig_dir.mkdir(parents=True, exist_ok=True)
    csv_file = lf_n + "_cost.csv"
    json2csv(data, csv_file)
    data = pd.read_csv(csv_file)

    fig_path = fig_dir / (f'{method_name}.png')
    sns.set_style("whitegrid")
    sns.set(font="Helvetica")
    ax = sns.barplot(
        x="method",
        y="avg time",
        hue="tool",
        data=data,
        palette=sns.color_palette("hls", 8),
    )
    if methods is not None:
        # diff method names
        title = f'EasyGraph vs. Networkx\nDataset: {dataset_name}\nMethods: eg.{methods[0]} vs. nx.{methods[1]}'
    else:
        title = f'EasyGraph vs. Networkx\nDataset: {dataset_name}\nMethods: eg.{method_name} vs. nx.{method_name}'
    ax.set_title(title)
    ax.set_xlabel("method")
    ax.set_ylabel("time(s)")
    plt.savefig(fig_path, dpi=2000)
    plt.close()


def list_allfile(path, suffix, all_files=[], all_suffix_files=[]):
    if os.path.exists(path):
        files = os.listdir(path)
    else:
        print('this path not exist')
        return
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            list_allfile(os.path.join(path, file), all_files)
        else:
            all_files.append(os.path.join(path, file))
    for file in all_files:
        if file.endswith(suffix):
            all_suffix_files.append(file)
    return all_suffix_files


def output(data, path):
    """dump data as json to path"""
    import json

    try:
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
    except TypeError:
        json_str = json.dumps(
            {'error': 'Object cannot be serialized to JSON'},
            ensure_ascii=False,
            indent=2,
        )
    with open(path, "w", encoding="utf-8") as json_file:
        json_file.write(json_str)


def eg2nx_graph(g: Graph) -> nx.Graph:
    G = nx.Graph()
    nodes_with_edges = set()
    for v1, v2, _ in g.edges:
        G.add_edge(v1, v2)
        nodes_with_edges.add(v1)
        nodes_with_edges.add(v2)
    for node in set(g.nodes) - nodes_with_edges:
        G.add_node(node)
    return G


def eg2nx_digraph(g: DiGraph) -> nx.DiGraph:
    G = nx.DiGraph()
    nodes_with_edges = set()
    for v1, v2, _ in g.edges:
        G.add_edge(v1, v2)
        nodes_with_edges.add(v1)
        nodes_with_edges.add(v2)
    for node in set(g.nodes) - nodes_with_edges:
        G.add_node(node)
    return G


def eg2nx(g: Union[Graph, DiGraph]) -> Union[nx.Graph, nx.DiGraph]:
    # if load_func_name in di_load_functions_name:
    if isinstance(g, DiGraph):
        G = eg2nx_digraph(g)
    else:
        G = eg2nx_graph(g)
    return G


def eg2ceg(g: Union[Graph, DiGraph]) -> Union[Graph, DiGraph]:
    if isinstance(g, Graph):
        G = eg.GraphC()
        # [G.add_edge(v1, v2) for v1, v2, _ in g.edges]
        nodes_with_edges = set()
        for v1, v2, _ in g.edges:
            G.add_edge(v1, v2)
            nodes_with_edges.add(v1)
            nodes_with_edges.add(v2)
        for node in set(g.nodes) - nodes_with_edges:
            G.add_node(node)
    else:
        raise NotImplementedError('DiGraphC not implemented')
    return G


def json2csv(json_data, filename):
    fw = open(filename, "w", encoding='utf-8')
    fw.write("method,tool,avg time" + "\n")

    for key in json_data:
        for metric, val in json_data[key].items():
            for k, v in val.items():
                fw.write(metric + "," + k + "," + str(v) + "\n")

    fw.close()


# class MethodCaller:
#     def __init__(self, eg_graph, )
# def eg_call_method(cost_dict, method_name: str, G, call_method_args_eg, call_method_kwargs_eg):
#     start = time.time()
#     eg_res = call_method(
#         eg, method_name, G, call_method_args_eg, call_method_kwargs_eg
#     )
#     cost_dict[load_func_name][method_name]["eg"] = time.time() - start
#     output(eg_res, load_func_name + "_" + method_name + "_eg_res.json")


def call_method(
    module, method, graph, args: Optional[list] = None, kwargs: Optional[dict] = None
):
    if not hasattr(module, method):
        raise AttributeError(f'{module} has no attribute {method}')
    m = getattr(module, method)
    if args is None and kwargs is None:
        result = m(graph)
    elif args is not None and kwargs is None:
        result = m(graph, *args)
    elif args is None and kwargs is not None:
        result = m(graph, **kwargs)
    else:
        result = m(graph, *args, **kwargs)
    if isinstance(result, Generator):
        result = list(result)
    return result


def get_Timer_args(
    module: Literal['eg', 'nx'],
    method: str,
    graph: str,
    args: list[str] = [],
    kwargs: dict[str, str] = {},
) -> tuple[str, str]:

    timer_setup = f'from __main__ import eg, nx, G_eg, G_nx, G_ceg, first_node_eg, first_node_nx, first_node_ceg'
    # if module == 'eg':
    #     timer_setup = 'import easygraph as eg'
    # elif module == 'nx':
    #     timer_setup = 'import networkx as nx'
    # else:
    if module not in ('eg', 'nx'):
        raise ValueError(f'{module=} is not supported')

    args_str = ', '.join(args)
    args_str = ', ' + args_str if args_str else ''
    kwargs_str = ', '.join(f'{x}={y}' for x, y in kwargs.items())
    kwargs_str = ', ' + kwargs_str if kwargs_str else ''
    timer_stmt = f"""
    result = {module}.{method}({graph}{args_str}{kwargs_str})
    from typing import Generator
    if isinstance(result, Generator):
        list(result)
    """
    timer_stmt = dedent(timer_stmt).strip()
    return timer_stmt, timer_setup


def bench_with_timeit(
    module: Literal['eg', 'nx'],
    method: str,
    graph: str,
    args: list[str] = [],
    kwargs: dict[str, str] = {},
) -> float:
    timer = Timer(*get_Timer_args(module, method, graph, args, kwargs))
    print(f'{timer.src=}')  # type: ignore
    count, total_time = timer.autorange()
    return total_time / count


def eval_method(
    cost_dict: dict,
    # eg_graph,
    # nx_graph,
    # ceg_graph,
    load_func_name: str,
    method_name: 'Union[str, tuple[str, str]]',
    call_method_args_eg: list[str] = [],
    call_method_args_ceg: list[str] = [],
    call_method_args_nx: list[str] = [],
    call_method_kwargs_eg: dict[str, str] = {},
    call_method_kwargs_ceg: dict[str, str] = {},
    call_method_kwargs_nx: dict[str, str] = {},
    dry_run: bool = False,
    skip_ceg: bool = False,
):
    # raise DeprecationWarning('Deprecated. Use ./bench_*.py instead')

    load_func_name = load_func_name.removeprefix('load_')
    if isinstance(method_name, str):
        print(f'benchmarking eg.{method_name} and nx.{method_name} on {load_func_name}')
        if dry_run:
            return
        cost_dict[load_func_name] = dict()
        cost_dict[load_func_name][method_name] = dict()

        print('easygraph')
        avg_time_eg = bench_with_timeit(
            module='eg',
            method=method_name,
            graph='G_eg',
            args=call_method_args_eg,
            kwargs=call_method_kwargs_eg,
        )
        cost_dict[load_func_name][method_name]["easygraph"] = avg_time_eg

        if not skip_ceg:
            print('easygraph with C++ binding')
            avg_time_ceg = bench_with_timeit(
                module='eg',
                method=method_name,
                graph='G_ceg',
                args=call_method_args_ceg,
                kwargs=call_method_kwargs_ceg,
            )
            cost_dict[load_func_name][method_name]["eg w/ C++ binding"] = avg_time_ceg

        print('networkx')
        avg_time_nx = bench_with_timeit(
            module='nx',
            method=method_name,
            graph='G_nx',
            args=call_method_args_nx,
            kwargs=call_method_kwargs_nx,
        )
        cost_dict[load_func_name][method_name]["networkx"] = avg_time_nx

        output(
            cost_dict,
            load_func_name + '_' + method_name + "_cost.json",
        )
        draw(load_func_name + '_' + method_name, cost_dict)
    elif isinstance(method_name, tuple):
        method_name_eg, method_name_nx = method_name
        # print('benchmarking method: ' + method_name_eg)
        print(
            f'benchmarking eg.{method_name_eg} and nx.{method_name_nx} on {load_func_name}'
        )
        if dry_run:
            return
        cost_dict[load_func_name] = dict()
        cost_dict[load_func_name][method_name_eg] = dict()

        print('easygraph')
        avg_time_eg = bench_with_timeit(
            module='eg',
            method=method_name_eg,
            graph='G_eg',
            args=call_method_args_eg,
            kwargs=call_method_kwargs_eg,
        )
        cost_dict[load_func_name][method_name_eg]["easygraph"] = avg_time_eg

        if not skip_ceg:
            print('easygraph with C++ binding')
            avg_time_ceg = bench_with_timeit(
                module='eg',
                method=method_name_eg,
                graph='G_ceg',
                args=call_method_args_ceg,
                kwargs=call_method_kwargs_ceg,
            )
            cost_dict[load_func_name][method_name_eg][
                "eg w/ C++ binding"
            ] = avg_time_ceg

        print('networkx')
        avg_time_nx = bench_with_timeit(
            module='nx',
            method=method_name_nx,
            graph='G_nx',
            args=call_method_args_nx,
            kwargs=call_method_kwargs_nx,
        )
        cost_dict[load_func_name][method_name_eg]["networkx"] = avg_time_nx
        output(
            cost_dict,
            load_func_name + '_' + method_name_eg + "_cost.json",
        )
        draw(load_func_name + '_' + method_name_eg, cost_dict, methods=method_name)
    else:
        raise ValueError('method_name or method_names must be specified')


def get_first_node(g):
    nodes = g.nodes
    if isinstance(nodes, dict):
        nodes_iter = nodes.keys()
    else:
        nodes_iter = nodes
    return list(islice(nodes_iter, 1))[0]


# def bench_shortest_path(cost_dict: dict, eg_graph, load_func_name: str):
#     # the common method both libs support is dijkstra
#     # for nx, we'll calculate the avg time
#     G = deepcopy(eg_graph)
#     G_nx = eg2nx(G)
#     load_func_name = load_func_name.removeprefix('load_')
#     print(f'benchmarking shortest path')
#     print(f'benchmarking Dijkstra on eg')
#     start = time.time()
#     eg_res = call_method(eg, 'Dijkstra', G, [get_first_node(G)])
#     cost_dict[load_func_name]['Dijkstra']['eg'] = time.time() - start
#     output(eg_res, load_func_name + '_Dijkstra_eg_res.json')

#     print(f'benchmarking single_source_dijkstra_path on nx (avg time)')
#     start = time.time()
#     nx_res = call_method(nx, 'dijkstra_path_length', G_nx, [get_first_node(G_nx)])
#     cost_dict[load_func_name]['Dijkstra']['nx'] = time.time() - start
#     output(nx_res, load_func_name + '_Dijkstra_nx_res.json')
#     draw(load_func_name + '_Dijkstra', cost_dict)
