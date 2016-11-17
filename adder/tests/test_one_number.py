from unittest import TestCase
import math

import adder

class TestOneNumber(TestCase):

    def test_floats(self):
        for num in [1617161771.7650001, math.pi, math.pi**100,
                    math.pi**-100, 3.1]:
            self.assertEqual(adder.run(num), num)

    def test_ints(self):
        for num in [-1,0,1]:
            self.assertEqual(adder.run(num), num)

    def test_deplorables(self):
        self.assertTrue(math.isinf(adder.run(math.inf)))
        self.assertTrue(math.isnan(adder.run(math.nan)))


