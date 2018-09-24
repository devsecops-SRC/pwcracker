#coding=utf-8
import ftplib
from lib.helper import getPath,getPort

def plu_info():
	dict_plugin={};
	dict_plugin['name']="ftp"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"
	dict_plugin['description'] = "Used to guess FTP service password."
	dict_plugin["usage"] = "python pwcracker.py -t ftp://127.0.0.1:21 -u test -P ./dic/general_password.txt"
	return dict_plugin

def doCrack(address,username,password):
	host = getPath(address)
	port = getPort(address)
	try:
		ftp = ftplib.FTP(host)
		ftp.connect(host, port, timeout = 10)
		ftp.login(username, password)
		ftp.quit()
		return True,u'Crack success!'
	except ftplib.all_errors:
		return False,u'Crack fail!'