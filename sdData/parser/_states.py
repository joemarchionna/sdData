from sdData.parser._stateEvent import StateEvent
from sdData.parser._stateName import StateName
from sdData.parser._stateResponse import StateResponse
import re


class _baseState(object):
    def __init__(self, context) -> None:
        self.name = None
        self.context = context

    def handleLine(self, fileLine: str):
        raise Exception("This Must Be Overridden!")

    def _getFieldName(self, fileLine) -> str:
        nameMatch = re.match("> +<(?P<prop>.+)>", fileLine)
        if nameMatch:
            return nameMatch.group("prop")
        return None

    def _isEndOfRecord(self, fileLine) -> bool:
        dsc = fileLine.count("$")
        return (dsc >= 2) and (dsc <= 5)


class StructureState(_baseState):
    def __init__(self, context) -> None:
        super().__init__(context)
        self.name = StateName.STRUCTURE

    def handleLine(self, fileLine: str):
        self.context.currentRecord.mol.append(fileLine)
        endMatch = re.match("M *END", fileLine)
        if endMatch:
            return StateResponse(StateEvent.STRUCTURE_END)
        if self._isEndOfRecord(fileLine):
            # add the end of structure line - you shouldn't get to this point if properly formed
            self.context.currentRecord.mol.append("M  END")
            return StateResponse(StateEvent.RECORD_END)
        return StateResponse()


class FieldNameState(_baseState):
    def __init__(self, context) -> None:
        super().__init__(context)
        self.name = StateName.FIELD_NAME

    def handleLine(self, fileLine: str):
        if not fileLine:
            return StateResponse()
        if self._isEndOfRecord(fileLine):
            return StateResponse(StateEvent.RECORD_END)
        fieldName = self._getFieldName(fileLine)
        if fieldName:
            if fieldName not in self.context.metaKeys:
                self.context.metaKeys.append(fieldName)
            return StateResponse(StateEvent.PARSED_FIELD_NAME, txt=fieldName)
        raise Exception("I shouldn't be here :-(")


class FieldValueState(_baseState):
    def __init__(self, context, fieldName: str) -> None:
        super().__init__(context)
        self.name = StateName.FIELD_VALUE
        self.fieldName = fieldName
        self.fieldValue = []

    def handleLine(self, fileLine: str):
        if not fileLine:
            self.context.currentRecord.meta[self.fieldName] = self.fieldValue
            return StateResponse(StateEvent.BLANK_LINE)
        if self._isEndOfRecord(fileLine):
            self.context.currentRecord.meta[self.fieldName] = self.fieldValue
            return StateResponse(StateEvent.RECORD_END)
        newFieldName = self._getFieldName(fileLine)
        if newFieldName:
            self.context.currentRecord.meta[self.fieldName] = self.fieldValue
            return StateResponse(StateEvent.PARSED_FIELD_NAME, txt=newFieldName)
        self.fieldValue.append(fileLine)
        return StateResponse()
