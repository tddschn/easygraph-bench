# SHELL := /usr/local/bin/bash
REPOS=tddschn/easygraph-bench easy-graph/easygraph-bench
REPO_SERVER=easy-graph/easygraph-bench
TAGS=server local
TAG_SERVER=server
NOTE_FILE_SERVER=server-release-note.md



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
	./gen_bench_script.py --er-paper
	./gen_bench_script.py --er-paper --multiprocessing-bench-scripts

gen-scripts-20230322:
	./gen_profile_scripts_with_suffix_wrapper.py '20230322-centrality' --tools 'igraph' 'easygraph' --methods 'betweenness centrality' 'closeness centrality'

gen-scripts-20230323:
	./gen_bench_script.py --profile --profile-suffix '20230323-kcore-centrality' --profile-select-tools 'igraph' 'easygraph' --profile-select-methods 'betweenness centrality' 'closeness centrality' 'k-core'
	./gen_bench_script.py --profile-entrypoint --profile-suffix '20230323-kcore-centrality' --profile-select-tools 'igraph' 'easygraph' --profile-select-methods 'betweenness centrality' 'closeness centrality' 'k-core'

release-dbs:
	$(foreach REPO,$(REPOS), \
		$(foreach TAG,$(TAGS), \
			gh --repo $(REPO) release upload $(TAG) bench-results-$(TAG).db --clobber; \
		) \
	)

edit-server-release-note:
	$(foreach REPO,$(REPOS), \
		gh --repo $(REPO) release edit $(TAG_SERVER) -F $(NOTE_FILE_SERVER); \
	)

make-server-release-latest:
	$(foreach REPO,$(REPOS), \
		gh --repo $(REPO) release edit $(TAG_SERVER) --latest; \
	)


init-server-releases:
	$(foreach TAG,$(TAGS), \
		gh --repo $(REPO_SERVER) release create $(TAG) --generate-notes; \
	)


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

patch-p: patch install publish push
minor-p: minor install publish push
major-p: major install publish push

install:
	poetry install

publish:
	poetry publish --build

patch:
	bump2version patch

minor:
	bump2version minor

major:
	bump2version major

push:
	git push origin master

# yapf:
# 	poetry run yapf -i -vv **/*.py

.PHONY: *