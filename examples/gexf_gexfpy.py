import sys, pprint

from xml.dom import minidom
import os, datetime

import matplotlib.cm as cm
import matplotlib as matplotlib
from gexfpy import Gexf, Graph, Node, Nodes, Color, Edges, Edge, EdgetypeType, xmlserialize


def color_map_color(value, cmap_name='Paired', vmin=0, vmax=1):
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    cmap = cm.get_cmap(cmap_name)  # PiYG
    rgb = cmap(norm(abs(value)))[:3]  # will return rgba, we take only first 3 so we get rgb
    return [round(x * 255) for x in rgb]


import pandas as pd

df = pd.read_csv('graph_edges.csv')

node_ids = list(set(list(df['source-id'].unique().tolist()) + list(df['destination-id'].unique().tolist())))
node_types = list(set(list(df['source-type'].unique().tolist()) + list(df['destination-type'].unique().tolist())))

node_type_dict = dict(zip(df['source-id'], df['source-type']))
node_type_dict.update(
    dict(zip(df['destination-id'], df['destination-type'])))
node_type_color_dict = dict(zip(node_types, [color_map_color(i / len(node_types)) for i in range(len(node_types))]))

num_nodes = len(node_ids)

node_list = []
for i in range(num_nodes):
    r, g, b = node_type_color_dict[node_type_dict[node_ids[i]]]
    nodei = Node(id=f'{node_ids[i]}',
                 label=f'{node_type_dict[node_ids[i]]}',
                 color=[Color(r=r, g=g, b=b)])
    node_list.append(nodei)

num_edges = len(df)

edge_list = []
for i in range(num_edges):
    row = df.iloc[i]

    graph_label = row['graph-id'] // 100
    r, g, b = color_map_color(graph_label / 6)

    edgei = Edge(id=f'{i}',
                 source=f'{row["source-id"]}',
                 target=f'{row["destination-id"]}',
                 type=EdgetypeType.UNDIRECTED,
                 label=f'{row["edge-type"]}',
                 weight=1,
                 color=[Color(r=r, g=g, b=b)])
    edge_list.append(edgei)

print(node_list)
print(edge_list)

gexf = Gexf(graph=Graph(nodes=[Nodes(node=node_list, count=len(node_list))],
                        edges=[Edges(edge=edge_list, count=len(edge_list))]))

save_path_file = f"gexf_gexfpy.gexf"

xmlserialize(gexf, save_path_file)
