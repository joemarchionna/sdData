from vrglTest.loggingTestCase import LoggingTestCase, LOGGER_NAME
from tests import TEST_WRITE_DIR
from sdData.helpers.txtSd import parseMolTxt
import pathlib
import json


class TestParseMol(LoggingTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        pathlib.Path(TEST_WRITE_DIR).mkdir(parents=True, exist_ok=True)

    def test_a_parse1(self):
        with open("tests/testFiles/sdTxt01.json") as fr:
            d = json.load(fr)
            lines = parseMolTxt(molTxt=d["mol"], lineDelimiter="\n")
            with open((TEST_WRITE_DIR + "/sdTxt01.txt"), "w") as fw:
                for l in lines:
                    fw.write("{}\n".format(l))
            self.assertEqual(15, len(lines))
