#!/usr/bin/env bash


# dataset: cheminformatics
echo "[35m============================================[0m"
echo "dataset: [34mcheminformatics[0m"
echo "[35m============================================[0m"

./profile_graphtool.py dataset/cheminformatics.edgelist "$@" || echo "./profile_graphtool.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_igraph.py dataset/cheminformatics.edgelist "$@" || echo "./profile_igraph.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_networkit.py dataset/cheminformatics.edgelist "$@" || echo "./profile_networkit.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_networkx.py dataset/cheminformatics.edgelist "$@" || echo "./profile_networkx.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
# ./profile_snap.py dataset/cheminformatics.edgelist "$@" || echo "./profile_snap.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log
./profile_easygraph.py dataset/cheminformatics.edgelist "$@" || echo "./profile_easygraph.py dataset/cheminformatics.edgelist failed" >>profile_entrypoint.log

# dataset: bio
echo "[35m============================================[0m"
echo "dataset: [34mbio[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/bio.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/bio.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/bio.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/bio.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/bio.edgelist "$@" || echo "./profile_snap_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/bio.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/bio.edgelist failed" >>profile_entrypoint.log

# dataset: eco
echo "[35m============================================[0m"
echo "dataset: [34meco[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/eco.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/eco.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/eco.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/eco.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/eco.edgelist "$@" || echo "./profile_snap_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/eco.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/eco.edgelist failed" >>profile_entrypoint.log

# dataset: pgp
echo "[35m============================================[0m"
echo "dataset: [34mpgp[0m"
echo "[35m============================================[0m"

./profile_graphtool.py dataset/pgp.edgelist "$@" || echo "./profile_graphtool.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_igraph.py dataset/pgp.edgelist "$@" || echo "./profile_igraph.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_networkit.py dataset/pgp.edgelist "$@" || echo "./profile_networkit.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_networkx.py dataset/pgp.edgelist "$@" || echo "./profile_networkx.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
# ./profile_snap.py dataset/pgp.edgelist "$@" || echo "./profile_snap.py dataset/pgp.edgelist failed" >>profile_entrypoint.log
./profile_easygraph.py dataset/pgp.edgelist "$@" || echo "./profile_easygraph.py dataset/pgp.edgelist failed" >>profile_entrypoint.log

# dataset: pgp_undirected
echo "[35m============================================[0m"
echo "dataset: [34mpgp_undirected[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_snap_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/pgp_undirected.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/pgp_undirected.edgelist failed" >>profile_entrypoint.log

# dataset: road
echo "[35m============================================[0m"
echo "dataset: [34mroad[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/road.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/road.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/road.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/road.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/road.edgelist "$@" || echo "./profile_snap_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/road.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/road.edgelist failed" >>profile_entrypoint.log

# dataset: uspowergrid
echo "[35m============================================[0m"
echo "dataset: [34muspowergrid[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_snap_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/uspowergrid.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/uspowergrid.edgelist failed" >>profile_entrypoint.log

# dataset: enron
echo "[35m============================================[0m"
echo "dataset: [34menron[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py enron.txt "$@" || echo "./profile_graphtool_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py enron.txt "$@" || echo "./profile_igraph_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py enron.txt "$@" || echo "./profile_networkit_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py enron.txt "$@" || echo "./profile_networkx_undirected.py enron.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py enron.txt "$@" || echo "./profile_snap_undirected.py enron.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py enron.txt "$@" || echo "./profile_easygraph_undirected.py enron.txt failed" >>profile_entrypoint.log

# dataset: amazon
echo "[35m============================================[0m"
echo "dataset: [34mamazon[0m"
echo "[35m============================================[0m"

./profile_graphtool.py amazon.txt "$@" || echo "./profile_graphtool.py amazon.txt failed" >>profile_entrypoint.log
./profile_igraph.py amazon.txt "$@" || echo "./profile_igraph.py amazon.txt failed" >>profile_entrypoint.log
./profile_networkit.py amazon.txt "$@" || echo "./profile_networkit.py amazon.txt failed" >>profile_entrypoint.log
./profile_networkx.py amazon.txt "$@" || echo "./profile_networkx.py amazon.txt failed" >>profile_entrypoint.log
# ./profile_snap.py amazon.txt "$@" || echo "./profile_snap.py amazon.txt failed" >>profile_entrypoint.log
./profile_easygraph.py amazon.txt "$@" || echo "./profile_easygraph.py amazon.txt failed" >>profile_entrypoint.log

# dataset: google
echo "[35m============================================[0m"
echo "dataset: [34mgoogle[0m"
echo "[35m============================================[0m"

