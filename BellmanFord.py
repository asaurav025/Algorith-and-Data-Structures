#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:27:30 2017

@author: ska

Bellman–Ford Algorithm :complexity o(VE)
works only when there are no negitive cycle
"""

def addEdge(u,v,w):
	graph.append([u,v,w])
	
def bellmanFord(src):
	dist = [maxnumber]*(V)
	dist[0] = 0
	for i in range(V-1):
		for u,v,w in graph:
			if dist[u] != maxnumber and dist[v] > dist[u] +w:
				dist[v] = dist[u] +w
		
	return dist
maxnumber = float("inf")
graph = []
V =5
addEdge(0, 1, -1)
addEdge(0, 2, 4)
addEdge(1, 2, 3)
addEdge(1, 3, 2)
addEdge(1, 4, 2)
addEdge(3, 2, 5)
addEdge(3, 1, 1)
addEdge(4, 3, -3)
print(bellmanFord(0))