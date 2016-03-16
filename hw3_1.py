#!/usr/bin/env python
#coding=utf-8

a=1
y=1
for x in range(1,11):
	for y in range(1,x+1):
		if y<=x:
			print a,
			a=a+1
	print "\n"	