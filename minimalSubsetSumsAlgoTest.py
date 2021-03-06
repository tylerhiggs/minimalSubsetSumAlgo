#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:59:26 2020

@author: tylerhiggs
"""

import os
import minimalSubsetSumsAlgo
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)


class TestImage(unittest.TestCase):
    def test_empty(self):
        l = []
        result = minimalSubsetSumsAlgo.minimalSubsetSumDifference(l)
        expected = set(),set()
        self.assertEqual(result, expected)
        
    def test_given(self):
        l = [5,10,15,20,25]
        expected_sum_difference = 5
        s1,s2 = minimalSubsetSumsAlgo.minimalSubsetSumDifference(l)
        self.assertEqual(abs(sum(s1) - sum(s2)), expected_sum_difference)
        
    def test_reversed(self):
        l = [25,20,15,10,5]
        expected_sum_difference = 5
        s1,s2 = minimalSubsetSumsAlgo.minimalSubsetSumDifference(l)
        self.assertEqual(abs(sum(s1) - sum(s2)), expected_sum_difference)
        
    def test_one_to_99(self):
        l = [i for i in range(1,100)]
        expected_sum_difference = 0
        s1,s2 = minimalSubsetSumsAlgo.minimalSubsetSumDifference(l)
        self.assertEqual(abs(sum(s1) - sum(s2)), expected_sum_difference)
        for i in l:
            if i in s1:
                self.assertTrue(i not in s2)
            elif i in s2:
                self.assertTrue(i not in s1)
            else:
                self.assertTrue(False)
                
    def test_subsets(self):
        l = [7,36,46,40]
        result_sets = tuple(minimalSubsetSumsAlgo.minimalSubsetSumDifference(l))
        s1 = {7,46}
        s2 = {36,40}
        self.assertTrue(s1 in result_sets)
        self.assertTrue(s2 in result_sets)
        
                
    def test_subsets_again(self):
        l = [1,6,5,11]
        result_sets = tuple(minimalSubsetSumsAlgo.minimalSubsetSumDifference(l))
        s1 = {1,5,6}
        s2 = {11}
        self.assertTrue(s1 in result_sets)
        self.assertTrue(s2 in result_sets)                       


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)