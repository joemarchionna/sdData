from vrglTest.loggingTestCase import LoggingTestCase, LOGGER_NAME
from tests import TEST_WRITE_DIR
from sdData.sdFile import SdFile
from sdData.helpers.jsonSd import dumpFile, loadFile
import os, pathlib


class TestWrite(LoggingTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        pathlib.Path(TEST_WRITE_DIR).mkdir(parents=True, exist_ok=True)

    def test_a_read(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd01.sdf")
        self.assertEqual(2, sdf.count())
        fn = "{}/sd01.json".format(TEST_WRITE_DIR)
        with open(fn, "w") as fw:
            dumpFile(sdf.records, fw)
        self.assertTrue(os.path.exists(fn))
        jsdf = SdFile(logName=LOGGER_NAME)
        with open(fn) as fr:
            jsdf.records = loadFile(fr)
        self.assertEqual(2, jsdf.count())

    def test_b_read(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd02.sdf")
        self.assertEqual(3, sdf.count())
        self.assertFalse(sdf.records[1].meta["Formula"])
        fn = "{}/sd02.json".format(TEST_WRITE_DIR)
        with open(fn, "w") as fw:
            dumpFile(sdf.records, fw)
        self.assertTrue(os.path.exists(fn))
        jsdf = SdFile(logName=LOGGER_NAME)
        with open(fn) as fr:
            jsdf.records = loadFile(fr)
        self.assertEqual(3, jsdf.count())

    def test_c_read(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd03.sdf")
        self.assertEqual(3, sdf.count())
        self.assertFalse(sdf.records[0].meta)
        fn = "{}/sd03.json".format(TEST_WRITE_DIR)
        with open(fn, "w") as fw:
            dumpFile(sdf.records, fw)
        self.assertTrue(os.path.exists(fn))
        jsdf = SdFile(logName=LOGGER_NAME)
        with open(fn) as fr:
            jsdf.records = loadFile(fr)
        self.assertEqual(3, jsdf.count())
