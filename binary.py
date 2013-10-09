#!/usr/bin/env python

"""Write a function that takes a target number and an array of numbers in
non-descending order and returns either the position of the number in the 
array or -1 to indicate the target number is not found int he array.
Also, write a suitable test program that shows the accuracy of your binary
search function"""

def binary(target, arr):
	low = 0
	high = len(arr)
	while low <= high:
		middle = (low + high)/2 
		if arr[middle] > target:
			high = middle - 1
		elif arr[middle] < target:
			low = middle + 1
		else:
			return middle

	return -1 # if the loop 

hi = [13, 19, 24, 29, 32, 37, 43]
print hi
pos = binary(32, hi)
print pos
