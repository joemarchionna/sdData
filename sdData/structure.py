from sdData.constants import LINE_TERMINATOR, MULTI_LINE_DELIM
from sdData.exceptions import SdParameterException


class Structure(object):
    def __init__(self) -> None:
        self.mol = []
        self.meta = {}

    def getMolStr(self, lineTerm: str = LINE_TERMINATOR) -> str:
        return lineTerm.join(self.mol)

    def getMetadata(self, fieldName: str, multiLineDelim: str = MULTI_LINE_DELIM) -> str:
        vals = self.meta.get(fieldName, [])
        return multiLineDelim.join(vals)

    def saveMetadata(self, fieldName: str, fieldValue):
        if not fieldName:
            raise SdParameterException("Structure Metadata Field Name Must Be Defined")
        if not isinstance(fieldValue, list):
            fieldValue = [fieldValue]
        self.meta[fieldName] = fieldValue
