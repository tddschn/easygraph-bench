sanity-check: gen-scripts
	# ./bench_stub.py -D -p 1 -a -G new
	# ./bench_stub_directed.py -D -p 1 -a -G new
	# ./bench_stub_directed.py -D -p 1
	# ./bench_stub_nx.py -D -p 1
	# ./bench_stub_with_underscore.py -D -p 1
	# ./bench_stub_with_underscore.py -p 1
	# ./bench_pgp.py -D -p 1 -t 10 -G other

gen-scripts:
	./gen_bench_script.py
	./gen_bench_script.py -e
	./gen_bench_script.py -E
	./gen_bench_script.py --entrypoint-bash-er
	./gen_bench_script.py -P
	./gen_bench_script.py -Z
	./gen_bench_script.py -m
	./gen_bench_script.py -M
	./gen_bench_script.py --entrypoint-bash-multiprocessing-paper
	./gen_bench_script.py --entrypoint-bash-paper

deta:
	deta deploy ../easygraph-bench-results-fastapi

evaluate: clean
	./bench.py

clean: clean-outputs clean-figs

clean-outputs:
	rm *.{json,csv}

clean-figs:
	rm -rf images/

zip-csv:
	zip -r bench-results-csv.zip *.csv

zip-figs:
	zip -r bench-result-figures.zip images

bench-all:
	parallel gh workflow run bench.yaml -f uploadResultsAsArtifact="false" -f benchScriptSet={} ::: 'stub' 'stub-fast' 'normal' 'large' 'coauthorship'
	# gh workflow run bench.yaml -f uploadResultsAsArtifact="false" -f benchScriptSet=stub-fast
	# gh workflow run bench.yaml -f uploadResultsAsArtifact="false" -f benchScriptSet=stub
	# gh workflow run bench.yaml -f uploadResultsAsArtifact="false" -f benchScriptSet=normal
	# gh workflow run bench.yaml -f uploadResultsAsArtifact="false" -f benchScriptSet=large
	# gh workflow run bench.yaml -f uploadResultsAsArtifact="false" -f benchScriptSet=coauthorship

.PHONY: *
