from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path
from io import StringIO

from xsdata.formats.dataclass.serializers.config import SerializerConfig

from .gexf import Gexf


def parse_string(xml_as_str: str) -> Gexf:
    parser = XmlParser()
    gexfobj = parser.from_string(xml_as_str, Gexf)
    return gexfobj


def parse(gexfpath: str) -> Gexf:
    xml_string = Path(gexfpath).read_text()
    parser = XmlParser()
    gexfobj = parser.from_string(xml_string, Gexf)
    return gexfobj


def xmlserialize(gexf: Gexf, gexfpath: str, pretty_print: bool = True):
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=pretty_print))
    with Path(gexfpath).open(mode='w') as fid:
        serializer.write(fid, gexf)


def stringify(gexf: Gexf, pretty_print: bool = True) -> str:
    sio = StringIO()
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=pretty_print))
    serializer.write(sio, gexf)
    return sio.getvalue()
