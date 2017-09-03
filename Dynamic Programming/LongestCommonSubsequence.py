#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:31:35 2017

@author: ska

Longest Common Subsequence
"""
def LCS(A, B):
	m = len(A)
	n = len(B)
	l = [[None for i in range(n+1)]for j in range(m+1)]
#	print(l)
#	print()
	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j== 0:
				l[i][j] = 0
			elif A[i-1] == B[j-1]:
				l[i][j] = l[i-1][j-1]+1
			else:
				l[i][j] = max(l[i-1][j],l[i][j-1])
#			print(l)
#			print()
	return l[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", LCS(X, Y))
