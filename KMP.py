#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:56:38 2017

@author: ska

KMP algorithm

"""
def kmp_matcher(P, T):
	n = len(T)
	m = len(P)
	# lps(array) It holds the longest prefix suffix
	lps = [0]*m
	j=0 # index for pattern
	
	computeLPS(P, m, lps )
	
	i = 0 # index for Text
	
	while i<n:
		if P[j] == T[i]:
			 i += 1
			 j += 1
		if j == m:
			print("pattern found at", i-m)
			j = lps[j-1]
			
		# mismatch after j matches	  
		elif i <n and P[j] != T[i]:
			if j!=0:
				j =lps[j-1]
			else:
				i += 1
def computeLPS(P,m,lps):
	l = 0
	lps[0] =0
	i =1
	while i <m:
		if P[i] == P[l]:
			l += 1
			lps[i] = l
			i += 1
		else:
			if l != 0:
				l = lps[l-1]
			else:
				lps[i] = 0
				i += 1 
	 
text = "saurav is cool and saurav is best"

pattern = "saurav"

kmp_matcher(pattern, text)			 