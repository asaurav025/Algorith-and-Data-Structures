#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 23:26:49 2017

@author: ska

Union-Find Data Structure
"""


def find(parent, child):  # Here we find parrent of child in recursive manner
	if parent[child] == child:
		return child
	else:
		return find(parent, parent[child])

def union(parent, rank, x, y):
	xroot = find(parent, x) # finding parent of x
	yroot = find(parent, y) # finding parent of y
	
	if rank[xroot] < rank[yroot]: #comparing ranks of parent, parent is selected on the basis of rank
		parent[xroot] = yroot
	elif rank[xroot] > rank[yroot]:
		parent[yroot] = xroot
	else:
		parent[xroot]  = yroot # if same then select any one of them as parent and increment its rank by 1
		rank[yroot] += 1
		
		
