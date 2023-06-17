from enum import Enum


class StateName(Enum):
    STRUCTURE = 1
    FIELD_NAME = 2
    FIELD_VALUE = 3
    END_OF_RECORD = 10
