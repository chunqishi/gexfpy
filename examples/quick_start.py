from gexfpy import parse, stringify

'''
Example 1: parse gexf file into python object
'''
sbu_310 = parse('sbu_310.gexf')
print('graph sbu_310 nodes number =', sbu_310.graph.nodes[0].count)


'''
Example 2: stringify python object into xml string
'''
from gexfpy import Gexf, Graph, Nodes, Edges, Node, Edge, Color

gexf = Gexf()
gexf.graph = Graph()
gexf.graph.nodes = [Nodes(node=[Node(id=1, label="node 1",
                                     color=[Color(r=255, g=0, b=0)]),
                                Node(id=2, label="node 2"),
                                Node(id=3, label="node 3")],
                          count=3)]
gexf.graph.edges = [Edges(edge=[Edge(source=1, target=2, label="edge 1"),
                                Edge(source=2, target=3, label="edge 1")],
                          count=2)]
s = stringify(gexf)
print(s)
