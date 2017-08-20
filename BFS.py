#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:29:13 2017

@author: ska

Breadth First Search
"""
def BFS(s):
	visited = [False]*len(g)
	traversal =[]
	queue = []
	queue.append(s)
	visited[s] = True
	while len(queue) >0:
		a = queue.pop(0)
		traversal.append(a)
		for i in g[a]:
			if visited[i]==False:
				queue.append(i)
				visited[i] = True
	return traversal
	
#==============================================================================
# Graph implementation
#==============================================================================

from collections import defaultdict

g = defaultdict(list)

def addEdge(a,b):
	g[a].append(b)
	
	
#==============================================================================
# Example Implementation	
#==============================================================================



addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 2)
addEdge(2, 0)
addEdge(2, 3)
addEdge(3, 3)

print(BFS(2))