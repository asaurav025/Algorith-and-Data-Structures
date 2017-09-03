#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:16:37 2017

@author: ska

Coin Change Problem
"""
#==============================================================================
# 
# def CoinC(S,m,n):
# 	table = [[0 for i in range(m)] for j in range(n+1)]
# 	
# 	for i in range(m):
# 		table[0][i] = 1
# 		
# 	for i in range(1, n+1):
# 		for j in range(m):
# 			if i-S[j] >=0:
# 				x = table[i-S[j]][j]
# 			else:
# 				x =0
# 			y = table[i][j-1] if j >0 else 0
# 			
# 			table[i][j] = x+y
# 	print(table)
# 	return table[n][m-1]
# 	
#==============================================================================
def CoinC(S,m,n):
	table = [[0 for i in range(n+1)] for j in range(m)]
	for i in range(m):
		table[i][0] = 1
	for i in range(m):
		for j in range(1,n+1):
			x = table[i][j-S[i]]  if (j-S[i]) >=0 else 0
			
			y = table[i-1][j] if i > 0 else 0
			
			table[i][j] = x+y
	print(table)
	return table[m-1][n]
			 
arr = [1, 2, 3]
m = len(arr)
n = 4

print(CoinC(arr, m, n))