#!/usr/bin/env python3

from pathlib import Path
import os
from pathlib import Path
from typing import Generator, Union, Optional
import easygraph as eg
import networkx as nx
import time
from copy import deepcopy
from easygraph import Graph, DiGraph
import networkx as nx
from itertools import islice

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
        x="method", y="cost", hue="tool", data=data, palette=sns.color_palette("hls", 8)
    )
    if methods is not None:
        # diff method names
        title = f'EasyGraph vs. Networkx\nDataset: {dataset_name}\nMethods: eg.{methods[0]} vs. nx.{methods[1]}'
    else:
        title = f'EasyGraph vs. Networkx\nDataset: {dataset_name}\nMethods: eg.{method_name} vs. nx.{method_name}'
    ax.set_title(title)
    ax.set_xlabel("method")
    ax.set_ylabel("cost(s)")
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
    for v1, v2, _ in g.edges:
        G.add_edge(v1, v2)
    return G


def eg2nx_digraph(g: DiGraph) -> nx.DiGraph:
    G = nx.DiGraph()
    for v1, v2, _ in g.edges:
        G.add_edge(v1, v2)
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
        [G.add_edge(v1, v2) for v1, v2, _ in g.edges]
    else:
        raise NotImplementedError('DiGraphC not implemented')
    return G


def json2csv(json_data, filename):
    fw = open(filename, "w", encoding='utf-8')
    fw.write("method,tool,cost" + "\n")

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


def eval_method(
    cost_dict: dict,
    eg_graph,
    nx_graph,
    ceg_graph,
    load_func_name: str,
    method_name: 'Union[str, tuple[str, str]]',
    # method_name: Optional[str] = None,
    # method_names: Optional[tuple[str, str]] = None,
    call_method_args_eg: Optional[list] = None,
    call_method_args_ceg: Optional[list] = None,
    call_method_args_nx: Optional[list] = None,
    call_method_kwargs_eg: Optional[dict] = None,
    call_method_kwargs_ceg: Optional[dict] = None,
    call_method_kwargs_nx: Optional[dict] = None,
    dry_run: bool = False,
):
    G_eg = deepcopy(eg_graph)
    # G_ceg = deepcopy(ceg_graph)
    G_ceg = ceg_graph.copy()
    G_nx = deepcopy(nx_graph)

    load_func_name = load_func_name.removeprefix('load_')
    if isinstance(method_name, str):
        print(f'benchmarking eg.{method_name} and nx.{method_name} on {load_func_name}')
        if dry_run:
            return
        cost_dict[load_func_name] = dict()
        cost_dict[load_func_name][method_name] = dict()

        start = time.time()
        eg_res = call_method(
            eg, method_name, G_eg, call_method_args_eg, call_method_kwargs_eg
        )
        cost_dict[load_func_name][method_name]["eg"] = time.time() - start
        output(eg_res, load_func_name + "_" + method_name + "_eg_res.json")

        start = time.time()
        ceg_res = call_method(
            eg, method_name, G_ceg, call_method_args_ceg, call_method_kwargs_ceg
        )
        cost_dict[load_func_name][method_name]["ceg"] = time.time() - start
        output(ceg_res, load_func_name + "_" + method_name + "_ceg_res.json")

        start = time.time()
        nx_res = call_method(
            nx, method_name, G_nx, call_method_args_nx, call_method_kwargs_nx
        )
        cost_dict[load_func_name][method_name]["nx"] = time.time() - start
        output(
            nx_res,
            load_func_name + "_" + method_name + "_nx_res.json",
        )

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

        start = time.time()
        eg_res = call_method(
            eg, method_name_eg, G_eg, call_method_args_eg, call_method_kwargs_eg
        )
        cost_dict[load_func_name][method_name_eg]["eg"] = time.time() - start
        output(eg_res, load_func_name + "_" + method_name_eg + "_eg_res.json")

        start = time.time()
        nx_res = call_method(
            nx, method_name_nx, G_nx, call_method_args_nx, call_method_kwargs_nx
        )
        cost_dict[load_func_name][method_name_eg]["nx"] = time.time() - start
        output(
            nx_res,
            load_func_name + "_" + method_name_eg + "_nx_res.json",
        )

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
