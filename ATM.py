#!/usr/bin/env python
#coding=utf-8

money=5000

tmoney=input('想要領多少錢?')

f=open("ATM.txt","w")

if tmoney<money:
	print ('您的存款還剩%d元') %(money-tmoney)
	f.write("您的存款還剩%d元" %(money-tmoney)) 

elif tmoney==money:
	print ('您的存款無剩餘存款')
	f.write("您的存款無剩餘存款")
elif tmoney>money:
	print ('您的存款不足！')
	f.write	("您的存款不足！")
