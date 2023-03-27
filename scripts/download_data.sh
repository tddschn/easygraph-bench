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
