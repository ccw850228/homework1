#!/usr/bin/env python
#coding=utf-8
print '�׷��K�X!start!'
import random
x=random.randint(1,99)

sta=1
fin=99
sum=1
num=input('�вq�Ʀr:')

while x!=num:
	if (num<x):
		sta=num
		print '�{�b�d��%d~%d' %(sta,fin)
		sum=sum+1
		num=input('�вq�Ʀr:')
	elif (num>x):
		fin=num
		print '�{�b�d��%d~%d' %(sta,fin)
		sum=sum+1
		num=input('�вq�Ʀr:')
else:
	print 'WOW BINGO!!! �K�X�O%d ��F%d��' %(x,sum)