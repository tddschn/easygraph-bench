from igraph import *

g = Graph.Read('../dataset/cheminformatics.edgelist', format='edges', directed=False)
g.connected_components()
