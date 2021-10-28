from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://www.gexf.net/1.2draft"


@dataclass
class Parent:
    class Meta:
        name = "parent"
        namespace = "http://www.gexf.net/1.2draft"

    for_value: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "name": "for",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ParentsContent:
    class Meta:
        name = "parents-content"

    parent: List[Parent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.gexf.net/1.2draft",
        }
    )
