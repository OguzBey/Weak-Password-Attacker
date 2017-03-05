#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# version 1.1.0

import urllib,urllib2,json

class ReverseIpLookup(object):

	def __init__(self):
		self.useragent = "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0"
		self.contenttype = "application/x-www-form-urlencoded; charset=UTF-8"
		self.link = "http://domains.yougetsignal.com/domains.php"
		self.key = ""

	def gonder(self,target):
		if target.startswith("http",0,4):
			return -1
		self.hedef = target
		self.values = [("remoteAddress",self.hedef),("key",self.key)]
		data = urllib.urlencode(self.values)
		req = urllib2.Request(self.link, data)
		req.add_header("Content-type", self.contenttype)
		req.add_header("User-agent", self.useragent)
		response = urllib2.urlopen(req)
		veri = json.loads(response.read())
		if veri["status"] == "Fail":
			return -2
		return veri["domainArray"]