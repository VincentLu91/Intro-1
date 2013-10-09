#!usr/bin/env python
import re

'''
search for: one or more times the word "the"
'''
file = open("alice.txt","r")
text = file.readlines()
file.close()

keyword = re.compile(r"(the )+")

for line in text:
	if keyword.search(line):
		print line,
