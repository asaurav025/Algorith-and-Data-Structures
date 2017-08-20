#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 09:09:13 2017

@author: ska

Prims MST: using min heap time complexity is ElogV

If we implement using fibonacci heap then time complexity becomes E+VlogV
"""

#==============================================================================
# MinHeap implementation 
#==============================================================================

def left(i):
	return (2*i)+1

def right(i):
	return (2*i)+2

def minHeapify(A,i):
	l = left(i)
	r = right(i)
#	print(A[i],A[l], A[r])
	if l<= len(A)-1 and A[l]<A[i]:
		smallest = l
	else:
		smallest = i
	if r <= len(A)-1 and A[r]<A[smallest]:
		smallest = r
	if smallest != i:
		A[smallest],A[i] = A[i], A[smallest]
		minHeapify(A,smallest)
		
def BuildHeap(A):
	heapSize = len(A)
#	print('Here')
	for i in range((heapSize-1)//2, -1,-1):
#		print(i)
		minHeapify(A,i)
	return A


def extractMin(A):
#	minHeapify(A,0)
	p = A[0]
	A[0],A[-1] = A[-1],A[0]
	A.pop()
	minHeapify(A,0)
	return p

#B= [[27,5],[17,3],[3,1],[16,20],[13,100],[10,1],[5,7],[12,4],[8,9],[99,0]]
#print(BuildHeap(B))
#while len(B):
#	print(extractMin(B))

#==============================================================================
# Implementation of Prim's MST
#==============================================================================
from math import inf

def Prims(A,j =0):
	virtices =[]
	for k in range(V):
		virtices.append([inf,k,None])
	virtices[j][0] = 0
#	print(virtices)
	key = virtices
	H = BuildHeap(key)
#	print(H)
	result = []
	while len(H)>0:
		us = extractMin(H)
		result.append(us)
		u = us[1]
#		print(us[0])
		for i in g[u]:
#			print(i)
			for l in range(len(H)):
#				print(H)
				if H[l][1] == i[0] and H[l][0] > i[1]:	#H[l][1] is virtice
					H[l][0] = i[1]
					H[l][2]=u 	#parent
#					minHeapify(H,H.index(H[l]))
						
#		print(H)
	return result

	
	
	
	
#==============================================================================
# Graph Implementation	
#==============================================================================
from collections import defaultdict
g = defaultdict(list)

def addEdge(u,v,w):
	g[v].append((u,w))
	g[u].append((v,w))
	
#==============================================================================
# Implementation of Example
#==============================================================================
V = 9
addEdge(0, 1, 4);
addEdge(0, 7, 8);
addEdge(1, 2, 8);
addEdge(1, 7, 11);
addEdge(2, 3, 7);
addEdge(2, 8, 2);
addEdge(2, 5, 4);
addEdge(3, 4, 9);
addEdge(3, 5, 14);
addEdge(4, 5, 10);
addEdge(5, 6, 2);
addEdge(6, 7, 1);
addEdge(6, 8, 6);
addEdge(7, 8, 7);
print(Prims(g,6))