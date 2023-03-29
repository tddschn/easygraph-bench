#!/usr/bin/env bash

# Download data for Benchmarking (remove comments)
wget -nv 'http://snap.stanford.edu/data/email-Enron.txt.gz' &&
    gunzip email-Enron.txt.gz &&
    grep -v '^#' email-Enron.txt >enron.txt &&
    rm email-Enron.txt

wget -nv 'http://snap.stanford.edu/data/amazon0302.txt.gz' &&
    gunzip amazon0302.txt.gz &&
    grep -v '^#' amazon0302.txt >amazon.txt &&
    rm amazon0302.txt

wget -nv 'http://snap.stanford.edu/data/web-Google.txt.gz' &&
    gunzip web-Google.txt.gz &&
    grep -v '^#' web-Google.txt >google.txt &&
    rm web-Google.txt

wget -nv 'http://snap.stanford.edu/data/soc-pokec-relationships.txt.gz' &&
    gunzip soc-pokec-relationships.txt.gz &&
    grep -v '^#' soc-pokec-relationships.txt >pokec.txt &&
    rm soc-pokec-relationships.txt

wget -nv 'https://snap.stanford.edu/data/ca-CondMat.txt.gz' &&
    gunzip ca-CondMat.txt.gz &&
    grep -v '^#' ca-CondMat.txt >condmat.txt &&
    rm ca-CondMat.txt

wget -nv 'http://snap.stanford.edu/data/wiki-Vote.txt.gz' &&
    gunzip wiki-Vote.txt.gz &&
    grep -v '^#' wiki-Vote.txt >wikivote.txt &&
    rm wiki-Vote.txt

# https://snap.stanford.edu/data/ego-Facebook.html
wget -nv 'http://snap.stanford.edu/data/facebook_combined.txt.gz' &&
    gunzip facebook_combined.txt.gz &&
    grep -v '^#' facebook_combined.txt >facebook.txt &&
    rm facebook_combined.txt &&
    # convert ' ' to \t in facebook.txt
    sed -i 's/ /\t/g' facebook.txt

# https://snap.stanford.edu/data/ca-HepTh.html
wget -nv 'http://snap.stanford.edu/data/ca-HepTh.txt.gz' &&
    gunzip ca-HepTh.txt.gz &&
    grep -v '^#' ca-HepTh.txt >hepth.txt &&
    rm ca-HepTh.txt
