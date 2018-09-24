#coding=utf-8
import cx_Oracle
from lib import helper as h

def plu_info():
	dict_plugin = {};
	dict_plugin['name'] = "oracle"
	dict_plugin['author'] = "c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 17:58"
	dict_plugin['description'] = "Used to guess Oracle database password."
	dict_plugin["usage"] = "python pwcracker.py -t oracle://192.168.1.108:1521?sid=ORCL -u SYS -P ./dic/general_password.txt"
	return dict_plugin
	
def doCrack(address,username,password):
	'''
	# ORA-28000 代表账号被锁
	# ORA-01017 代表账号或密码不正确
	# ORA-12505 代表sid不正确
	'''
	
	host = h.getPath(address)
	port = h.getPort(address) if h.getPort(address) !=None else 1521
	## 该处存在问题，如果没有传入参数，也没有报错。
	sid = h.getParameters(address).get('sid')
	service_name = h.getParameters(address).get('service_name')
	
	if sid and sid != None:
		dsn = cx_Oracle.makedsn(host=host, port=port, sid=sid)
	elif service_name and service_name !=None:
		dsn = cx_Oracle.makedsn(host=host, port=port, service_name=service_name)
	else:
		mesg = 'Options sid and service_name cannot be both empty'
		return False,mesg
	
	try:
		fp = cx_Oracle.connect(username, password, dsn, threaded=True)
		code, mesg = '0',fp.version
		return True,mesg
	except cx_Oracle.DatabaseError as e:
		code,mesg = e.args[0].message[:-1].split(': ', 1)
		return False,mesg
	