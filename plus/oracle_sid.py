#coding=utf-8
import cx_Oracle
from lib import helper as h

'''
该插件的准确性有待提高，经过测试可以爆破处sid，但是设置一个错误地址也会返回有爆破成功的sid。
'''

def plu_info():
	dict_plugin = {};
	dict_plugin['name'] = "oracle_sid"
	dict_plugin['author'] = "c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:05"
	dict_plugin['description'] = "Used to guess Oracle database sid."
	dict_plugin["usage"] = "python pwcracker.py -t oracle_sid://192.168.1.108:1521 -P ./dic/general_password.txt"
	return dict_plugin

def doCheck(address,username,password):
	if not (len(username) == 1 and username[0] == ''):
		return False,u'oracle数据的sid破解，无需设置账号！'
	else:
		return True,None

def doCrack(address,username,password):
	'''
	# ORA-28000 代表账号被锁
	# ORA-01017 代表账号或密码不正确
	# ORA-12505 代表sid不正确
	'''
	host = h.getPath(address)
	port = h.getPort(address) if h.getPort(address) !=None else 1521		
	dsn = cx_Oracle.makedsn(host=host, port=port, sid=password)
	try:
		fp = cx_Oracle.connect('SYS', '', dsn, threaded=True)
		code, mesg = '0',fp.version
		return True,mesg
	except cx_Oracle.DatabaseError as e:
		code,mesg = e.args[0].message[:-1].split(': ', 1)
		#print code,mesg
	
	if code == 'ORA-12505':
		return False,u'Crack fail!'
	else:
		return True,u'Crack success!'
	