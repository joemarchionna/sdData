from sdData.structure import Structure
from sdData.exceptions import SdParameterException
from sdData.helpers.fileSd import openFile, saveFile
import logging


class SdFile(object):
    def __init__(self, logName: str) -> None:
        self.logger = logging.getLogger(logName)
        self.records = []
        self.fn = None

    def getRecords(self)->list[Structure]:
        return self.records

    def count(self):
        return len(self.records)

    def open(self, filename: str):
        self.records = openFile(loggerName=self.logger.name, filename=filename)
        self.fn = filename

    def save(self, filename: str = None):
        fn = self._getFilename(filename)
        saveFile(fn, self.records)

    def add(self, sdStructure: Structure):
        if not isinstance(sdStructure, Structure):
            raise SdParameterException("sdStructure Parameter Must Be Of Type 'sdData.Structure'")
        self.records.append(sdStructure)

    def _getFilename(self, filename: str, isJson: bool = False) -> str:
        msg = None
        if not self.records:
            msg = "No SD Records Exist"
        if not filename and not self.fn:
            msg = "No File Name Defined"
        if isJson and not filename.endswith(".json"):
            msg = "Saving To Json But File Name Is Not .json"
        if msg:
            msg = "Dump/Save Failed: " + msg
            self.logger.error(msg)
            raise SdParameterException(msg)
        if filename:
            self.fn = filename
        return self.fn
