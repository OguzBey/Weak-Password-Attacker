#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# version 1.1.0

import sys,os,time
sys.path.append("./source/")
import lookupip as lk
import bruteforce as bf
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')

class Color(object):

	def __init__(self):
		self.red = "\033[31m" # kırmızı
		self.white = "\033[97m" # beyaz
		self.reset = "\033[0m" # resetleme
		self.bold = "\033[1m" # koyu yazma
		self.underline = "\033[4m" # alt yazili yazma

yazi = Color()

class Help(object):
	def __init__(self):
		print yazi.bold+yazi.white+ "python file.py -u <link|ip adress> -w <text file>"+yazi.reset
		print yazi.underline+yazi.red+ "Example :\n" + yazi.reset
		print yazi.bold+yazi.red+ "python weakpassword.py -u site.com -w ~/Desktop/cikti.txt\n"+yazi.reset
def start(link,filename):
	lookup = lk.ReverseIpLookup()
	ret = lookup.gonder(link)
	if ret == -1:
		Help()
		time.sleep(2)
		sys.exit()
	elif ret == -2:
		print yazi.bold+yazi.red+"[!]  Ip engeli..."+yazi.reset
		time.sleep(2)
		sys.exit()
	for domain ,bosluk in ret:
		calistir.run(domain,filename)

if __name__ == '__main__':

	if len(sys.argv) == 5:
		if sys.argv[1] == "-u" and sys.argv[3] == "-w":
			calistir = bf.Tarayici()
			start(sys.argv[2],sys.argv[4])
			#print sys.argv[4]
		else:
			Help()
	else:
		Help()
