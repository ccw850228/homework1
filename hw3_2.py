#!/usr/bin/env python
#coding=utf-8

i=1
num=0

x=input('�п�J�@�Ʀr:')

while i<=x:
	if x%i==0:
		num=num+1
	i=i+1

if num==2:
	print '%d�O���' %x
else:
	print '%d���O���' %x