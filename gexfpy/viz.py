from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime
from .dynamics import SpellsContent

__NAMESPACE__ = "http://www.gexf.net/1.2draft/viz"


class EdgeShapeType(Enum):
    SOLID = "solid"
    DOTTED = "dotted"
    DASHED = "dashed"
    DOUBLE = "double"


class NodeShapeType(Enum):
    DISC = "disc"
    SQUARE = "square"
    TRIANGLE = "triangle"
    DIAMOND = "diamond"
    IMAGE = "image"


@dataclass
class Spells(SpellsContent):
    class Meta:
        name = "spells"
        namespace = "http://www.gexf.net/1.2draft/viz"


@dataclass
class ColorContent:
    class Meta:
        name = "color-content"

    spells: Optional[Spells] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft/viz",
        }
    )
    r: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_inclusive": 255,
        }
    )
    g: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_inclusive": 255,
        }
    )
    b: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_inclusive": 255,
        }
    )
    a: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
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
class EdgeShapeContent:
    class Meta:
        name = "edge-shape-content"

    spells: Optional[Spells] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft/viz",
        }
    )
    value: Optional[EdgeShapeType] = field(
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


@dataclass
class NodeShapeContent:
    class Meta:
        name = "node-shape-content"

    spells: Optional[Spells] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft/viz",
        }
    )
    value: Optional[NodeShapeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uri: Optional[str] = field(
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
class PositionContent:
    class Meta:
        name = "position-content"

    spells: Optional[Spells] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft/viz",
        }
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    z: Optional[float] = field(
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


@dataclass
class SizeContent:
    class Meta:
        name = "size-content"

    spells: Optional[Spells] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft/viz",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
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
class ThicknessContent:
    class Meta:
        name = "thickness-content"

    spells: Optional[Spells] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft/viz",
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
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
