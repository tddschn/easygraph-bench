#!/usr/bin/env python3

from pathlib import Path
import easygraph as eg
import networkx as nx
from config import DATASET_DIR
from utils import (
    list_allfile,
    load_func_for_nx,
    directed_dataset,
    print_with_hr,
    load_large_datasets_with_read_edgelist,
)


# --------------------
# @coreturn's datasets
# --------------------


def load_cheminformatics():
    """
    https://networkrepository.com/ENZYMES-g1.php
    """
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
    """
    https://networkrepository.com/bio-yeast.php
    """
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
    """
    https://networkrepository.com/econ-mahindas.php
    """
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


# --------------------
# road-usa
# --------------------
def load_road() -> eg.Graph:
    """
    partial dataset from
    https://networkrepository.com/road-usa.php
    """
    ROAD_DIR = DATASET_DIR / 'road'
    road_file_path = ROAD_DIR / 'road.txt'
    print_with_hr(f'loading graph road-usa from {str(road_file_path)} ...')
    G = eg.Graph()
    G.add_edges_from_file(str(road_file_path))
    print_with_hr(
        f'finished loading graph road-usa\nnodes: {len(G.nodes)}, edges: {len(G.edges)}, is_directed: {G.is_directed()}'
    )
    return G


# --------------------
# pgp network of trust
# --------------------


@directed_dataset
@load_func_for_nx
def load_pgp() -> nx.DiGraph:
    PGP_DIR = DATASET_DIR / "pgp"
    graph_file_path = PGP_DIR / "pgp.xml"
    print_with_hr(f'loading graph pgp from {str(graph_file_path)} ...')
    g = nx.read_graphml(str(graph_file_path))
    print_with_hr(
        f'finish loading graph pgp.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


@load_func_for_nx
def load_pgp_undirected() -> nx.Graph:
    PGP_DIR = DATASET_DIR / "pgp"
    graph_file_path = PGP_DIR / "pgp_undirected.xml"
    print_with_hr(f'loading graph pgp_undirected from {str(graph_file_path)} ...')
    g = nx.read_graphml(str(graph_file_path))
    print_with_hr(
        f'finish loading graph pgp_undirected.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


# --------------------
# other datasets used in the paper
# --------------------
# @load_func_for_nx
# def load_food() -> nx.


# --------------------
# really large datasets
# --------------------
@directed_dataset
@load_func_for_nx
def load_enron() -> nx.DiGraph:
    """
    https://snap.stanford.edu/data/email-Enron.html
    """
    p = Path('enron.txt')
    print_with_hr(f'loading graph enron from {str(p)} ...')
    if not p.exists():
        error_msg = f'enron.txt not found. Download from http://snap.stanford.edu/data/email-Enron.txt.gz .'
        raise FileNotFoundError(error_msg)
    g = load_large_datasets_with_read_edgelist(str(p))
    print_with_hr(
        f'finish loading graph enron.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


@directed_dataset
@load_func_for_nx
def load_google() -> nx.DiGraph:
    """
    https://snap.stanford.edu/data/web-Google.html
    """
    p = Path('google.txt')
    print_with_hr(f'loading graph google from {str(p)} ...')
    if not p.exists():
        error_msg = f'google.txt not found. Download from http://snap.stanford.edu/data/web-Google.txt.gz .'
        raise FileNotFoundError(error_msg)
    g = load_large_datasets_with_read_edgelist(str(p))
    print_with_hr(
        f'finish loading graph google.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


@directed_dataset
@load_func_for_nx
def load_amazon() -> nx.DiGraph:
    """
    https://snap.stanford.edu/data/amazon0302.html
    """
    p = Path('amazon.txt')
    print_with_hr(f'loading graph amazon from {str(p)} ...')
    if not p.exists():
        error_msg = f'amazon.txt not found. Download from http://snap.stanford.edu/data/amazon0302.txt.gz .'
        raise FileNotFoundError(error_msg)
    g = load_large_datasets_with_read_edgelist(str(p))
    print_with_hr(
        f'finish loading graph amazon.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


@directed_dataset
@load_func_for_nx
def load_pokec() -> nx.DiGraph:
    """
    https://snap.stanford.edu/data/soc-Pokec.html
    """
    p = Path('pokec.txt')
    print_with_hr(f'loading graph pokec from {str(p)} ...')
    if not p.exists():
        error_msg = f'pokec.txt not found. Download from http://snap.stanford.edu/data/soc-pokec-relationships.txt.gz .'
        raise FileNotFoundError(error_msg)
    g = load_large_datasets_with_read_edgelist(str(p))
    print_with_hr(
        f'finish loading graph pokec.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


# --------------------
# chenyang03/co-authorship-network (very large)
# --------------------
# @directed_dataset
@load_func_for_nx
def load_coauthorship(
    coauthorship_edges_file: str = '../co-authorship-network/edges.txt',
) -> nx.DiGraph:
    """
    https://github.com/chenyang03/co-authorship-network
    """
    print_with_hr(f'loading graph coauthorship from {coauthorship_edges_file} ...')
    number_of_nodes = 402392
    g: nx.DiGraph = nx.read_edgelist(
        coauthorship_edges_file,
        delimiter=',',
        nodetype=int,  # create_using=nx.DiGraph()
    )
    g.add_nodes_from(range(number_of_nodes))
    print_with_hr(
        f'finish loading graph coauthorship.\nnodes: {len(g.nodes)}, edges: {len(g.edges)}, is_directed: {g.is_directed()}'
    )
    return g


# --------------------
# stub loaders
# --------------------


def load_stub():
    print_with_hr('loading graph stub ...')
    G: eg.Graph = eg.complete_graph(5)  # type: ignore
    print_with_hr(
        f'finished loading graph stub\nnodes: {len(G.nodes)}, edges: {len(G.edges)}, is_directed: {G.is_directed()}'
    )
    return G


def load_stub_with_underscore():
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


@load_func_for_nx
def load_stub_nx():
    print_with_hr('loading graph stub_nx ...')
    G = nx.complete_graph(5)  # type: ignore
    print_with_hr(
        f'finished loading graph stub_nx\nnodes: {len(G.nodes)}, edges: {len(G.edges)}, is_directed: {G.is_directed()}'
    )
    return G
