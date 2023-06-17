from vrglTest.loggingTestCase import LoggingTestCase
import re

_matchCode = "> +<(?P<prop>.+)>"


class TestProperty(LoggingTestCase):
    def test_a_varyingSpacesFail(self):
        m = self.getMatchedProperty("><No>")
        self.assertIsNone(m)

    def test_b_varyingSpaces(self):
        m = self.getMatchedProperty("> <Yes>")
        self.assertEqual(m, "Yes")

    def test_c_varyingSpaces(self):
        m = self.getMatchedProperty(">  <Yes Sir>")
        self.assertEqual(m, "Yes Sir")

    def test_d_varyingSpaces(self):
        m = self.getMatchedProperty(">   <Yes Oh Yes>")
        self.assertEqual(m, "Yes Oh Yes")

    def test_e_varyingSpaces(self):
        m = self.getMatchedProperty(">   <Yes Oh Yes> somethin somethin")
        self.assertEqual(m, "Yes Oh Yes")

    def getMatchedProperty(self, txt):
        m = re.match(_matchCode, txt)
        if m:
            return m.group("prop")
        return None
