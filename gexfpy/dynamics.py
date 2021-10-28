from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "http://www.gexf.net/1.2draft"


@dataclass
class Spell:
    class Meta:
        name = "spell"
        namespace = "http://www.gexf.net/1.2draft"

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


class TimeformatType(Enum):
    INTEGER = "integer"
    DOUBLE = "double"
    DATE = "date"
    DATE_TIME = "dateTime"


@dataclass
class SpellsContent:
    class Meta:
        name = "spells-content"

    spell: List[Spell] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
            "min_occurs": 1,
        }
    )
