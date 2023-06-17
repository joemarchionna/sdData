from sdData.parser._stateEvent import StateEvent


class StateResponse(object):
    def __init__(self, event: StateEvent = StateEvent.NONE, processTxt: bool = False, txt: str = None) -> None:
        self.event = event
        self.processTxt = processTxt
        self.txt = txt

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Event: {}, Process Text: {}, Text: {}".format(self.event, self.processTxt, self.txt)
