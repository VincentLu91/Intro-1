#!/usr/bin/env python
"""Write a program that evaluates the nth element of the sequence."""

# This could be solved by recursion: Gn+1 = 1 + 1/Gn

def gdratio(n):
	gdsum = 1.0
	for i in range(n):
		gdsum = 1 + 1/gdsum
	return gdsum

print gdratio(200)
