from enum import Enum


class StateEvent(Enum):
    NONE = 0
    STRUCTURE_END = 20
    PARSED_FIELD_NAME = 30
    BLANK_LINE = 50
    RECORD_END = 100
