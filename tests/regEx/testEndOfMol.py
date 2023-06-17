from vrglTest.loggingTestCase import LoggingTestCase
import re

_matchCode = "M *END"


class TestEndOfMol(LoggingTestCase):
    def test_a_Fail(self):
        m = self.getMatchedProperty("")
        self.assertIsNone(m)

    def test_b_Fail(self):
        m = self.getMatchedProperty(" ")
        self.assertIsNone(m)

    def test_c_Fail(self):
        m = self.getMatchedProperty("MEND")
        self.assertIsNotNone(m)

    def test_d_varyingSpaces(self):
        m = self.getMatchedProperty("M END")
        self.assertIsNotNone(m)

    def test_e_varyingSpaces(self):
        m = self.getMatchedProperty("M  END")
        self.assertIsNotNone(m)

    def getMatchedProperty(self, txt):
        m = re.match(_matchCode, txt)
        return m
