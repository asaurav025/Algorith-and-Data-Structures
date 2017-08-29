#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:06:09 2017

@author: ska

Dijktra [complexity(n^2)]
"""
import sys
def minDistance(dist, visited):
	mi = sys.maxsize
	for i in range(v):
		if dist[i] <mi and visited[i]  == False:
			mi = dist[i]
			min_index = i
	return min_index
				
def dijktra(s):
	dist = [sys.maxsize]*v
	dist[s] = 0
	
	visited = [False]*v
	
	for node in range(v):
		u = minDistance(dist, visited)
		visited[u] = True
		
		for w in range(v):
			if graph[u][w] >0  and visited[w] == False and dist[w] > dist[u] + graph[u][w]:
				 dist[w] = dist[u] + graph[u][w]
	print(dist)
	
	
v =9					
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ];