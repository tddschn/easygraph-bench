#!/usr/bin/env bash


# dataset: cheminformatics
echo "[35m============================================[0m"
echo "dataset 1/20: [34mcheminformatics[0m"
echo "[35m============================================[0m"

./profile_graphtool.py dataset/cheminformatics.edgelist "$@" || echo "./profile_graphtool.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_igraph.py dataset/cheminformatics.edgelist "$@" || echo "./profile_igraph.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_networkit.py dataset/cheminformatics.edgelist "$@" || echo "./profile_networkit.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_networkx.py dataset/cheminformatics.edgelist "$@" || echo "./profile_networkx.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
# ./profile_snap.py dataset/cheminformatics.edgelist "$@" || echo "./profile_snap.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_easygraph.py dataset/cheminformatics.edgelist "$@" || echo "./profile_easygraph.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log

# dataset: bio
echo "[35m============================================[0m"
echo "dataset 2/20: [34mbio[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/bio.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/bio.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/bio.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/bio.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/bio.edgelist "$@" || echo "./profile_snap_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/bio.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log

# dataset: eco
echo "[35m============================================[0m"
echo "dataset 3/20: [34meco[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/eco.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/eco.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/eco.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/eco.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/eco.edgelist "$@" || echo "./profile_snap_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/eco.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log

# dataset: pgp
echo "[35m============================================[0m"
echo "dataset 4/20: [34mpgp[0m"
echo "[35m============================================[0m"

./profile_graphtool.py dataset/pgp.edgelist "$@" || echo "./profile_graphtool.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_igraph.py dataset/pgp.edgelist "$@" || echo "./profile_igraph.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_networkit.py dataset/pgp.edgelist "$@" || echo "./profile_networkit.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_networkx.py dataset/pgp.edgelist "$@" || echo "./profile_networkx.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
# ./profile_snap.py dataset/pgp.edgelist "$@" || echo "./profile_snap.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_easygraph.py dataset/pgp.edgelist "$@" || echo "./profile_easygraph.py dataset/pgp.edgelist failed" >>profile_entrypoint.log

# dataset: pgp_undirected
echo "[35m============================================[0m"
echo "dataset 5/20: [34mpgp_undirected[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_snap_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log

# dataset: road
echo "[35m============================================[0m"
echo "dataset 6/20: [34mroad[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/road.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/road.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/road.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/road.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/road.edgelist "$@" || echo "./profile_snap_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/road.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log

# dataset: uspowergrid
echo "[35m============================================[0m"
echo "dataset 7/20: [34muspowergrid[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_snap_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log

# dataset: enron
echo "[35m============================================[0m"
echo "dataset 8/20: [34menron[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py enron.txt "$@" || echo "./profile_graphtool_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py enron.txt "$@" || echo "./profile_igraph_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py enron.txt "$@" || echo "./profile_networkit_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py enron.txt "$@" || echo "./profile_networkx_undirected.py enron.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py enron.txt "$@" || echo "./profile_snap_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py enron.txt "$@" || echo "./profile_easygraph_undirected.py enron.txt failed" >>profile_entrypoint.log

# dataset: amazon
echo "[35m============================================[0m"
echo "dataset 9/20: [34mamazon[0m"
echo "[35m============================================[0m"

./profile_graphtool.py amazon.txt "$@" || echo "./profile_graphtool.py amazon.txt failed" >>profile_entrypoint.log
./profile_igraph.py amazon.txt "$@" || echo "./profile_igraph.py amazon.txt failed" >>profile_entrypoint.log
./profile_networkit.py amazon.txt "$@" || echo "./profile_networkit.py amazon.txt failed" >>profile_entrypoint.log
./profile_networkx.py amazon.txt "$@" || echo "./profile_networkx.py amazon.txt failed" >>profile_entrypoint.log
# ./profile_snap.py amazon.txt "$@" || echo "./profile_snap.py amazon.txt failed" >>profile_entrypoint.log
./profile_easygraph.py amazon.txt "$@" || echo "./profile_easygraph.py amazon.txt failed" >>profile_entrypoint.log

# dataset: google
echo "[35m============================================[0m"
echo "dataset 10/20: [34mgoogle[0m"
echo "[35m============================================[0m"

