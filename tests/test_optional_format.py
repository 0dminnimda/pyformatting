# -*- coding: utf-8 -*-

# import pyformatting for all python 3 versions
# especially for python < 3.4 (these versions don't have pip)
from os.path import dirname
import sys
sys.path.insert(0, dirname(sys.path[0]))
import pyformatting
sys.path.pop(0)

# standard import
import unittest
from pyformatting.correct_version import PY_34
from pyformatting import optional_format

# defaults
FULL_KW = {"a": 9, "b": 8, "c": 7, "d": 6}
HALF_KW = {"a": 9, "b": 8}

FULL_A = (9, 8, 7, 6)
HALF_A = (9, 8)

IN_0 = "{}{}{}{}"
IN_1 = "{0}{1}{2}{3}"
IN_2 = "{a}{b}{c}{d}"


# test case
class TestOptionalFormat(unittest.TestCase):
    def o_format(self, result, *args, **kwargs):
        self.assertEqual(optional_format(*args, **kwargs), result)

    def test_not_filled(self):
        if PY_34:
            self.o_format(IN_0, IN_0)
            self.o_format(IN_0, IN_0, **FULL_KW)

        self.o_format(IN_1, IN_1)
        self.o_format(IN_1, IN_1, **FULL_KW)

        self.o_format(IN_2, IN_2)
        self.o_format(IN_2, IN_2, *FULL_A)

    def test_partially_filled(self):
        if PY_34:
            self.o_format("98{}{}", IN_0, *HALF_A)
            self.o_format("98{}{}", IN_0, *HALF_A, **FULL_KW)

        self.o_format("98{2}{3}", IN_1, *HALF_A)
        self.o_format("98{2}{3}", IN_1, *HALF_A, **FULL_KW)

        self.o_format("98{c}{d}", IN_2, **HALF_KW)
        self.o_format("98{c}{d}", IN_2, *FULL_A, **HALF_KW)

    def test_fully_filled(self):
        if PY_34:
            self.o_format("9876", IN_0, *FULL_A)
            self.o_format("9876", IN_0, *FULL_A, **FULL_KW)

        self.o_format("9876", IN_1, *FULL_A)
        self.o_format("9876", IN_1, *FULL_A, **FULL_KW)

        self.o_format("9876", IN_2, **FULL_KW)
        self.o_format("9876", IN_2, *FULL_A, **FULL_KW)


# run test case
if __name__ == "__main__":
    unittest.main(argv=sys.argv.append('-v'))
