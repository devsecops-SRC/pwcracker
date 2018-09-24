#coding=utf-8
import hashlib
from lib.helper import getPath

def plu_info():
	dict_plugin={};
	dict_plugin['name']="sha384"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"
	dict_plugin['description'] = "Used to crack SHA384 ciphertext."
	dict_plugin["usage"] = "python pwcracker.py -t sha384://9ca694a90285c034432c9550421b7b9dbd5c0f4b6673f05f6dbce58052ba20e4248041956ee8c9a2ec9f10290cdc0782 -P ./dic/general_password.txt"
	return dict_plugin

def doCheck(address,username,password):
	hash_str = getPath(address)
	if len(hash_str) != 96:
		return False,u'%s格式错误，sha384密文长度应该为96！' % hash_str	
	elif not (len(username) == 1 and username[0] == ''):
		return False,u'sha384破解，无需设置账号！'
	else:
		return True,None

def doCrack(address,username,password):
	hash_str = getPath(address)
	m = hashlib.sha384()
	m.update(password)
	encrypt_str = m.hexdigest()
	if encrypt_str.lower() == hash_str.lower():
		return True,u'Crack success!'
	else:
		return False,u'Crack fail!'