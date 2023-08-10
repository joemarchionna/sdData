from sdData.constants import MOL_JSON_KEY, MOL_JSON_LINE_TERMINATOR
from sdData.structure import Structure
import json


def _getStructureRecord(jsonStructure: dict, jsonLineDelim: str) -> Structure:
    s = Structure()
    s.mol = jsonStructure[MOL_JSON_KEY].split(jsonLineDelim)
    jsonStructure.pop(MOL_JSON_KEY)
    s.meta.update(jsonStructure)
    return s


def loadStr(txt: str, jsonLineDelim: str = MOL_JSON_LINE_TERMINATOR) -> list[Structure]:
    records = []
    jsonData = json.loads(txt)
    for r in jsonData:
        records.append(_getStructureRecord(r, jsonLineDelim))
    return records


def loadFile(reader, jsonLineDelim: str = MOL_JSON_LINE_TERMINATOR) -> list[Structure]:
    records = []
    jsonData = json.load(reader)
    for r in jsonData:
        records.append(_getStructureRecord(r, jsonLineDelim))
    return records


def _getJsonRecord(sdStructure: Structure, jsonLineDelim: str):
    d = {}
    d[MOL_JSON_KEY] = jsonLineDelim.join(sdStructure.mol)
    d.update(sdStructure.meta)
    return d


def dumpStr(
    sdStructures: list,
    indent: int = 4,
    jsonLineDelim: str = MOL_JSON_LINE_TERMINATOR,
) -> str:
    jsonRecords = []
    for sd in sdStructures:
        jsonRecords.append(_getJsonRecord(sd, jsonLineDelim))
    return json.dumps(jsonRecords, indent=indent)


def dumpFile(sdStructures: list, writer, indent: int = 4, jsonLineDelim: str = MOL_JSON_LINE_TERMINATOR):
    jsonRecords = []
    for sd in sdStructures:
        jsonRecords.append(_getJsonRecord(sd, jsonLineDelim))
    json.dump(jsonRecords, writer, indent=indent)
