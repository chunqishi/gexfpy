from gexfpy import parse_string, stringify

gexf_12_s = '''
<?xml version="1.0" encoding="UTF-8"?>
<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">
    <graph mode="static" defaultedgetype="directed">
        <nodes>
            <node id="0" label="Hello" />
            <node id="1" label="Word" />
        </nodes>
        <edges>
            <edge id="0" source="0" target="1" />
        </edges>
    </graph>
</gexf>
'''


def test_parse():
    gexf_12 = parse_string(gexf_12_s)

    assert len(gexf_12.graph.nodes[0].node) == 2
    assert len(gexf_12.graph.edges[0].edge) == 1


def test_stringify():
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
    assert "255" in s


if __name__ == "__main__":
    test_parse()
    test_stringify()
