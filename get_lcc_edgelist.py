#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2023-03-24
Purpose: Why not?
"""

import argparse
from pathlib import Path
import networkx as nx
from config import edgelist_filenames

def load_graph(filename: str) -> nx.Graph:
    return nx.read_edgelist(filename, delimiter="\t", nodetype=int, create_using=nx.Graph())

def get_lcc(g: nx.Graph) -> nx.Graph:
    return nx.subgraph(g, max(nx.connected_components(g), key=len))

def write_graph(g: nx.Graph, path: str):
    nx.write_edgelist(g, path, delimiter="\t", data=False)



def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Why not?',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)




    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    for filename in edgelist_filenames:
        new_path = Path(filename).with_stem(f"{Path(filename).stem}_lcc")
        if new_path.exists():
            continue
        g = load_graph(filename)
        lcc = get_lcc(g)
        write_graph(lcc, str(new_path))
        print(f'Converted {filename} to {new_path}')


if __name__ == '__main__':
    main()
