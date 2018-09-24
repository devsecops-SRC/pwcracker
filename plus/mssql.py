#coding=utf-8

from lib import helper as h
from lib.config import IS_WIN
if IS_WIN:
	import pymssql
else:
	from impacket import tds
	from impacket.tds import TDS_ERROR_TOKEN, TDS_LOGINACK_TOKEN

def plu_info():
	dict_plugin = {};
	dict_plugin['name'] = "mssql"
	dict_plugin['author'] = "c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:13"
	dict_plugin['description'] = "Used to guess SQL Server database password."
	dict_plugin["usage"] = "python pwcracker.py -t mssql://192.168.1.108:1433 -u sa -P ./dic/general_password.txt"
	return dict_plugin
	
def doCrack(address,username,password):
	if IS_WIN:
		return crack_in_windows(address,username,password)
	else:
		return crack_in_linux(address,username,password)

def crack_in_linux(address,username,password):
	'''
	中文提示：用户 'sa' 登录失败。
	英文提示：Login failed for user
	经过测试在linux下成功
	window7下报错：struct.error: ('unpack requires a string argument of length 1', "When unpacking field 'Type | <B | ''[:1]'")
	'''
	host = h.getPath(address)
	port = h.getPort(address) if h.getPort(address) != None else 1433
	
	fp = tds.MSSQL(host, int(port))
	fp.connect()
	r = fp.login(None, username, password, None, None, False)
	# 第二种登录方式：r = fp.login(None, username, password, domain, password_hash, True)
	if not r:
		key = fp.replies[TDS_ERROR_TOKEN][0]
		code = key['Number']
		mesg = key['MsgText'].decode('utf-16le')
	else:
		key = fp.replies[TDS_LOGINACK_TOKEN][0]
		code = '0'
		mesg = '%s (%d%d %d%d)' % (key['ProgName'].decode('utf-16le'), key['MajorVer'], key['MinorVer'], key['BuildNumHi'], key['BuildNumLow'])

	fp.disconnect()
	code = int(code)
	if code == 0:
		return True,mesg
	elif code == 18456:
		return False,mesg
	else:
		return False,mesg

def crack_in_windows(address,username,password):
	host = h.getPath(address)
	port = h.getPort(address) if h.getPort(address) != None else 1433

	try:
		db = pymssql.connect(server=host, port=port, user=username, password=password)
		return True,None
	except Exception, e:
		return False,str(e)