#!/usr/bin/env python3

import easygraph as eg
import networkx as nx
from config import DATASET_DIR
from utils import list_allfile, load_func_for_nx, directed_dataset, print_with_hr


def load_cheminformatics():
    print_with_hr(f'loading graph cheminformatics ...')
    G = eg.Graph()
    with open("./dataset/ENZYMES_g1/ENZYMES_g1.edges") as f:
        for l in f.readlines():
            v = l.split()
            G.add_edge(v[0], v[1])
    print_with_hr(
        'finished loading graph cheminformatics\n'
        + "ENZYMES_g1: "
        + "nodes: "
        + str(len(G.nodes))
        + " edges: "
        + str(len(G.edges))
        + "is_directed: "
        + str(G.is_directed())
    )
    return G


def load_bio():
    print_with_hr('loading graph bio ...')
    G = eg.Graph()
    jump_lines = 2
    with open("./dataset/bio-yeast/bio-yeast.mtx") as f:
        for i, l in enumerate(f):
            if i < jump_lines:
                continue
            v = l.split()
            G.add_edge(v[0], v[1])
    print_with_hr(
        'finished loading graph bio\n'
        + "bio-yeast: "
        + "nodes: "
        + str(len(G.nodes))
        + " edges: "
        + str(len(G.edges))
        + "is_directed: "
        + str(G.is_directed())
    )
    return G


def load_eco():
    print_with_hr('loading graph eco ...')
    G = eg.Graph()
    jump_lines = 14
    with open("./dataset/econ-mahindas/econ-mahindas.mtx") as f:
        for i, l in enumerate(f):
            if i < jump_lines:
                continue
            v = l.split()
            G.add_edge(v[0], v[1])
    print_with_hr(
        "finished loading graph eco\n"
        + "econ-mahindas: "
        + "nodes: "
        + str(len(G.nodes))
        + " edges: "
        + str(len(G.edges))
        + "is_directed: "
        + str(G.is_directed())
    )
    return G


@directed_dataset
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
    print(
        "gplus: "
        + "nodes: "
        + str(len(G.nodes))
        + " edges: "
        + str(len(G.edges))
        + "is_directed: "
        + str(G.is_directed())
    )
    return G


@directed_dataset
@load_func_for_nx
def load_pgp():
    PGP_DIR = DATASET_DIR / "pgp"
    graph_file_path = PGP_DIR / "pgp.xml"
    print_with_hr(f'loading graph pgp from {str(graph_file_path)} ...')
    g = nx.read_graphml(str(graph_file_path))
    print_with_hr(
        f'finish loading graph pgp.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


@load_func_for_nx
def load_pgp_undirected():
    PGP_DIR = DATASET_DIR / "pgp"
    graph_file_path = PGP_DIR / "pgp_undirected.xml"
    print_with_hr(f'loading graph pgp_undirected from {str(graph_file_path)} ...')
    g = nx.read_graphml(str(graph_file_path))
    print_with_hr(
        f'finish loading graph pgp_undirected.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


def load_stub():
    print_with_hr('loading graph stub ...')
    G: eg.Graph = eg.complete_graph(5)  # type: ignore
    print_with_hr(
        f'finished loading graph stub\nnodes: {len(G.nodes)}, edges: {len(G.edges)}, is_directed: {G.is_directed()}'
    )
    return G


@directed_dataset
def load_stub_directed():
    print_with_hr('loading graph stub_directed ...')
    G: eg.DiGraph = eg.complete_graph(5, create_using=eg.DiGraph)  # type: ignore
    print_with_hr(
        f'finished loading graph stub_directed\nnodes: {len(G.nodes)}, edges: {len(G.edges)}, is_directed: {G.is_directed()}'
    )
    return G
