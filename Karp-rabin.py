#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 18:07:31 2017

@author: ska

Karp- Rabin (pattern matching)
"""

def karp_rabin(T,P,d,q):
	n= len(T)
	m= len(P)
	h = (d**(m-1))%q
	
#	Initiallizing Hash value
	p =0
	t=0
	
#	Preprocessing
	for i in range(m):
		p = (d*p + ord(P[i]))%q
		t= (d*t + ord(T[i]))%q
	
	
	
#	Pattern matching	
	for i in range(n-m+1):
		if p==t:
			if T[i:i+m] == P:
				print("pattern found at",i)
		if i <(n-m):
			t= (d*(t-ord(T[i])*h) + ord(T[i+m]))%q # Ajusting Hash Value
		if t <0:
			t = t+q
					
	
	
	
	
d =256 # Radix
q =293 # any large prime number


text = "saurav is cool and saurav is best"

pattern = "saurav"

karp_rabin(text, pattern,d,q)