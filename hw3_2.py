#!/usr/bin/env python
#coding=utf-8

i=1
num=0

x=input('請輸入一數字:')

while i<=x:
	if x%i==0:
		num=num+1
	i=i+1

if num==2:
	print '%d是質數' %x
else:
	print '%d不是質數' %x