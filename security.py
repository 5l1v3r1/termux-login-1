# -*- coding: utf-8 -*-
# coding=utf-8
import time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)

def regis():
	os.system('clear')
	slowprint('\x1b[00m\033[041m SECURE YOUR TERMUX APP \033[00m')
	u = raw_input('\x1b[00mMasukan Nickname  : \x1b[33m')
	if u == '' in u:
		regis()
	else:
		p = raw_input('\x1b[00mMasukan Password  : \x1b[33m')
		if p == '' in p:
			regis()
		else:
			os.system('clear')
			slowprint('\033[041m REGISTRATION SUCCESS \033[00m')
			slowprint('\x1b[00m File saved as \x1b[33m/termux-login/login.py')
			slowprint('\x1b[00m User & Pass saved as \x1b[33m/termux-login/sc2')
			os.system('sleep 3')
			users ="usr='"+u+"'"
			passd ="pwd='"+p+"'"
			os.system('print "'+users+'" > sc2;print "'+passd+'" >> sc2')
			os.system('cat sc1 > login.py;cat sc2 >> login.py;cat sc4 >> login.py;cat sc3 >> login.py;python2 login.py')

regis()