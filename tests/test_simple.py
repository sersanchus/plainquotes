from unittest import TestCase

from plainquotes import plain_quotes


class SimpleTestCase(TestCase):

    def test_1(self):
        self.assertEquals(plain_quotes(""" "a" 'b' "c'd'e" """), " 'a' 'b' 'c\\'d\\'e' ")

    def test_2(self):
        self.assertEquals(plain_quotes(r"""a(""ab"+"ac"+"ad"")"""), "a(''ab'+'ac'+'ad'')")

    def test_3(self):
        self.assertEquals(plain_quotes("""'exec("ls 'tmp("a")'")'""", '"'), '"exec(\\"ls \\\\"tmp(\\\\\\\\"a\\\\\\\\")\\\\"\\")"')
