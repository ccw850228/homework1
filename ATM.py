#!/usr/bin/env python
#coding=utf-8

money=5000

tmoney=input('�Q�n��h�ֿ�?')

f=open("ATM.txt","w")

if tmoney<money:
	print ('�z���s���ٳ�%d��') %(money-tmoney)
	f.write("�z���s���ٳ�%d��" %(money-tmoney)) 

elif tmoney==money:
	print ('�z���s�ڵL�Ѿl�s��')
	f.write("�z���s�ڵL�Ѿl�s��")
elif tmoney>money:
	print ('�z���s�ڤ����I')
	f.write	("�z���s�ڤ����I")
