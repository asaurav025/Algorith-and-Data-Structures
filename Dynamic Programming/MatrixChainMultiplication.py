#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:30:05 2017

@author: ska

Matrix Chain Multiplication
"""
import sys
def MatrixChainOrder(arr, n):
	m = [[0 for i in range(n)] for j in range(n)]
	
	for i in range(1,n):
		m[i][i] =0
	for l in range(2,n):
		for i in range(1, n-l+1):
			j =  i +l-1
			m[i][j] = sys.maxsize
			for k in range(i,j):
				q =m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j]
				if q < m[i][j]:
					m[i][j] = q
	return m[1][n-1]
arr = [1, 2, 3 ,4]
size = len(arr)
print(MatrixChainOrder(arr,size))