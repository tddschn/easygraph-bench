#!/usr/bin/env bash

DIR_NAME='er-paper-{{ date_s }}'

{% for config in nodes_and_edges_list %}
./gen_er.py --er-dataset-dir-name "${DIR_NAME}" --nodes '{{ config.nodes }}' --edges '{{ config.edges }}' {{ extra_args }}
{% endfor %}