# -*- coding: utf-8 -*-

import smtplib
import os
from jinja2 import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail(object):
	"""docstring for SendEmail"""
	def __init__(self):
		super(SendEmail, self).__init__()
		self.mail_from = 'zabbix@zabbix'
		self.mail_user = 'zabbix'
		self.mail_to = 'admin@admni'
		self.mail_server = 'localhost'
		self.mail_pass = ''
		self.mail_subject = 'Subject from Zabbix'
		self.mail_head = 'head'
		self.mail_graph = ''
		self.mail_footer = 'footer'
		self.mail_url = ''

	def send(self):
		msg = MIMEMultipart('alternative')
		msg['Subject'] = self.mail_subject
		msg['From'] = self.mail_from
		msg['To'] = self.mail_to

		text = self.mail_head + self.mail_footer

		template_file = open(os.getcwd + './email_template.j2')
		template_text = ''
		for lines in template_file:
			template_text = template_text + lines

		t = Template(template_text)
		html = t.render(zabbix_name='Test_Zabbix',
								trigger_text=self.mail_head, graph=self.mail_graph,
								trigger_url=self.mail_url, trigger_details=self.mail_footer,
								company='Company Artsofte')

		part1 = MIMEText(text, 'plain', 'utf-8')
		part2 = MIMEText(html, 'html', 'utf-8')

		msg.attach(part1)
		msg.attach(part2)

		s = smtplib.SMTP()
		s.connect(self.mail_server)
		s.ehlo(self.mail_from)
		s.login(self.mail_user, self.mail_pass)
		s.sendmail(self.mail_from, self.mail_to, msg.as_string())
		s.quit()

		
