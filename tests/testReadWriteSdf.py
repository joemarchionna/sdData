from vrglTest.loggingTestCase import LoggingTestCase, LOGGER_NAME
from tests import TEST_WRITE_DIR
from sdData.sdFile import SdFile
import os, pathlib


class TestReadWriteSdf(LoggingTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        pathlib.Path(TEST_WRITE_DIR).mkdir(parents=True, exist_ok=True)

    def test_a_read(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd01.sdf")
        self.assertEqual(2, sdf.count())
        fn = "{}/sd01.sdf".format(TEST_WRITE_DIR)
        sdf.save(filename=fn)
        self.assertTrue(os.path.exists(fn))

    def test_b_read(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd02.sdf")
        self.assertEqual(3, sdf.count())
        self.assertFalse(sdf.records[1].meta["Formula"])
        fn = "{}/sd02.sdf".format(TEST_WRITE_DIR)
        sdf.save(filename=fn)
        self.assertTrue(os.path.exists(fn))

    def test_c_read(self):
        sdf = SdFile(logName=LOGGER_NAME)
        sdf.open(filename="tests/testFiles/sd03.sdf")
        self.assertEqual(3, sdf.count())
        self.assertFalse(sdf.records[0].meta)
        fn = "{}/sd03.sdf".format(TEST_WRITE_DIR)
        sdf.save(filename=fn)
        self.assertTrue(os.path.exists(fn))
