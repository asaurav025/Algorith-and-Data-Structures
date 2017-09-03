#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:26:17 2017

@author: ska

Minimum Cost Path
"""
def MCP(cost, m,n):
	MCP = [[0 for i in range(len(cost[0])) ] for j in range(len(cost))]
	MCP[0][0]  = cost[0][0]
	for i in range(1,m+1):
		MCP[i][0] = MCP[i-1][0] +cost[i][0]
	for i in range(1, n+1):
		MCP[0][i] = MCP[0][i-1] + cost[0][i]
	for i in range(1, m+1):
		for j in range(1, n+1):
			MCP[i][j] = min(MCP[i-1][j-1], MCP[i][j-1], MCP[i-1][j]) + cost[i][j]
#	print(MCP)
	return MCP[m][n]


cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(MCP(cost, 2, 2))