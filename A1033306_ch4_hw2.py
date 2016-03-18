#!/usr/bin/env python
#coding=utf-8
print '終極密碼!start!'
import random
x=random.randint(1,99)

sta=1
fin=99
sum=1
num=input('請猜數字:')

while x!=num:
	if (num<x):
		sta=num
		print '現在範圍%d~%d' %(sta,fin)
		sum=sum+1
		num=input('請猜數字:')
	elif (num>x):
		fin=num
		print '現在範圍%d~%d' %(sta,fin)
		sum=sum+1
		num=input('請猜數字:')
else:
	print 'WOW BINGO!!! 密碼是%d 花了%d次' %(x,sum)