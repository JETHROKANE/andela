#!/usr/bin/python

import unittest
from ptest1 import primeAnalysis

class ptest2(unittest.TestCase):
    def final_output(self):
        self.assertEqual(primeAnalysis(26), '2,3,5,7,11,13,17,19,23,')

    def test_int(self):
        self.assertEqual(primeAnalysis(26.12), 'The provided input is not an intiger.')

    def test_str(self):
        self.assertEqual(primeAnalysis('str'), 'The provided input is not an intiger.')

    def test_neg(self):
        self.assertEqual(primeAnalysis(-51), 'The provided input is not an intiger.')

if __name__ == '__main__':
    unittest.main()