./profile_graphtool.py google.txt "$@" || echo "./profile_graphtool.py google.txt failed" >>profile_entrypoint.log
./profile_igraph.py google.txt "$@" || echo "./profile_igraph.py google.txt failed" >>profile_entrypoint.log
./profile_networkit.py google.txt "$@" || echo "./profile_networkit.py google.txt failed" >>profile_entrypoint.log
./profile_networkx.py google.txt "$@" || echo "./profile_networkx.py google.txt failed" >>profile_entrypoint.log
# ./profile_snap.py google.txt "$@" || echo "./profile_snap.py google.txt failed" >>profile_entrypoint.log
./profile_easygraph.py google.txt "$@" || echo "./profile_easygraph.py google.txt failed" >>profile_entrypoint.log

# dataset: pokec
echo "[35m============================================[0m"
echo "dataset: [34mpokec[0m"
echo "[35m============================================[0m"

./profile_graphtool.py pokec.txt "$@" || echo "./profile_graphtool.py pokec.txt failed" >>profile_entrypoint.log
./profile_igraph.py pokec.txt "$@" || echo "./profile_igraph.py pokec.txt failed" >>profile_entrypoint.log
./profile_networkit.py pokec.txt "$@" || echo "./profile_networkit.py pokec.txt failed" >>profile_entrypoint.log
./profile_networkx.py pokec.txt "$@" || echo "./profile_networkx.py pokec.txt failed" >>profile_entrypoint.log
# ./profile_snap.py pokec.txt "$@" || echo "./profile_snap.py pokec.txt failed" >>profile_entrypoint.log
./profile_easygraph.py pokec.txt "$@" || echo "./profile_easygraph.py pokec.txt failed" >>profile_entrypoint.log

# dataset: condmat
echo "[35m============================================[0m"
echo "dataset: [34mcondmat[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py condmat.txt "$@" || echo "./profile_graphtool_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py condmat.txt "$@" || echo "./profile_igraph_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py condmat.txt "$@" || echo "./profile_networkit_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py condmat.txt "$@" || echo "./profile_networkx_undirected.py condmat.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py condmat.txt "$@" || echo "./profile_snap_undirected.py condmat.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py condmat.txt "$@" || echo "./profile_easygraph_undirected.py condmat.txt failed" >>profile_entrypoint.log

# dataset: wikivote
echo "[35m============================================[0m"
echo "dataset: [34mwikivote[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py wikivote.txt "$@" || echo "./profile_graphtool_undirected.py wikivote.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py wikivote.txt "$@" || echo "./profile_igraph_undirected.py wikivote.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py wikivote.txt "$@" || echo "./profile_networkit_undirected.py wikivote.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py wikivote.txt "$@" || echo "./profile_networkx_undirected.py wikivote.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py wikivote.txt "$@" || echo "./profile_snap_undirected.py wikivote.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py wikivote.txt "$@" || echo "./profile_easygraph_undirected.py wikivote.txt failed" >>profile_entrypoint.log

# dataset: cheminformatics_lcc
echo "[35m============================================[0m"
echo "dataset: [34mcheminformatics_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/cheminformatics_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/cheminformatics_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: bio_lcc
echo "[35m============================================[0m"
echo "dataset: [34mbio_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/bio_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/bio_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: eco_lcc
echo "[35m============================================[0m"
echo "dataset: [34meco_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/eco_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/eco_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: pgp_lcc
echo "[35m============================================[0m"
echo "dataset: [34mpgp_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/pgp_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/pgp_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: pgp_undirected_lcc
echo "[35m============================================[0m"
echo "dataset: [34mpgp_undirected_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/pgp_undirected_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/pgp_undirected_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: road_lcc
echo "[35m============================================[0m"
echo "dataset: [34mroad_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/road_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/road_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: uspowergrid_lcc
echo "[35m============================================[0m"
echo "dataset: [34muspowergrid_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_graphtool_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_igraph_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_igraph_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkit_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_networkit_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_networkx_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_networkx_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_snap_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py dataset/uspowergrid_lcc.edgelist "$@" || echo "./profile_easygraph_undirected.py dataset/uspowergrid_lcc.edgelist failed" >>profile_entrypoint.log

# dataset: enron_lcc
echo "[35m============================================[0m"
echo "dataset: [34menron_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py enron_lcc.txt "$@" || echo "./profile_graphtool_undirected.py enron_lcc.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py enron_lcc.txt "$@" || echo "./profile_igraph_undirected.py enron_lcc.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py enron_lcc.txt "$@" || echo "./profile_networkit_undirected.py enron_lcc.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py enron_lcc.txt "$@" || echo "./profile_networkx_undirected.py enron_lcc.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py enron_lcc.txt "$@" || echo "./profile_snap_undirected.py enron_lcc.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py enron_lcc.txt "$@" || echo "./profile_easygraph_undirected.py enron_lcc.txt failed" >>profile_entrypoint.log

