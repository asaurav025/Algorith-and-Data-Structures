#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:04:26 2017

@author: ska

Longest Increasing Susequence
"""
def lis(ar):
	n = len(ar)
	l = [1]*n
	for i in range(1,n):
		for j in range(i):
			if ar[i]>ar[j] and l[i] < l[j]+1:
				l[i] = l[j] +1
	return max(l)

arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", lis(arr))
