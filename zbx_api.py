# -*- coding: utf-8 -*-
import requests
import sys
import os
import base64

class ZabbixImage(object):
	"""For get graph image"""
	def __init__(self, server, api_user, api_pass):
		super(ZabbixImage, self).__init__()
		#self.arg = arg
		self.server = server
		self.api_user = api_user
		self.api_pass =api_pass
		self.verify = True
		self.cookie = None
		self.res_img = None
		self.res_url = None

	def login(self):

		if not self.verify:
			requests.package.urllib3.disable_warnings()

		data_api = {"name": self.api_user, "password": self.api_pass, "enter": "Sign in"}
		req_cookie = requests.post(self.server + "/", data=data_api, verify=self.verify)
		cookie = req_cookie.cookies

		if len(req_cookie.history) > 1 and req_cookie.history[0].status_code == 302:
			print_message("Probably the server in your config file has not full URL")

		if not cookie:
			print_message("authorization failed")
			cookie = None

		self.cookie = cookie

	def graph_get(self, itemid, period, title, width, height):
		#title = requests.utils.quote(title)

		zbx_url_url = self.server + "/history.php?action=showgraph&itemids%5B%5D={0}".format(itemid)

		zbx_img_url = self.server + "/chart.php?period={1}" \
									"&itemids%5B0%5D={0}" \
									"&type=0&updateProfile=1" \
									"&width={3}"\
									"&height={4}".format(itemid, period,title,width,height)
		print_message(zbx_img_url)

		res = requests.get(zbx_img_url, cookies=self.cookie)
		res_code = res.status_code
		if res_code == 404:
			print_message("can`t get image from '{0}'".format(zbx_img_url))
			return False
			
		self.res_img = '<img src="data:image/png;base64,' + base64.b64encode(res.content) + '" alt=graph>'
		self.res_url = zbx_url_url
		

def print_message(string):
    string = str(string) + "\n"
    filename = sys.argv[0].split("/")[-1]
    sys.stderr.write(filename + ": " + string)