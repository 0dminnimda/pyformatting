# -*- coding: utf-8 -*-

# import pyformatting for all python 3 versions
from os.path import dirname
import sys
sys.path.insert(0, dirname(sys.path[0]))
import pyformatting
sys.path.pop(0)

# standard import
import unittest
from pyformatting import optional_format, defaultformatter

# defaults
KW = {"a": 9, "b": 8, "c": 7, "d": 6}
HALF_KW = {"a": 9, "b": 8}

NA = (9, 8, 7, 6)
HALF_A = (9, 8)

IN_0 = "-{}-{}-{}-{}-"
IN_1 = "-{0}-{1}-{2}-{3}-"
IN_2 = "-{a}-{b}-{c}-{d}-"

IN_0_S = "-{!s}-{!s}-{!s}-{!s}-"
IN_1_S = "-{0!s}-{1!s}-{2!s}-{3!s}-"
IN_2_S = "-{a!s}-{b!s}-{c!s}-{d!s}-"

IN_0_C = "-{:,}-{:,}-{:,}-{:,}-"
IN_1_C = "-{0:,}-{1:,}-{2:,}-{3:,}-"
IN_2_C = "-{a:,}-{b:,}-{c:,}-{d:,}-"

default_format = defaultformatter(int)


# test cases
class TestOptionalFormat(unittest.TestCase):
    def _format(self, result, *args, **kwargs):
        self.assertEqual(
            optional_format(*args, **kwargs), "-9-8-" + result + "-")

    def test_format(self):
        self._format("{}-{}", IN_0, *HALF_A)

        self._format("{2}-{3}", IN_1, *HALF_A)

        self._format("{c}-{d}", IN_2, **HALF_KW)

    def test_additional_format(self):
        self._format("{}-{}", IN_0, *HALF_A, **KW)

        self._format("{2}-{3}", IN_1, *HALF_A, **KW)

        self._format("{c}-{d}", IN_2, *NA, **HALF_KW)

    def test_format_spec(self):
        self._format("{:,}-{:,}", IN_0_C, *HALF_A)

        self._format("{2:,}-{3:,}", IN_1_C, *HALF_A)

        self._format("{c:,}-{d:,}", IN_2_C, **HALF_KW)

    def test_conversion(self):
        self._format("{!s}-{!s}", IN_0_S, *HALF_A)

        self._format("{2!s}-{3!s}", IN_1_S, *HALF_A)

        self._format("{c!s}-{d!s}", IN_2_S, **HALF_KW)


class TestDefaultFormat(unittest.TestCase):
    def _format(self, *args, **kwargs):
        self.assertEqual(
            default_format(*args, **kwargs), "-9-8-0-0-")

    def test_format(self):
        self._format(IN_0, *HALF_A)

        self._format(IN_1, *HALF_A)

        self._format(IN_2, **HALF_KW)

    def test_additional_format(self):
        self._format(IN_0, *HALF_A, **KW)

        self._format(IN_1, *HALF_A, **KW)

        self._format(IN_2, *NA, **HALF_KW)

    def test_format_spec(self):
        self._format(IN_0_C, *HALF_A)

        self._format(IN_1_C, *HALF_A)

        self._format(IN_2_C, **HALF_KW)

    def test_conversion(self):
        self._format(IN_0_S, *HALF_A)

        self._format(IN_1_S, *HALF_A)

        self._format(IN_2_S, **HALF_KW)


# run test case
if __name__ == "__main__":
    unittest.main(argv=sys.argv + ['-v'])