# dataset: amazon_lcc
echo "[35m============================================[0m"
echo "dataset: [34mamazon_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py amazon_lcc.txt "$@" || echo "./profile_graphtool_undirected.py amazon_lcc.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py amazon_lcc.txt "$@" || echo "./profile_igraph_undirected.py amazon_lcc.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py amazon_lcc.txt "$@" || echo "./profile_networkit_undirected.py amazon_lcc.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py amazon_lcc.txt "$@" || echo "./profile_networkx_undirected.py amazon_lcc.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py amazon_lcc.txt "$@" || echo "./profile_snap_undirected.py amazon_lcc.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py amazon_lcc.txt "$@" || echo "./profile_easygraph_undirected.py amazon_lcc.txt failed" >>profile_entrypoint.log

# dataset: google_lcc
echo "[35m============================================[0m"
echo "dataset: [34mgoogle_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py google_lcc.txt "$@" || echo "./profile_graphtool_undirected.py google_lcc.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py google_lcc.txt "$@" || echo "./profile_igraph_undirected.py google_lcc.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py google_lcc.txt "$@" || echo "./profile_networkit_undirected.py google_lcc.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py google_lcc.txt "$@" || echo "./profile_networkx_undirected.py google_lcc.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py google_lcc.txt "$@" || echo "./profile_snap_undirected.py google_lcc.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py google_lcc.txt "$@" || echo "./profile_easygraph_undirected.py google_lcc.txt failed" >>profile_entrypoint.log

# dataset: pokec_lcc
echo "[35m============================================[0m"
echo "dataset: [34mpokec_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py pokec_lcc.txt "$@" || echo "./profile_graphtool_undirected.py pokec_lcc.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py pokec_lcc.txt "$@" || echo "./profile_igraph_undirected.py pokec_lcc.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py pokec_lcc.txt "$@" || echo "./profile_networkit_undirected.py pokec_lcc.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py pokec_lcc.txt "$@" || echo "./profile_networkx_undirected.py pokec_lcc.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py pokec_lcc.txt "$@" || echo "./profile_snap_undirected.py pokec_lcc.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py pokec_lcc.txt "$@" || echo "./profile_easygraph_undirected.py pokec_lcc.txt failed" >>profile_entrypoint.log

# dataset: condmat_lcc
echo "[35m============================================[0m"
echo "dataset: [34mcondmat_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py condmat_lcc.txt "$@" || echo "./profile_graphtool_undirected.py condmat_lcc.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py condmat_lcc.txt "$@" || echo "./profile_igraph_undirected.py condmat_lcc.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py condmat_lcc.txt "$@" || echo "./profile_networkit_undirected.py condmat_lcc.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py condmat_lcc.txt "$@" || echo "./profile_networkx_undirected.py condmat_lcc.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py condmat_lcc.txt "$@" || echo "./profile_snap_undirected.py condmat_lcc.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py condmat_lcc.txt "$@" || echo "./profile_easygraph_undirected.py condmat_lcc.txt failed" >>profile_entrypoint.log

# dataset: wikivote_lcc
echo "[35m============================================[0m"
echo "dataset: [34mwikivote_lcc[0m"
echo "[35m============================================[0m"

./profile_graphtool_undirected.py wikivote_lcc.txt "$@" || echo "./profile_graphtool_undirected.py wikivote_lcc.txt failed" >>profile_entrypoint.log
./profile_igraph_undirected.py wikivote_lcc.txt "$@" || echo "./profile_igraph_undirected.py wikivote_lcc.txt failed" >>profile_entrypoint.log
./profile_networkit_undirected.py wikivote_lcc.txt "$@" || echo "./profile_networkit_undirected.py wikivote_lcc.txt failed" >>profile_entrypoint.log
./profile_networkx_undirected.py wikivote_lcc.txt "$@" || echo "./profile_networkx_undirected.py wikivote_lcc.txt failed" >>profile_entrypoint.log
# ./profile_snap_undirected.py wikivote_lcc.txt "$@" || echo "./profile_snap_undirected.py wikivote_lcc.txt failed" >>profile_entrypoint.log
./profile_easygraph_undirected.py wikivote_lcc.txt "$@" || echo "./profile_easygraph_undirected.py wikivote_lcc.txt failed" >>profile_entrypoint.log