import sys, pprint

from xml.dom import minidom
import os, datetime

import matplotlib.cm as cm
import matplotlib as matplotlib


def color_map_color(value, cmap_name='Paired', vmin=0, vmax=1):
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    cmap = cm.get_cmap(cmap_name)
    rgb = cmap(norm(abs(value)))[:3]  # will return rgba, we take only first 3 so we get rgb
    return [round(x * 255) for x in rgb]


doc = minidom.Document()

gexf = doc.createElement('gexf')
gexf.setAttribute('xmlns', 'http://www.gexf.net/1.2draft')
gexf.setAttribute('version', '1.2')

doc.appendChild(gexf)

meta = doc.createElement('meta')
meta.setAttribute('lastmodifieddate', f'{datetime.datetime.now():%Y-%m-%d}')
gexf.appendChild(meta)

creator = doc.createElement('creator')
creator.appendChild(doc.createTextNode('Chunqi Shi'))
meta.appendChild(creator)
description = doc.createElement('description')
description.appendChild(doc.createTextNode('sbustreamspot-data display in gexf by gephi'))
meta.appendChild(description)

graph = doc.createElement('graph')
graph.setAttribute('mode', f'static')
graph.setAttribute('defaultedgetype', f'undirected')
gexf.appendChild(graph)

import pandas as pd

df = pd.read_csv('graph_edges.csv')

node_ids = list(set(list(df['source-id'].unique().tolist()) + list(df['destination-id'].unique().tolist())))
node_types = list(set(list(df['source-type'].unique().tolist()) + list(df['destination-type'].unique().tolist())))

node_type_dict = dict(zip(df['source-id'], df['source-type']))
node_type_dict.update(
    dict(zip(df['destination-id'], df['destination-type'])))
node_type_color_dict = dict(zip(node_types, [color_map_color(i / len(node_types)) for i in range(len(node_types))]))

num_nodes = len(node_ids)

nodes = doc.createElement('nodes')
nodes.setAttribute('count', f'{num_nodes}')
graph.appendChild(nodes)

for i in range(num_nodes):
    nodei = doc.createElement('node')
    nodei.setAttribute('id', f'{node_ids[i]}')
    nodei.setAttribute('label', f'{node_type_dict[node_ids[i]]}')
    attvalues = doc.createElement('attvalues')
    color = doc.createElement('color')
    r, g, b = node_type_color_dict[node_type_dict[node_ids[i]]]
    color.setAttribute('r', f'{r}')
    color.setAttribute('g', f'{g}')
    color.setAttribute('b', f'{b}')
    # size = doc.createElement('size')
    nodei.appendChild(color)
    nodei.appendChild(attvalues)
    nodes.appendChild(nodei)

num_edges = len(df)

edges = doc.createElement('edges')
edges.setAttribute('count', f'{num_edges}')
graph.appendChild(edges)

for i in range(num_edges):
    row = df.iloc[i]
    edgei = doc.createElement('edge')
    edgei.setAttribute('id', f'{i}')
    edgei.setAttribute('source', f'{row["source-id"]}')
    edgei.setAttribute('target', f'{row["destination-id"]}')
    edgei.setAttribute('type', f'undirected')
    edgei.setAttribute('label', f'{row["edge-type"]}')
    edgei.setAttribute('weight', f'1')

    graph_label = row['graph-id'] // 100
    r, g, b = color_map_color(graph_label / 6)
    color = doc.createElement('color')
    color.setAttribute('r', f'{r}')
    color.setAttribute('g', f'{g}')
    color.setAttribute('b', f'{b}')
    edgei.appendChild(color)

    edges.appendChild(edgei)

xml_str = doc.toprettyxml(indent="\t")
save_path_file = f"gexf_minidom.gexf"
with open(save_path_file, "w") as f:
    f.write(xml_str)