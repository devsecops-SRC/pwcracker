#coding=utf-8
import MySQLdb
from lib.helper import getPath,getPort


plugin_help = "python pwcracker.py -t mysql://127.0.0.1:3306 -u root -p root"

def plu_info():
	dict_plugin = {};
	dict_plugin['name'] = "mysql"
	dict_plugin['author'] = "c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 17:57"
	dict_plugin['description'] = "Used to guess MySQL database password."
	dict_plugin["usage"] = "python pwcracker.py -t mysql://192.168.1.108:3306 -u root -P ./dic/general_password.txt"
	return dict_plugin
	
def doCrack(address,username,password):
	host = getPath(address)
	port = getPort(address)
	db=None 
	try: 
		db=MySQLdb.connect(host=host,user=username,passwd=password,db='mysql',port=int(port))
		return True,u'Crack success!'
	except: 
		return False,u'Crack fail!'
	finally: 
		if db: 
			db.close() 