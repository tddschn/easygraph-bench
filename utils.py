#!/usr/bin/env python3

from pathlib import Path
import os
from pathlib import Path
from typing import Union, Optional
import easygraph as eg
import networkx as nx
import time
from copy import deepcopy
from .types import MethodName

from config import (
    eg_master_dir,
    load_functions_name,
    di_load_functions_name,
    clustering_methods,
    shortest_path_methods,
)


def draw(lf_n, data):
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
    ax.set_title(
        f'EasyGraph vs. Networkx\nDataset: {dataset_name}, Method: {method_name}'
    )
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
    import json

    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(path, "w", encoding="utf-8") as json_file:
        json_file.write(json_str)


def eg2nx(g):
    G = nx.Graph()
    for v1, v2, _ in g.edges:
        G.add_edge(v1, v2)
    return G


def eg2nx_di(g):
    G = nx.DiGraph()
    for v1, v2, _ in g.edges:
        G.add_edge(v1, v2)
    return G


def json2csv(json_data, filename):
    fw = open(filename, "w", encoding='utf-8')
    fw.write("method,tool,cost" + "\n")

    for key in json_data:
        for metric, val in json_data[key].items():
            for k, v in val.items():
                fw.write(metric + "," + k + "," + str(v) + "\n")

    fw.close()


def call_method(
    module, method, graph, args: Optional[list] = None, kwargs: Optional[dict] = None
):
    if args is None and kwargs is None:
        return getattr(module, method)(graph)
    if args is not None and kwargs is None:
        return getattr(module, method)(graph, *args)
    if args is None and kwargs is not None:
        return getattr(module, method)(graph, **kwargs)
    if args is not None and kwargs is not None:
        return getattr(module, method)(graph, *args, **kwargs)


def eval_method(
    cost_dict: dict,
    eg_graph,
    load_func_name: str,
    method_name: 'Union[str, tuple[str, str]]',
    # method_name: Optional[str] = None,
    # method_names: Optional[tuple[str, str]] = None,
    call_method_args_eg: Optional[list] = None,
    call_method_args_nx: Optional[list] = None,
    call_method_kwargs_eg: Optional[dict] = None,
    call_method_kwargs_nx: Optional[dict] = None,
):
    G = deepcopy(eg_graph)
    if isinstance(method_name, str):
        print('benchmarking method: ' + method_name)
        cost_dict[load_func_name] = dict()
        cost_dict[load_func_name][method_name] = dict()

        # 加载数据

        # 运行eg方法
        start = time.time()
        eg_res = call_method(
            eg, method_name, G, call_method_args_eg, call_method_kwargs_eg
        )
        cost_dict[load_func_name][method_name]["eg"] = time.time() - start
        output(eg_res, load_func_name + "_" + method_name + "_eg_res.json")

        # 运行nx方法,判断转为无向图还是有向图
        if load_func_name in di_load_functions_name:
            G = eg2nx_di(G)
        else:
            G = eg2nx(G)
        start = time.time()
        nx_res = call_method(
            nx, method_name, G, call_method_args_nx, call_method_kwargs_nx
        )
        cost_dict[load_func_name][method_name]["nx"] = time.time() - start
        output(
            nx_res,
            load_func_name.removeprefix('load_') + "_" + method_name + "_nx_res.json",
        )

        output(
            cost_dict,
            load_func_name.removeprefix('load_') + '_' + method_name + "_cost.json",
        )
        draw(load_func_name.removeprefix('load_') + '_' + method_name, cost_dict)
    elif isinstance(method_name, tuple):
        method_name_eg, method_name_nx = method_name
        print('benchmarking method: ' + method_name_eg)
        cost_dict[load_func_name] = dict()
        cost_dict[load_func_name][method_name_eg] = dict()

        # 加载数据

        # 运行eg方法
        start = time.time()
        eg_res = call_method(
            eg, method_name_eg, G, call_method_args_eg, call_method_kwargs_eg
        )
        cost_dict[load_func_name][method_name_eg]["eg"] = time.time() - start
        output(eg_res, load_func_name + "_" + method_name_eg + "_eg_res.json")

        # 运行nx方法,判断转为无向图还是有向图
        if load_func_name in di_load_functions_name:
            G = eg2nx_di(G)
        else:
            G = eg2nx(G)
        start = time.time()
        nx_res = call_method(
            nx, method_name_nx, G, call_method_args_nx, call_method_kwargs_nx
        )
        cost_dict[load_func_name][method_name_nx]["nx"] = time.time() - start
        output(
            nx_res,
            load_func_name.removeprefix('load_')
            + "_"
            + method_name_nx
            + "_nx_res.json",
        )

        output(
            cost_dict,
            load_func_name.removeprefix('load_') + '_' + method_name_nx + "_cost.json",
        )
        draw(load_func_name.removeprefix('load_') + '_' + method_name_nx, cost_dict)
    else:
        raise ValueError('method_name or method_names must be specified')
