sanity-check: gen-scripts
	# ./bench_stub.py -D -p 1
	./bench_stub_nx.py -D -p 1

gen-scripts:
	./gen_bench_script.py

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

.PHONY: *
