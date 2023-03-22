#!/usr/bin/env bash


# dataset: cheminformatics
echo "[35m============================================[0m"
echo "dataset: [34mcheminformatics[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_20230322-centrality.py dataset/cheminformatics.edgelist "$@" || echo "./profile_graphtool_20230322-centrality.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_igraph_20230322-centrality.py dataset/cheminformatics.edgelist "$@" || echo "./profile_igraph_20230322-centrality.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
# ./profile_networkit_20230322-centrality.py dataset/cheminformatics.edgelist "$@" || echo "./profile_networkit_20230322-centrality.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
# ./profile_networkx_20230322-centrality.py dataset/cheminformatics.edgelist "$@" || echo "./profile_networkx_20230322-centrality.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_20230322-centrality.py dataset/cheminformatics.edgelist "$@" || echo "./profile_snap_20230322-centrality.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_20230322-centrality.py dataset/cheminformatics.edgelist "$@" || echo "./profile_easygraph_20230322-centrality.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log

# dataset: bio
echo "[35m============================================[0m"
echo "dataset: [34mbio[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_undirected_20230322-centrality.py dataset/bio.edgelist "$@" || echo "./profile_graphtool_undirected_20230322-centrality.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected_20230322-centrality.py dataset/bio.edgelist "$@" || echo "./profile_igraph_undirected_20230322-centrality.py dataset/bio.edgelist failed" >>profile_entrypoint.log
# ./profile_networkit_undirected_20230322-centrality.py dataset/bio.edgelist "$@" || echo "./profile_networkit_undirected_20230322-centrality.py dataset/bio.edgelist failed" >>profile_entrypoint.log
# ./profile_networkx_undirected_20230322-centrality.py dataset/bio.edgelist "$@" || echo "./profile_networkx_undirected_20230322-centrality.py dataset/bio.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected_20230322-centrality.py dataset/bio.edgelist "$@" || echo "./profile_snap_undirected_20230322-centrality.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected_20230322-centrality.py dataset/bio.edgelist "$@" || echo "./profile_easygraph_undirected_20230322-centrality.py dataset/bio.edgelist failed" >>profile_entrypoint.log

# dataset: eco
echo "[35m============================================[0m"
echo "dataset: [34meco[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_undirected_20230322-centrality.py dataset/eco.edgelist "$@" || echo "./profile_graphtool_undirected_20230322-centrality.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected_20230322-centrality.py dataset/eco.edgelist "$@" || echo "./profile_igraph_undirected_20230322-centrality.py dataset/eco.edgelist failed" >>profile_entrypoint.log
# ./profile_networkit_undirected_20230322-centrality.py dataset/eco.edgelist "$@" || echo "./profile_networkit_undirected_20230322-centrality.py dataset/eco.edgelist failed" >>profile_entrypoint.log
# ./profile_networkx_undirected_20230322-centrality.py dataset/eco.edgelist "$@" || echo "./profile_networkx_undirected_20230322-centrality.py dataset/eco.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected_20230322-centrality.py dataset/eco.edgelist "$@" || echo "./profile_snap_undirected_20230322-centrality.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected_20230322-centrality.py dataset/eco.edgelist "$@" || echo "./profile_easygraph_undirected_20230322-centrality.py dataset/eco.edgelist failed" >>profile_entrypoint.log

# dataset: pgp
echo "[35m============================================[0m"
echo "dataset: [34mpgp[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_20230322-centrality.py dataset/pgp.edgelist "$@" || echo "./profile_graphtool_20230322-centrality.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_igraph_20230322-centrality.py dataset/pgp.edgelist "$@" || echo "./profile_igraph_20230322-centrality.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
# ./profile_networkit_20230322-centrality.py dataset/pgp.edgelist "$@" || echo "./profile_networkit_20230322-centrality.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
# ./profile_networkx_20230322-centrality.py dataset/pgp.edgelist "$@" || echo "./profile_networkx_20230322-centrality.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_20230322-centrality.py dataset/pgp.edgelist "$@" || echo "./profile_snap_20230322-centrality.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_20230322-centrality.py dataset/pgp.edgelist "$@" || echo "./profile_easygraph_20230322-centrality.py dataset/pgp.edgelist failed" >>profile_entrypoint.log

# dataset: pgp_undirected
echo "[35m============================================[0m"
echo "dataset: [34mpgp_undirected[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_graphtool_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_igraph_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
# ./profile_networkit_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_networkit_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
# ./profile_networkx_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_networkx_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_snap_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_easygraph_undirected_20230322-centrality.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log

# dataset: road
echo "[35m============================================[0m"
echo "dataset: [34mroad[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_undirected_20230322-centrality.py dataset/road.edgelist "$@" || echo "./profile_graphtool_undirected_20230322-centrality.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected_20230322-centrality.py dataset/road.edgelist "$@" || echo "./profile_igraph_undirected_20230322-centrality.py dataset/road.edgelist failed" >>profile_entrypoint.log
# ./profile_networkit_undirected_20230322-centrality.py dataset/road.edgelist "$@" || echo "./profile_networkit_undirected_20230322-centrality.py dataset/road.edgelist failed" >>profile_entrypoint.log
# ./profile_networkx_undirected_20230322-centrality.py dataset/road.edgelist "$@" || echo "./profile_networkx_undirected_20230322-centrality.py dataset/road.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected_20230322-centrality.py dataset/road.edgelist "$@" || echo "./profile_snap_undirected_20230322-centrality.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected_20230322-centrality.py dataset/road.edgelist "$@" || echo "./profile_easygraph_undirected_20230322-centrality.py dataset/road.edgelist failed" >>profile_entrypoint.log

