from enum import Enum


class ModeType(Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"


class AttrtypeType(Enum):
    INTEGER = "integer"
    LONG = "long"
    DOUBLE = "double"
    FLOAT = "float"
    BOOLEAN = "boolean"
    LISTSTRING = "liststring"
    STRING = "string"
    ANY_URI = "anyURI"


class DefaultedgetypeType(Enum):
    """
    Datatypes.
    """
    DIRECTED = "directed"
    UNDIRECTED = "undirected"
    MUTUAL = "mutual"


class EdgetypeType(Enum):
    DIRECTED = "directed"
    UNDIRECTED = "undirected"
    MUTUAL = "mutual"


class GexfContentVersion(Enum):
    VALUE_1_2 = "1.2"


class IdtypeType(Enum):
    INTEGER = "integer"
    STRING = "string"
