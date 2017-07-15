# zabbix-email-extra
Exta email notification from zabbix

# Description

Script for pretty formated email from zabbix-server, with graph. Used adaptive mail template HTMLemail.
![Example mail](https://habrastorage.org/web/3b0/60d/a27/3b060da2775e42aaba59bdf150450181.png)


# Instalation

1. Install python3.
1. Install python extensions: 
	* pip install py-zabbix
	* pip install jinja2
	* pip install requests
1. Create Zabbix read-only user for api.
1. Configure zbx_ex_setting.py (see zbx_ex_setting.example.py for expample).
1. Put scripts to zabbix_alert_script directory.
1. Configure Zabbix, then he used this script for sending notifications.