# dataset: uspowergrid
echo "[35m============================================[0m"
echo "dataset: [34muspowergrid[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_undirected_20230322-centrality.py dataset/uspowergrid.edgelist "$@" || echo "./profile_graphtool_undirected_20230322-centrality.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected_20230322-centrality.py dataset/uspowergrid.edgelist "$@" || echo "./profile_igraph_undirected_20230322-centrality.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
# ./profile_networkit_undirected_20230322-centrality.py dataset/uspowergrid.edgelist "$@" || echo "./profile_networkit_undirected_20230322-centrality.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
# ./profile_networkx_undirected_20230322-centrality.py dataset/uspowergrid.edgelist "$@" || echo "./profile_networkx_undirected_20230322-centrality.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected_20230322-centrality.py dataset/uspowergrid.edgelist "$@" || echo "./profile_snap_undirected_20230322-centrality.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected_20230322-centrality.py dataset/uspowergrid.edgelist "$@" || echo "./profile_easygraph_undirected_20230322-centrality.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log

# dataset: enron
echo "[35m============================================[0m"
echo "dataset: [34menron[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_undirected_20230322-centrality.py enron.txt "$@" || echo "./profile_graphtool_undirected_20230322-centrality.py enron.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected_20230322-centrality.py enron.txt "$@" || echo "./profile_igraph_undirected_20230322-centrality.py enron.txt failed" >>profile_entrypoint.log
# ./profile_networkit_undirected_20230322-centrality.py enron.txt "$@" || echo "./profile_networkit_undirected_20230322-centrality.py enron.txt failed" >>profile_entrypoint.log
# ./profile_networkx_undirected_20230322-centrality.py enron.txt "$@" || echo "./profile_networkx_undirected_20230322-centrality.py enron.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected_20230322-centrality.py enron.txt "$@" || echo "./profile_snap_undirected_20230322-centrality.py enron.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected_20230322-centrality.py enron.txt "$@" || echo "./profile_easygraph_undirected_20230322-centrality.py enron.txt failed" >>profile_entrypoint.log

# dataset: amazon
echo "[35m============================================[0m"
echo "dataset: [34mamazon[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_20230322-centrality.py amazon.txt "$@" || echo "./profile_graphtool_20230322-centrality.py amazon.txt failed" >>profile_entrypoint.log
./profile_igraph_20230322-centrality.py amazon.txt "$@" || echo "./profile_igraph_20230322-centrality.py amazon.txt failed" >>profile_entrypoint.log
# ./profile_networkit_20230322-centrality.py amazon.txt "$@" || echo "./profile_networkit_20230322-centrality.py amazon.txt failed" >>profile_entrypoint.log
# ./profile_networkx_20230322-centrality.py amazon.txt "$@" || echo "./profile_networkx_20230322-centrality.py amazon.txt failed" >>profile_entrypoint.log
# ./profile_snap_20230322-centrality.py amazon.txt "$@" || echo "./profile_snap_20230322-centrality.py amazon.txt failed" >>profile_entrypoint.log
./profile_easygraph_20230322-centrality.py amazon.txt "$@" || echo "./profile_easygraph_20230322-centrality.py amazon.txt failed" >>profile_entrypoint.log

# dataset: google
echo "[35m============================================[0m"
echo "dataset: [34mgoogle[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_20230322-centrality.py google.txt "$@" || echo "./profile_graphtool_20230322-centrality.py google.txt failed" >>profile_entrypoint.log
./profile_igraph_20230322-centrality.py google.txt "$@" || echo "./profile_igraph_20230322-centrality.py google.txt failed" >>profile_entrypoint.log
# ./profile_networkit_20230322-centrality.py google.txt "$@" || echo "./profile_networkit_20230322-centrality.py google.txt failed" >>profile_entrypoint.log
# ./profile_networkx_20230322-centrality.py google.txt "$@" || echo "./profile_networkx_20230322-centrality.py google.txt failed" >>profile_entrypoint.log
# ./profile_snap_20230322-centrality.py google.txt "$@" || echo "./profile_snap_20230322-centrality.py google.txt failed" >>profile_entrypoint.log
./profile_easygraph_20230322-centrality.py google.txt "$@" || echo "./profile_easygraph_20230322-centrality.py google.txt failed" >>profile_entrypoint.log

# dataset: pokec
echo "[35m============================================[0m"
echo "dataset: [34mpokec[0m"
echo "[35m============================================[0m"

# ./profile_graphtool_20230322-centrality.py pokec.txt "$@" || echo "./profile_graphtool_20230322-centrality.py pokec.txt failed" >>profile_entrypoint.log
./profile_igraph_20230322-centrality.py pokec.txt "$@" || echo "./profile_igraph_20230322-centrality.py pokec.txt failed" >>profile_entrypoint.log
# ./profile_networkit_20230322-centrality.py pokec.txt "$@" || echo "./profile_networkit_20230322-centrality.py pokec.txt failed" >>profile_entrypoint.log
# ./profile_networkx_20230322-centrality.py pokec.txt "$@" || echo "./profile_networkx_20230322-centrality.py pokec.txt failed" >>profile_entrypoint.log
# ./profile_snap_20230322-centrality.py pokec.txt "$@" || echo "./profile_snap_20230322-centrality.py pokec.txt failed" >>profile_entrypoint.log
./profile_easygraph_20230322-centrality.py pokec.txt "$@" || echo "./profile_easygraph_20230322-centrality.py pokec.txt failed" >>profile_entrypoint.log