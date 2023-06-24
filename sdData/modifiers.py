from sdData.structure import Structure
from sdData.sdFile import SdFile


def keepMeta(record: Structure, keys: list):
    metaKeys = [str(x) for x in record.meta.keys()]
    for k in metaKeys:
        if k not in keys:
            record.meta.pop(k)


def removeMeta(record: Structure, keys: list):
    metaKeys = [str(x) for x in record.meta.keys()]
    for k in metaKeys:
        if k in keys:
            record.meta.pop(k)


def divideIntoSds(sdf: SdFile, maxLength) -> list[SdFile]:
    sdLists = divideInto(records=sdf.records, maxLength=maxLength)
    files = []
    for l in sdLists:
        s = SdFile(sdf.logger.name)
        s.records = l
        files.append(s)
    return files


def divideInto(records, maxLength):
    """returns a mutiple list of length maxLength of a list: [ [0..maxLength], [0..maxLength], ... ]"""
    # looping till length l
    for i in range(0, len(records), maxLength):
        yield records[i : i + maxLength]


def validateStructure(record: Structure):
    errors = []
    lineCount = len(record.mol)
    if lineCount > 4:
        # check if there's too many lines in the header
        ss = record.mol[3].strip()
        if len(ss) == 0:
            errors.append("No Data On Line 4 (1-N): This Is Typically Because Of An Extra Header Line")
        values = ss.split(" ")
        if values:
            if values[0].startswith("M"):
                errors.append("Structure Data On Line 4 (1-N): This Is Typically Due To Too Few Header Lines")
            elif not values[0].isnumeric():
                errors.append("The Data On Line 4 (1-N) Is Not Numeric: This Is Typically Because Of An Extra Header Line")
