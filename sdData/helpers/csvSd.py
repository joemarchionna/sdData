from sdData.constants import ALL_FIELDS, LINE_TERMINATOR, CSV_DELIMITER, MULTI_LINE_DELIM
from sdData.structure import Structure


def writeCsv(
    fileWriter,
    sdStructure: Structure,
    metaFieldNames: list,
    delimiter: str = CSV_DELIMITER,
    multiLineDelim: str = MULTI_LINE_DELIM,
    lineTerm: str = LINE_TERMINATOR,
):
    addDelimiter = False
    for k in metaFieldNames:
        if addDelimiter:
            fileWriter.write(delimiter)
        vals = sdStructure.meta.get(k, [])
        fileWriter.write(multiLineDelim.join(vals))
        addDelimiter = True
    fileWriter.write(lineTerm)


def saveCsv(
    filename,
    sdStructures: list,
    metaFieldNames: list = [ALL_FIELDS],
    delimiter: str = CSV_DELIMITER,
    multiLineDelim: str = MULTI_LINE_DELIM,
    lineTerm: str = LINE_TERMINATOR,
):
    if metaFieldNames[0] == ALL_FIELDS:
        metaFieldNames = list(str(x) for x in sdStructures[0].meta.keys())
    with open(filename, "w") as fw:
        hdr = delimiter.join(metaFieldNames)
        fw.write("{}{}".format(hdr, lineTerm))
        for s in sdStructures:
            writeCsv(fw, s, metaFieldNames, delimiter, multiLineDelim, lineTerm)
