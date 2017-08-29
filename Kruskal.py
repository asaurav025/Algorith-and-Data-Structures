#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:24:56 2017

@author: ska

Kruskal MST: time complexity ElogV
"""
#==============================================================================
# Implemention of Union-Find Data Structure
#==============================================================================

def find(parent, i):
	if parent[i] == i:
		return i
	return find(parent, parent[i])

def union(parent, rank, x,y):
	xroot = find(parent, x)
	yroot = find(parent, y)
	
	#Assign parent according to rank
	if rank[xroot] > rank[yroot]:
		parent[yroot] = xroot
	elif rank[xroot] < rank[yroot]:
		parent[xroot] = yroot
	else:
		parent[xroot] = yroot
		rank[yroot] += 1
		
#==============================================================================
#Kruskal Minimum Spanning Tree |||| graph is of form [u,v,w], where u and v ar virtices
# and w weight|| V = total no. of virtices
#==============================================================================

def KruskalMST():
	result = []
	
	graphs = sorted(graph , key = lambda item:item[2])
	parent=[]
	rank =[0]*V
	for i in range(V):
		parent.append(i)
		
	i = 0 # index for sorted edges
	e = 0 # index for result
	
	while e < V-1:
		u,v,w = graphs[i]
		i += 1
		x = find(parent, u)
		y = find(parent, v)
		if x != y:
			union(parent, rank, x,y)
			e += 1
			result.append([u,v,w])
	print(result)
#==============================================================================
# Graph Implementation	
#==============================================================================
def addEdge(u,v,w):
	graph.append([u,v,w])

graph = []

#==============================================================================
# Implementation by example
#==============================================================================
V =4 
addEdge(0, 1, 10)
addEdge(0, 2, 6)
addEdge(0, 3, 5)
addEdge(1, 3, 15)
addEdge(2, 3, 4)

KruskalMST()
			
	
	
	
	