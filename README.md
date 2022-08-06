# easygraph-bench

Benchmarking code that compares the performance of the 2 graph libraries easygraph (python & C++ binding) and networkx.

- [easygraph-bench](#easygraph-bench)
  - [Benchmarking method](#benchmarking-method)
  - [Benchmarked methods](#benchmarked-methods)
  - [Run locally](#run-locally)
  - [Datasets](#datasets)

## Benchmarking method

[timeit.Timer.autorange](https://docs.python.org/3.10/library/timeit.html#timeit.Timer.autorange) is used to run the specified methods on the graph objects.

If the method returns a Generator, the result will be exhausted.

See [get_Timer_args()](https://github.com/tddschn/easygraph-bench/blob/69cc89889e39386f495b7fa07be3116443cc9356/utils.py#L191)
 
## Benchmarked methods

See [config.py](./config.py) for more details.

- clustering_methods: `["average_clustering", "clustering"]`
- shortest_path_methods: `[('Dijkstra', 'single_source_dijkstra_path')]`
- connected_components_methods: `[ "is_connected", "number_connected_components", "connected_components", ("connected_component_of_node", 'node_connected_component'), ]`
- mst_methods: `['minimum_spanning_tree']`

## Run locally
- [./bench_cheminfo.py](./bench_cheminfo.py): Run benchmarks on the cheminfomatics dataset
- [./bench_bio.py](./bench_bio.py): Run benchmarks on the bio dataset
- [./bench_eco.py](./bench_eco.py): Run benchmarks on the eco dataset
- [./bench_soc.py](./bench_soc.py): Run benchmarks on the soc dataset

To run these scripts, you need to clone the repo and install the dependencies listed in requirements.txt.

As of 8/6/2022, wheel for `python-easygraph` is not available on PyPI, and you need to build it yourself and install the module.

For macOS users, you may try the following snippet to do that:

```bash
git clone https://github.com/easy-graph/Easy-Graph && cd Easy-Graph
brew install boost boost-python

[ -d 'build'] && rm -rf build/
python3 setup.py build_ext -l boost_python39 -L "/usr/local/Cellar/boost-python3/1.79.0/lib" -I "/usr/local/Cellar/boost/1.79.0/include"
python3 setup.py install
```

## Datasets

See [dataset_loaders.py](./dataset_loaders.py).