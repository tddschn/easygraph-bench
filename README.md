# easygraph-bench

[![benchmark](https://github.com/tddschn/easygraph-bench/actions/workflows/bench.yaml/badge.svg?event=workflow_dispatch)](https://github.com/tddschn/easygraph-bench/actions/workflows/bench.yaml)

Benchmarking code that compares the performance of the 2 graph libraries [easygraph](https://github.com/easy-graph/Easy-Graph) (python & C++ binding) and [networkx](https://networkx.org).


- [easygraph-bench](#easygraph-bench)
  - [Benchmarking method](#benchmarking-method)
  - [Benchmarked methods](#benchmarked-methods)
  - [Run](#run)
    - [Run locally](#run-locally)
      - [Scripts usage](#scripts-usage)
      - [Run on a custom dataset](#run-on-a-custom-dataset)
    - [Run on GitHub Actions](#run-on-github-actions)
  - [Result visualization](#result-visualization)
  - [Datasets](#datasets)
  - [FAQ](#faq)
    - [Why do you repeat yourself by using `bench_*.py` scripts?](#why-do-you-repeat-yourself-by-using-bench_py-scripts)
  - [Results](#results)
    - [Results downloads](#results-downloads)
    - [Complete results](#complete-results)
      - [cheminformatics](#cheminformatics)
      - [bio](#bio)
      - [eco](#eco)
      - [pgp](#pgp)
      - [pgp_undirected](#pgp_undirected)
      - [enron](#enron)
      - [coauthorship](#coauthorship)

## Benchmarking method

[timeit.Timer.autorange](https://docs.python.org/3.10/library/timeit.html#timeit.Timer.autorange) is used to run the specified methods on the graph objects.

If the method returns a Generator, the result will be exhausted.

See [get_Timer_args()](https://github.com/tddschn/easygraph-bench/blob/69cc89889e39386f495b7fa07be3116443cc9356/utils.py#L191) for more details.
 
## Benchmarked methods

See [config.py](./config.py) for more details.

- clustering_methods: `["average_clustering", "clustering"]`  
    (`eg.average_clustering` vs `nx.average_clustering`, ...)
- shortest_path_methods: `[('Dijkstra', 'single_source_dijkstra_path')]`  
    (`eg.Dijkstra` vs `nx.single_source_dijkstra_path`)
<!-- - connected_components_methods: `[ "is_connected", "number_connected_components", "connected_components", ("connected_component_of_node", 'node_connected_component'), ]` -->
- connected_components_methods: `["is_biconnected", "biconnected_components"]`
- mst_methods: `['minimum_spanning_tree']`  
    C++ binding not supported for this method yet.

## Run

### Run locally

`python >= 3.9` is required.

You can run benchmarking on a single dataset with the `./bench_*.py` scripts,  
or run benchmarking on a set of datasets with the `./entrypoint_*.py` scripts.

<!-- - Run benchmarks on a single dataset  
    You can choose what method category to benchmark via `-G`. See [Scripts usage](#scripts-usage).
    - [./bench_cheminformatics.py](./bench_cheminformatics.py): Run benchmarks on the cheminfomatics dataset
    - [./bench_bio.py](./bench_bio.py): Run benchmarks on the bio dataset
    - [./bench_eco.py](./bench_eco.py): Run benchmarks on the eco dataset
    - [./bench_soc.py](./bench_soc.py): Run benchmarks on the soc dataset (WIP)
- Run benchmarks on all datasets  
    - [./bench.py](./bench.py): Run benchmarks on all datasets  
        You can choose what method category to benchmark via `-G`. See [Scripts usage](#scripts-usage).
- Deprecated  
    - [./archive/bench.py](./archive/bench.py):  
    Deprecated, modified and parameterized from [@coreturn](https://github.com/coreturn)'s benchmarking script.  
    Only run the methods once with and record the difference of the result of `time.time()` calls as the time spent.  
    Use the following scripts instead. -->

To run these scripts, you need to clone the repo and install the dependencies listed in requirements.txt.

As of 8/6/2022, wheel for `python-easygraph` is not available on PyPI, and you need to build it yourself and install the module.

For macOS users, you may try the following snippet to do that:

```bash
git clone https://github.com/easy-graph/Easy-Graph && cd Easy-Graph
brew install boost --build-from-source
brew install boost-python

[ -d 'build'] && rm -rf build/

# modify line below based on your machine configuration, don't copy and run verbatim!
# you may also need to install clang or clang++ if you haven't already.
python3 setup.py build_ext -l boost_python310 -L "/usr/local/Cellar/boost-python3/1.79.0/lib" -I "/usr/local/Cellar/boost/1.79.0/include"

python3 setup.py install
```

#### Scripts usage

```
$ ./bench_cheminfo.py --help

ENZYMES_g1: nodes: 37 edges: 84
usage: bench_cheminfo.py [-h] [-G {clustering,shortest-path,connected-components,mst} [{clustering,shortest-path,connected-components,mst} ...]] [-C]

EasyGraph & NetworkX side-by-side benchmarking

optional arguments:
  -h, --help            show this help message and exit
  -G {clustering,shortest-path,connected-components,mst} [{clustering,shortest-path,connected-components,mst} ...], --method-group {clustering,shortest-path,connected-components,mst} [{clustering,shortest-path,connected-components,mst} ...]
  -C, --skip-cpp-easygraph, --skip-ceg
                        Skip benchmarking cpp_easygraph methods (default: False)
```

#### Run on a custom dataset

See [./bench_cheminfo.py](./bench_cheminfo.py).

Modify the dataset loading function `load_cheminformatics` to load your own dataset.

### Run on GitHub Actions

Fork this repo, go to the Actions tab and click Run Workflow.

## Result visualization

`timeit` results are saved in json files, and `seaborn` is used to render and save the figures in the `images/` directory.

<!-- The figures look like this:
![](images-public/cheminfomatics/average_clustering.png) -->

See [Complete results](#complete-results).


## Datasets

See [dataset_loaders.py](./dataset_loaders.py) and [dataset](./dataset/) for details.

| Dataset Name    | nodes  | edges   | type                             | is_directed |
| --------------- | ------ | ------- | -------------------------------- | ----------- |
| cheminformatics | 37     | 84      | easygraph.classes.graph.Graph    | False       |
| bio             | 1458   | 1948    | easygraph.classes.graph.Graph    | False       |
| eco             | 1258   | 7619    | easygraph.classes.graph.Graph    | False       |
| pgp             | 39796  | 301498  | networkx.classes.digraph.DiGraph | True        |
| pgp_undirected  | 39796  | 197150  | networkx.classes.graph.Graph     | False       |
| enron           | 36692  | 367662  | networkx.classes.digraph.DiGraph | True        |
| amazon          | 262111 | 1234877 | networkx.classes.digraph.DiGraph | True        |
| coauthorship    | 402392 | 1234019 | networkx.classes.graph.Graph     | False       |

<!-- | pokec           | 1632803 | 30622564 | networkx.classes.digraph.DiGraph | True        |
| google          | 875713  | 5105039  | networkx.classes.digraph.DiGraph | True        | -->

## FAQ

### Why do you repeat yourself by using `bench_*.py` scripts?

Yeah, I know this is not DRY. But for the `timeit`-based benchmarking code to work,
`eg`, `nx` and the graph objects must be in the global scope, i.e. `__main__`. 

I don't know how to do that while sticking to the DRY principle. 

But if you know, please tell me. :)

## Results

<!-- - Machine: MacBookPro16,2 (Mid-2020 MacBook Pro, Intel i7-1068NG7 (8) @ 2.30GHz, 16GB RAM)
- OS: macOS Monterey 12.5 21G72 x86_64
- python: Python 3.10.5 | packaged by conda-forge | (main, Jun 14 2022, 07:03:09) [Clang 13.0.1 ] on darwin -->

The benchmarking were ran on Ubuntu 20.04 with GitHub Actions on [GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#cloud-hosts-used-by-github-hosted-runners)

Results were generated by running `./bench.py`. See also [bench.yaml](./.github/workflows/bench.yaml).

### Results downloads

You can download the benchmarking results on the [Releases](https://github.com/tddschn/easygraph-bench/releases) page.

### Complete results

Click on the triangles to see the results.  
The images may take sometime to load.

`avg_time == -1` means method not supported by graph type (`NetworkXNotImplemented` or `EasyGraphNotImplemented` exceptions thrown).

`avg_time == -10` means that the benchmarking of this method was timed out.

<!-- the markdown code below this line is auto generated by `./gen_results_markdown.py` -->

#### cheminformatics

ENZYMES_g1: nodes: 37 edges: 84

- <details>
  <summary>average_clustering</summary>
  
  ![](./images-public/cheminformatics/average_clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>clustering</summary>
  
  ![](./images-public/cheminformatics/clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>Dijkstra</summary>
  
  ![](./images-public/cheminformatics/Dijkstra.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>is_biconnected</summary>
  
  ![](./images-public/cheminformatics/is_biconnected.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>biconnected_components</summary>
  
  ![](./images-public/cheminformatics/biconnected_components.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>minimum_spanning_tree</summary>
  
  ![](./images-public/cheminformatics/minimum_spanning_tree.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>density</summary>
  
  ![](./images-public/cheminformatics/density.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


#### bio

bio-yeast: nodes: 1458 edges: 1948

- <details>
  <summary>average_clustering</summary>
  
  ![](./images-public/bio/average_clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>clustering</summary>
  
  ![](./images-public/bio/clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>Dijkstra</summary>
  
  ![](./images-public/bio/Dijkstra.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>is_biconnected</summary>
  
  ![](./images-public/bio/is_biconnected.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>biconnected_components</summary>
  
  ![](./images-public/bio/biconnected_components.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>minimum_spanning_tree</summary>
  
  ![](./images-public/bio/minimum_spanning_tree.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>density</summary>
  
  ![](./images-public/bio/density.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


#### eco

econ-mahindas: nodes: 1258 edges: 7619

- <details>
  <summary>average_clustering</summary>
  
  ![](./images-public/eco/average_clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>clustering</summary>
  
  ![](./images-public/eco/clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>Dijkstra</summary>
  
  ![](./images-public/eco/Dijkstra.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>is_biconnected</summary>
  
  ![](./images-public/eco/is_biconnected.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>biconnected_components</summary>
  
  ![](./images-public/eco/biconnected_components.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>minimum_spanning_tree</summary>
  
  ![](./images-public/eco/minimum_spanning_tree.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>density</summary>
  
  ![](./images-public/eco/density.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


#### pgp

pgp network of trust: nodes: 39796 edges: 301498

- <details>
  <summary>average_clustering</summary>
  
  ![](./images-public/pgp/average_clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>clustering</summary>
  
  ![](./images-public/pgp/clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>Dijkstra</summary>
  
  ![](./images-public/pgp/Dijkstra.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>is_biconnected</summary>
  
  ![](./images-public/pgp/is_biconnected.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>biconnected_components</summary>
  
  ![](./images-public/pgp/biconnected_components.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>minimum_spanning_tree</summary>
  
  ![](./images-public/pgp/minimum_spanning_tree.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>density</summary>
  
  ![](./images-public/pgp/density.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


#### pgp_undirected

pgp network of trust: nodes: 39796 edges: 197150

- <details>
  <summary>average_clustering</summary>
  
  ![](./images-public/pgp_undirected/average_clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>clustering</summary>
  
  ![](./images-public/pgp_undirected/clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>Dijkstra</summary>
  
  ![](./images-public/pgp_undirected/Dijkstra.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>is_biconnected</summary>
  
  ![](./images-public/pgp_undirected/is_biconnected.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>biconnected_components</summary>
  
  ![](./images-public/pgp_undirected/biconnected_components.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>minimum_spanning_tree</summary>
  
  ![](./images-public/pgp_undirected/minimum_spanning_tree.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>density</summary>
  
  ![](./images-public/pgp_undirected/density.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


#### enron

SNAP email-Enron dataset: nodes: 36692 edges: 367662

- <details>
  <summary>average_clustering</summary>
  
  ![](./images-public/enron/average_clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>clustering</summary>
  
  ![](./images-public/enron/clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>Dijkstra</summary>
  
  ![](./images-public/enron/Dijkstra.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>is_biconnected</summary>
  
  ![](./images-public/enron/is_biconnected.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>biconnected_components</summary>
  
  ![](./images-public/enron/biconnected_components.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>minimum_spanning_tree</summary>
  
  ![](./images-public/enron/minimum_spanning_tree.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>density</summary>
  
  ![](./images-public/enron/density.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>


#### coauthorship

Yang Chen's co-authorship network on Google Scholar: nodes: 402392 edges: 1234019

- <details>
  <summary>average_clustering</summary>
  
  ![](./images-public/coauthorship/average_clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>clustering</summary>
  
  ![](./images-public/coauthorship/clustering.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>Dijkstra</summary>
  
  ![](./images-public/coauthorship/Dijkstra.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>is_biconnected</summary>
  
  ![](./images-public/coauthorship/is_biconnected.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>biconnected_components</summary>
  
  ![](./images-public/coauthorship/biconnected_components.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>minimum_spanning_tree</summary>
  
  ![](./images-public/coauthorship/minimum_spanning_tree.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>

- <details>
  <summary>density</summary>
  
  ![](./images-public/coauthorship/density.png)
  <!-- ## Heading
  1. A numbered
  2. list
     * With some
     * Sub bullets -->
<!-- Two important rules:

Make sure you have an empty line after the closing </summary> tag, otherwise the markdown/code blocks won't show correctly.
Make sure you have an empty line after the closing </details> tag if you have multiple collapsible sections. -->
</details>
