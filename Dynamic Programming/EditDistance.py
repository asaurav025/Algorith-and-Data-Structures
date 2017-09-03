#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 11:41:19 2017

@author: ska

Edit Distance
"""
def ed(str1,str2,m,n):
	 ed = [[None for i in range(n+1)] for j in range(m+1)]
	 
	 for i in range(m+1):
		 for j in range(n+1):
			 if i == 0:
				 ed[i][j] = j
			 elif j == 0:
				 ed[i][j] = i
			 elif str1[i-1] == str2[j-1]:
				 ed[i][j] = ed[i-1][j-1]	 
			 else:
				 ed[i][j] = 1+ min(ed[i-1][j],ed[i][j-1], ed[i-1][j-1])
				 
	 return ed[m][n]				 
 
str1 = "sunday"
str2 = "saturday"
 
print(ed(str1, str2, len(str1), len(str2)))