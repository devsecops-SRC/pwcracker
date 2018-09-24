#coding=utf-8
import hashlib
from lib.helper import getPath

def plu_info():
	dict_plugin={};
	dict_plugin['name']="md5"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"
	dict_plugin['description'] = "Used to crack MD5 ciphertext."
	dict_plugin["usage"] = "python pwcracker.py -t md5://21232f297a57a5a743894a0e4a801fc3 -P ./dic/general_password.txt"
	return dict_plugin

def doCheck(address,username,password):
	hash_str = getPath(address)
	if len(hash_str) != 16 and len(hash_str) != 32:
		return False,u'%s格式错误，md5密文长度应该为16或者32！' % hash_str	
	elif not (len(username) == 1 and username[0] == ''):
		return False,u'md5破解，无需设置账号！'
	else:
		return True,None

def doCrack(address,username,password):
	hash_str = getPath(address)
	m = hashlib.md5()
	m.update(password)
	encrypt_str = m.hexdigest()
	if encrypt_str.lower() == hash_str.lower():
		return True,'Crack success!'
	else:
		return False,'Crack fail!'