#!/usr/bin/env bash


# dataset: cheminformatics
echo "[35m============================================[0m"
echo "dataset 1/2: [34mcheminformatics (Directed)[0m"
echo "[35m============================================[0m"

# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_graphtool_cpp-sanity-check.py dataset/cheminformatics.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_igraph_cpp-sanity-check.py dataset/cheminformatics.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_networkit_cpp-sanity-check.py dataset/cheminformatics.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_networkx_cpp-sanity-check.py dataset/cheminformatics.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_snap_cpp-sanity-check.py dataset/cheminformatics.edgelist "$@"
echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m [1;4;32measygraph[0m'
./profile_easygraph_cpp-sanity-check.py dataset/cheminformatics.edgelist "$@"

# dataset: bio
echo "[35m============================================[0m"
echo "dataset 2/2: [34mbio (Undirected)[0m"
echo "[35m============================================[0m"

# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_graphtool_undirected_cpp-sanity-check.py dataset/bio.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_igraph_undirected_cpp-sanity-check.py dataset/bio.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_networkit_undirected_cpp-sanity-check.py dataset/bio.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_networkx_undirected_cpp-sanity-check.py dataset/bio.edgelist "$@"
# echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m easygraph'
# ./profile_snap_undirected_cpp-sanity-check.py dataset/bio.edgelist "$@"
echo '[9mgraphtool[0m [9migraph[0m [9mnetworkit[0m [9mnetworkx[0m [9msnap[0m [1;4;32measygraph[0m'
./profile_easygraph_undirected_cpp-sanity-check.py dataset/bio.edgelist "$@"