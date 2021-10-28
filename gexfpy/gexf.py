from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.gexf.net/1.2draft"

from .datatypes import (
    AttrtypeType,
    ModeType,
    EdgetypeType,
    DefaultedgetypeType,
    IdtypeType,
    GexfContentVersion
)

from .dynamics import (
    SpellsContent,
    TimeformatType,
)

from .phylogenics import ParentsContent
from .viz import (
    ColorContent,
    EdgeShapeContent,
    NodeShapeContent,
    PositionContent,
    SizeContent,
    ThicknessContent,
)


@dataclass
class Attvalue:
    class Meta:
        name = "attvalue"
        namespace = "http://www.gexf.net/1.2draft"

    for_value: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "name": "for",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    start: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    startopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    end: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    endopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class ClassType(Enum):
    NODE = "node"
    EDGE = "edge"


@dataclass
class Default:
    class Meta:
        name = "default"
        namespace = "http://www.gexf.net/1.2draft"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Options:
    class Meta:
        name = "options"
        namespace = "http://www.gexf.net/1.2draft"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class AttributeContent:
    class Meta:
        name = "attribute-content"

    default: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    options: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    id: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[AttrtypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AttvaluesContent:
    class Meta:
        name = "attvalues-content"

    attvalue: List[Attvalue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )


@dataclass
class Color(ColorContent):
    class Meta:
        name = "color"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Parents(ParentsContent):
    class Meta:
        name = "parents"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Position(PositionContent):
    class Meta:
        name = "position"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Size(SizeContent):
    class Meta:
        name = "size"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Spells(SpellsContent):
    class Meta:
        name = "spells"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Thickness(ThicknessContent):
    class Meta:
        name = "thickness"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Attribute(AttributeContent):
    class Meta:
        name = "attribute"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Attvalues(AttvaluesContent):
    class Meta:
        name = "attvalues"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class AttributesContent:
    class Meta:
        name = "attributes-content"

    attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    class_value: Optional[ClassType] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "required": True,
        }
    )
    mode: Optional[ModeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    startopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    end: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    endopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EdgeContent:
    class Meta:
        name = "edge-content"

    attvalues: List[Attvalues] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    spells: List[Spells] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    color: List[Color] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    thickness: List[Thickness] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    shape: List[EdgeShapeContent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    start: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    startopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    end: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    endopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[EdgetypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    source: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    target: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    weight: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NodeContent:
    class Meta:
        name = "node-content"

    attvalues: List[Attvalues] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    spells: List[Spells] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    nodes: List["Nodes"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    edges: List["Edges"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    parents: List[Parents] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    color: List[Color] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    position: List[Position] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    size: List[Size] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    shape: List[NodeShapeContent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    start: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    startopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    end: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    endopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    pid: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Attributes(AttributesContent):
    class Meta:
        name = "attributes"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class GraphContent:
    class Meta:
        name = "graph-content"

    attributes: List[Attributes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    nodes: List["Nodes"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    edges: List["Edges"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    timeformat: Optional[TimeformatType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    startopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    end: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    endopen: Optional[Union[int, float, XmlDate, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    defaultedgetype: Optional[DefaultedgetypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    idtype: Optional[IdtypeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mode: Optional[ModeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Creator:
    class Meta:
        name = "creator"
        namespace = "http://www.gexf.net/1.2draft"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Description:
    class Meta:
        name = "description"
        namespace = "http://www.gexf.net/1.2draft"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Keywords:
    class Meta:
        name = "keywords"
        namespace = "http://www.gexf.net/1.2draft"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class MetaContent:
    class Meta:
        name = "meta-content"

    creator: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    lastmodifieddate: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Edge(EdgeContent):
    class Meta:
        name = "edge"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Graph(GraphContent):
    class Meta:
        name = "graph"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class MetaType(MetaContent):
    class Meta:
        name = "meta"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Node(NodeContent):
    class Meta:
        name = "node"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class EdgesContent:
    class Meta:
        name = "edges-content"

    edge: List[Edge] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NodesContent:
    class Meta:
        name = "nodes-content"

    node: List[Node] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Edges(EdgesContent):
    class Meta:
        name = "edges"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class Nodes(NodesContent):
    class Meta:
        name = "nodes"
        namespace = "http://www.gexf.net/1.2draft"


@dataclass
class GexfContent:
    """
    Tree.
    """

    class Meta:
        name = "gexf-content"

    meta: Optional[MetaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
    graph: Optional[Graph] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
            "required": True,
        }
    )
    version: Optional[GexfContentVersion] = field(
        default=GexfContentVersion.VALUE_1_2,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    variant: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Gexf(GexfContent):
    class Meta:
        name = "gexf"
        namespace = "http://www.gexf.net/1.2draft"
