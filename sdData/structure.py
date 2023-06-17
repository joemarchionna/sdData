from sdData.constants import LINE_TERMINATOR, MULTI_LINE_DELIM


class Structure(object):
    def __init__(self) -> None:
        self.mol = []
        self.meta = {}

    def getMolStr(self, lineTerm: str = LINE_TERMINATOR) -> str:
        return lineTerm.join(self.mol)

    def getMetadata(self, fieldName: str, multiLineDelim: str = MULTI_LINE_DELIM) -> str:
        vals = self.meta.get(fieldName, [])
        return multiLineDelim.join(vals)
