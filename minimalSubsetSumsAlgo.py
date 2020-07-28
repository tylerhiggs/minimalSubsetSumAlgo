#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:09:32 2020

@author: Tyler Higgs
"""

def minimalSubsetSumDifference(A):
    '''
    1. Sub-prob: x(i,s): divide array A[i:] into two subsets so that the 
        difference between the subsets is as small as possible and return this 
        smallest difference where s is the pre-existing sum. We can create a 
        sum by labeling one subset as positive and another as negativen and 
        taking the absolute value
    2. Relation: x(i,s) = min(x(i + 1, s + A[i]),x(i + 1, s - A[i]))
    3. Topological order: always increase i
    4. Base: x(n,s) = s
    5. Original: x(0,0)
    6. Time: O(sn)
    '''
    
    B = set()
    C = set()
    
    P = {}
    memo = {}
        
    def x(i,s):
        if (i,s) in memo:
            return memo[(i,s)]
        elif i < len(A):
            add = abs(x(i + 1, s + A[i]))
            sub = abs(x(i + 1, s - A[i]))
            if add > sub:
                P[(i,s)] = (i + 1, s - A[i])
            else:
                P[(i,s)] = (i + 1, s + A[i])
            ans = min(add, sub)
            memo[(i,s)] = ans
            return ans
        else:
            memo[(i,s)] = s
            return s
    
    x(0,0)
    
    next_s = 0
    
    for i in range(len(A)):
        if P[(i,next_s)][1] == next_s + A[i]:
            B.add(A[i])
            next_s = next_s + A[i]
        else:
            C.add(A[i])
            next_s = next_s - A[i]
        
    return B,C

    