./profile_graphtool.py google.txt "$@" || echo "./profile_graphtool.py google.txt failed" >>profile_entrypoint.log
./profile_igraph.py google.txt "$@" || echo "./profile_igraph.py google.txt failed" >>profile_entrypoint.log
./profile_networkit.py google.txt "$@" || echo "./profile_networkit.py google.txt failed" >>profile_entrypoint.log
./profile_networkx.py google.txt "$@" || echo "./profile_networkx.py google.txt failed" >>profile_entrypoint.log
# ./profile_snap.py google.txt "$@" || echo "./profile_snap.py google.txt failed" >>profile_entrypoint.log
./profile_easygraph.py google.txt "$@" || echo "./profile_easygraph.py google.txt failed" >>profile_entrypoint.log

# dataset: pokec
echo "[35m============================================[0m"
echo "dataset 11/20: [34mpokec[0m"
echo "[35m============================================[0m"

./profile_graphtool.py pokec.txt "$@" || echo "./profile_graphtool.py pokec.txt failed" >>profile_entrypoint.log
./profile_igraph.py pokec.txt "$@" || echo "./profile_igraph.py pokec.txt failed" >>profile_entrypoint.log
./profile_networkit.py pokec.txt "$@" || echo "./profile_networkit.py pokec.txt failed" >>profile_entrypoint.log
./profile_networkx.py pokec.txt "$@" || echo "./profile_networkx.py pokec.txt failed" >>profile_entrypoint.log
# ./profile_snap.py pokec.txt "$@" || echo "./profile_snap.py pokec.txt failed" >>profile_entrypoint.log
./profile_easygraph.py pokec.txt "$@" || echo "./profile_easygraph.py pokec.txt failed" >>profile_entrypoint.log

# dataset: condmat
echo "[35m============================================[0m"
echo "dataset 12/20: [34mcondmat[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py condmat.txt "$@" || echo "./profile_graphtool_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py condmat.txt "$@" || echo "./profile_igraph_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py condmat.txt "$@" || echo "./profile_networkit_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py condmat.txt "$@" || echo "./profile_networkx_undirected.py condmat.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py condmat.txt "$@" || echo "./profile_snap_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py condmat.txt "$@" || echo "./profile_easygraph_undirected.py condmat.txt failed" >>profile_entrypoint.log

# dataset: wikivote
echo "[35m============================================[0m"
echo "dataset 13/20: [34mwikivote[0m"
echo "[35m============================================[0m"

./profile_graphtool.py wikivote.txt "$@" || echo "./profile_graphtool.py wikivote.txt failed" >>profile_entrypoint.log
./profile_igraph.py wikivote.txt "$@" || echo "./profile_igraph.py wikivote.txt failed" >>profile_entrypoint.log
./profile_networkit.py wikivote.txt "$@" || echo "./profile_networkit.py wikivote.txt failed" >>profile_entrypoint.log
./profile_networkx.py wikivote.txt "$@" || echo "./profile_networkx.py wikivote.txt failed" >>profile_entrypoint.log
# ./profile_snap.py wikivote.txt "$@" || echo "./profile_snap.py wikivote.txt failed" >>profile_entrypoint.log
./profile_easygraph.py wikivote.txt "$@" || echo "./profile_easygraph.py wikivote.txt failed" >>profile_entrypoint.log

# dataset: cheminformatics_lcc
echo "[35m============================================[0m"
echo "dataset 14/20: [34mcheminformatics_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: bio_lcc
echo "[35m============================================[0m"
echo "dataset 15/20: [34mbio_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: eco_lcc
echo "[35m============================================[0m"
echo "dataset 16/20: [34meco_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: pgp_lcc
echo "[35m============================================[0m"
echo "dataset 17/20: [34mpgp_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: pgp_undirected_lcc
echo "[35m============================================[0m"
echo "dataset 18/20: [34mpgp_undirected_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: road_lcc
echo "[35m============================================[0m"
echo "dataset 19/20: [34mroad_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: uspowergrid_lcc
echo "[35m============================================[0m"
echo "dataset 20/20: [34muspowergrid_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log