#!/usr/bin/env python3

import easygraph as eg
import networkx as nx
import time
import os


eval_functions_name = ["average_clustering"]

load_functions_name = [
    "load_cheminformatics",
    "load_bio",
    "load_eco",
    # "load_soc"
]

di_load_functions_name = ["load_soc"]


def load_cheminformatics():
    G = eg.Graph()
    with open("./dataset/ENZYMES_g1/ENZYMES_g1.edges") as f:
        for l in f.readlines():
            v = l.split()
            G.add_edge(v[0], v[1])
    print(
        "ENZYMES_g1: " + "nodes: " + str(len(G.nodes)) + " edges: " + str(len(G.edges))
    )
    return G


def load_bio():
    G = eg.Graph()
    jump_lines = 2
    with open("./dataset/bio-yeast/bio-yeast.mtx") as f:
        for i, l in enumerate(f):
            if i < jump_lines:
                continue
            v = l.split()
            G.add_edge(v[0], v[1])
    print(
        "bio-yeast: " + "nodes: " + str(len(G.nodes)) + " edges: " + str(len(G.edges))
    )
    return G


def load_eco():
    G = eg.Graph()
    jump_lines = 14
    with open("./dataset/econ-mahindas/econ-mahindas.mtx") as f:
        for i, l in enumerate(f):
            if i < jump_lines:
                continue
            v = l.split()
            G.add_edge(v[0], v[1])
    print(
        "econ-mahindas: "
        + "nodes: "
        + str(len(G.nodes))
        + " edges: "
        + str(len(G.edges))
    )
    return G


def load_soc():
    # gplus为有向图
    G = eg.DiGraph()
    files = list_allfile("./dataset/gplus/", ".edges")
    print(files)
    for filename in files:  # type: ignore
        name = filename.split("/")[-1].split(".")[0]
        with open(filename) as f:
            for l in f:
                v = l.split()
                print(v)
                # a follow b
                G.add_edge(v[0], v[1])
                G.add_edge(name, v[0])
                G.add_edge(name, v[1])
            f.close()
        print("finish load " + filename)
    print("gplus: " + "nodes: " + str(len(G.nodes)) + " edges: " + str(len(G.edges)))
    return G


def draw(lf_n, data):
    import matplotlib
    from matplotlib import pyplot
    import matplotlib.pyplot as plt

    # matplotlib.rc("font",family='fangsong')
    import seaborn as sns
    import pandas as pd

    csv_file = lf_n + "_cost.csv"
    json2csv(data, csv_file)
    data = pd.read_csv(csv_file)

    fig_name = lf_n + '_compare.png'
    sns.set_style("whitegrid")
    sns.set(font="fangsong")
    ax = sns.barplot(
        x="method", y="cost", hue="tool", data=data, palette=sns.color_palette("hls", 8)
    )
    ax.set_title('comparison of easygraph and networkx in ' + lf_n)
    ax.set_xlabel("method")
    ax.set_ylabel("cost(s)")
    plt.savefig(fig_name, dpi=2000)
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


if __name__ == "__main__":

    # 遍历数据集
    for lf_n in load_functions_name:
        cost_dict = dict()
        # 遍历方法
        for ef_n in eval_functions_name:
            cost_dict[lf_n] = dict()
            cost_dict[lf_n][ef_n] = dict()

            # 加载数据
            g = eval(lf_n)()

            # 运行eg方法
            start = time.time()
            eg_res = eval("eg." + ef_n)(g, g.nodes)
            cost_dict[lf_n][ef_n]["eg"] = time.time() - start
            output(eg_res, lf_n + "_" + ef_n + "_eg_res.json")

            # 运行nx方法,判断转为无向图还是有向图
            if lf_n in di_load_functions_name:
                g = eg2nx_di(g)
            else:
                g = eg2nx(g)
            start = time.time()
            nx_res = eval("nx." + ef_n)(g, g.nodes)
            cost_dict[lf_n][ef_n]["nx"] = time.time() - start
            output(nx_res, lf_n + "_" + ef_n + "_nx_res.json")

        output(cost_dict, lf_n + "_cost.json")
        draw(lf_n, cost_dict)
