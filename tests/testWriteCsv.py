from vrglTest.loggingTestCase import LoggingTestCase, LOGGER_NAME
from tests import TEST_WRITE_DIR
from sdData.sdFile import SdFile
from sdData.helpers.csvSd import saveCsv
import os, pathlib


class TestWriteCsv(LoggingTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        pathlib.Path(TEST_WRITE_DIR).mkdir(parents=True, exist_ok=True)

    def test_a_all(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd01.sdf")
        fn = "{}/sd01.csv".format(TEST_WRITE_DIR)
        saveCsv(filename=fn, sdStructures=sdf.records)
        self.assertTrue(os.path.exists(fn))

    def test_b_partial(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd01.sdf")
        fn = "{}/sd01_partial.csv".format(TEST_WRITE_DIR)
        saveCsv(filename=fn, sdStructures=sdf.records, metaFieldNames=["ID", "sourceOrg"])
        self.assertTrue(os.path.exists(fn))
