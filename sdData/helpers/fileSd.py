from sdData.constants import SD_META_PREFIX, SD_RECORD_TERMINATOR, LINE_TERMINATOR
from sdData.parser.textParser import TextParser
from sdData.structure import Structure


def readFile(loggerName: str, reader, recordCompleteCallback=None) -> list[Structure]:
    parser = TextParser(loggerName)
    parser.subscribe(recordCompleteCallback)
    l = reader.readline()
    while l:
        parser.parseLine(l)
        l = reader.readline()
    return parser.records


def openFile(loggerName: str, filename: str) -> list[Structure]:
    with open(filename) as fr:
        return readFile(loggerName, fr)


def _getMetaLines(metaKey: str, metaValue: list, metaPrefix: str) -> list:
    lines = []
    lines.append("{}{}>".format(metaPrefix, metaKey))
    lines.extend(metaValue)
    lines.append("")
    return lines


def _getRecordLines(sdStructure: Structure, metaPrefix: str) -> list:
    lines = []
    lines.extend(sdStructure.mol)
    lines.append("")
    for k, v in sdStructure.meta.items():
        lines.extend(_getMetaLines(k, v, metaPrefix))
    return lines


def writeStructure(
    fileWriter,
    sdStructure: Structure,
    lineTerm: str = LINE_TERMINATOR,
    metaPrefix: str = SD_META_PREFIX,
    recordTerm: str = SD_RECORD_TERMINATOR,
):
    lines = _getRecordLines(sdStructure, metaPrefix)
    for l in lines:
        fileWriter.write("{}{}".format(l, lineTerm))
    fileWriter.write("{}{}".format(recordTerm, lineTerm))


def saveFile(
    filename: str,
    sdStructures: list,
    lineTerm: str = LINE_TERMINATOR,
    metaPrefix: str = SD_META_PREFIX,
    recordTerm: str = SD_RECORD_TERMINATOR,
):
    with open(filename, "w") as fw:
        for sd in sdStructures:
            writeStructure(fw, sd, lineTerm, metaPrefix, recordTerm)
