def parseMolTxt(molTxt: str, lineDelimiter: str) -> list[str]:
    molLines = molTxt.split(lineDelimiter)
    return molLines
