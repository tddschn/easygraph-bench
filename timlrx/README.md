# Benchmarking EasyGraph against other libraries in `timlrx`'s benchmark

- `timlrx`'s code repository: https://github.com/timlrx/graph-benchmarks
  
## Methodology

There're multiple largely duplicated benchmarking scripts in `timlrx`'s repository,
so I extracted the parts specific to each library with `semgrep` (see [`semgrep_extract.sh`](./semgrep_extract.sh)) and saved them to [`graph-benchmarking-code.json`](./graph-benchmark-code.json).

Then I added code for EasyGraph to that file, generated benchmarking scripts for each library with this Jinja Template [`profile_template.jinja.py`](../templates/profile_template.jinja.py). 

## Run the benchmark

Clone this repository, install required packages, set up sqlite databases to store bench results, and run

```bash
./profile_entrypoint.sh
```