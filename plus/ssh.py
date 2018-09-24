#coding=utf-8
import paramiko
from lib import helper as h

def plu_info():
	dict_plugin = {};
	dict_plugin['name'] = "ssh"
	dict_plugin['author'] = "c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-19 0:23"
	dict_plugin['description'] = "Used to guess SSH service password."
	dict_plugin["usage"] = "python pwcracker.py -t ssh://192.168.228.165:22 -u root -P ./dic/general_password.txt"
	return dict_plugin

def doCrack(address, username, password):
	host = h.getPath(address)
	port = h.getPort(address) if h.getPort(address) != None else 22
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host,port,username,password,timeout=5)		
		ssh.close()
		return True,u'Crack success!'
	except Exception,e:
		return False,u'Crack fail!'