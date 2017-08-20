#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:43:26 2017

@author: ska

Topological Sorting: Used for Directed Acyclic Graph(DAG)
"""


def topoSort():
	visited = [False]*V
	stack = []
	
	for i in range(V):
		if visited[i] == False:
			topoUtil(i, visited, stack)
			
	print(stack)

def topoUtil(v, visited, stack):
	visited[v] = True
#	print(v)
	for i in g[v]:
		if visited[i] == False:
			topoUtil(i, visited, stack)
	stack.insert(0,v)			
	
#==============================================================================
#Implementation of Graph 
#==============================================================================
from collections import defaultdict

g = defaultdict(list)

def addEdge(a,b):
	g[a].append(b)
	
#==============================================================================
# implementation of example 
#==============================================================================
addEdge(5, 2);
addEdge(5, 0);
addEdge(4, 0);
addEdge(4, 1);
addEdge(2, 3);
addEdge(3, 1);
V = 6 #total no. of virtices

topoSort()
 
