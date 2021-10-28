![GEXFpy](./docs/source/_static/logo.png)
===


GEXFpy is a python wrapper for [Gexf XML version 1.2](http://www.gexf.net/1.2draft) . 

We provide 2 ways to use it:

- **Parse Gexf XML as Graph Python Object**:  read gexf version 1.2 xml file into python as Gexf python object.
- **Serialize  Graph Python Object into Gexf XML**: create python object Gexf instance and serialize this object into gexf version 1.2 xml file.

## Getting Started

### Requirements and Installation

- Python version >= 3.8
- xsdata version == 21.9


```bash
pip install gexfpy
```

Install from source via:

```bash
pip install git+https://github.com/chunqishi/gexfpy.git
```

Or clone the repository and install with the following commands:

```bash
git clone git@github.com:chunqishi/gexfpy.git
cd gexfpy
pip install -e .
```

## Usage

### API Usage

You can run all kinds of experiments through GEXFpy APIs. 
A quickstart example can be found in the [quick_start.py](https://github.com/chunqishi/gexfpy/tree/master/examples/quick_start.py). More examples are provided in the [examples/](https://github.com/chunqishi/gexfpy/tree/master/examples/).

```python
from gexfpy import parse

# basic usage parse file
sbu_310 = parse('sbu_310.gexf')
print('graph sbu_310 nodes number =', len(sbu_310.graph.nodes[0].node))


# serialize Gexf object into xml string
from gexfpy import stringify
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
```


Check the `documentation <https://gexfpy.readthedocs.io>`_ for more
✨✨✨


## Changelog
### Version 0.1.1 2021-10-30
It works only for gexf version 1.2 draft


