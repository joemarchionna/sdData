from sdData.parser._states import StructureState, FieldNameState, FieldValueState
from sdData.parser._stateEvent import StateEvent
from sdData.parser._stateName import StateName

STATE_MAP = {
    "originatingState": {"event": "nextState"},
    StateName.STRUCTURE: {StateEvent.STRUCTURE_END: FieldNameState, StateEvent.RECORD_END: StructureState},
    StateName.FIELD_NAME: {StateEvent.PARSED_FIELD_NAME: FieldValueState, StateEvent.RECORD_END: StructureState},
    StateName.FIELD_VALUE: {
        StateEvent.BLANK_LINE: FieldNameState,
        StateEvent.PARSED_FIELD_NAME: FieldValueState,
        StateEvent.RECORD_END: StructureState,
    },
}
