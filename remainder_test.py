# Importing unittest and pytest for the test to able to run

import pytest
import unittest

from remainder_calc import Remainder


class RemainderTest(unittest.TestCase):
    rem = Remainder()

    def test_remain(self):
        self.assertEqual(self.rem.remain(4, 2), True)

    def test_positive(self):
        self.assertEqual(self.rem.positive(5, 2), True)
