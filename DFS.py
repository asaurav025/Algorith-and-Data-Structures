#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:45:00 2017

@author: ska

Depth First Search
"""
#==============================================================================
# when graph is connected use DFS1
#==============================================================================
def DFS1(v):
	visited = [False]*len(g)
#	traverse =[]
	DFSUtil(v, visited)
	
def DFSUtil(v, visited):
	visited[v] =True
#	traverse.append(v)
	print(v)
	for i in g[v]:
		if visited[i] == False:
			DFSUtil(i, visited)
	
#==============================================================================
#when Graph is not connected use DFS2 ,it do not take any argument
#==============================================================================

def DFS2():
	visited = [False]*len(g)
#	traverse =[]
	for i in g.keys():
		if visited[i] == False:
			DFSUtil(i, visited)
			
#==============================================================================
#Graph implentation 
#==============================================================================

from collections import defaultdict

g = defaultdict(list)

def addEdge(a,b):
	g[a].append(b)
	
#traverse = []
#==============================================================================
# Example Implementation	
#==============================================================================



addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 2)
addEdge(2, 0)
addEdge(2, 3)
addEdge(3, 3)
DFS2()
#DFS1(0)