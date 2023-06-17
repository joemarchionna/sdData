from sdData.parser._map import STATE_MAP
from sdData.parser._states import StructureState
from sdData.parser._stateEvent import StateEvent
from sdData.structure import Structure
import logging


class TextParser(object):
    def __init__(self, loggerName: str) -> None:
        self.logger = logging.getLogger(loggerName)
        self.currentState = StructureState(self)
        self.currentRecord = Structure()
        self.records = []

    def parseLine(self, txt: str):
        resp = self.currentState.handleLine(txt.rstrip())
        if resp.event.value > 0:
            self.logger.debug("Current State: {}, State Response: {}".format(self.currentState.name, resp))
            # change states
            nextState = STATE_MAP[self.currentState.name][resp.event]
            if resp.txt:
                self.currentState = nextState(self, resp.txt)
            else:
                self.currentState = nextState(self)

            # change to a new record
            if resp.event == StateEvent.RECORD_END:
                self.records.append(self.currentRecord)
                self.currentRecord = Structure()
