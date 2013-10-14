#!usr/bin/env python
import re

'''
search for: one or more times the word "the"
This program is a solution to an exercise taken from a link: http://www.upriss.org.uk/python/PythonCourse.html
'''
file = open("alice.txt","r")
text = file.readlines()
file.close()

keyword = re.compile(r"(the )+")

for line in text:
	if keyword.search(line):
		print line,
