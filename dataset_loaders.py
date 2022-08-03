#!/usr/bin/env python3

import easygraph as eg
from utils import list_allfile


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
    # gplus: digraph
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
