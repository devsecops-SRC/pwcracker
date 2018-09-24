#coding=utf-8
import telnetlib
import re
from lib import helper as h

def plu_info():
	dict_plugin = {};
	dict_plugin['name'] = "telnet"
	dict_plugin['author'] = "c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 17:41"
	dict_plugin['description'] = "Used to guess Telnet service password."
	dict_plugin["usage"] = "python pwcracker.py -t telnet://192.168.228.165:23 -u root -P ./dic/general_password.txt"
	return dict_plugin

def doCrack(address,username,password):
	host = h.getPath(address)
	port = h.getPort(address) if h.getPort(address) != None else 23
	try:
		tn = telnetlib.Telnet(host,port,timeout=10)
		tn.set_debuglevel(0) #2是为了看更多东西
		# tn.read_until("login: ".encode('ascii'))
		# tn.write(username.encode('ascii') + "\r\n".encode('ascii'))
		# tn.read_until("password: ".encode('ascii'))
		# tn.write(password.encode('ascii') + "\r\n".encode('ascii'))

		tn.read_until("login:")
		tn.write(username + "\r\n")
		tn.read_until("assword:")
		tn.write(password + "\r\n")
		
		res = tn.read_some()
		res = tn.read_some()
		res = tn.read_some()
		tn.write("exit\r\n")
		tn.close()
		# Windows下登录失败关键字为Login Failed，Linux下登录失败关键字为Login incorrect。
		rex = r'Login\s+(Failed|incorrect)' 
		tmp = re.search(rex,res)
		if tmp == None:
			return True,u'Crack success!'
		else:
			return False,u'Crack fail!'

	except Exception as e:
		return False,str(e)	