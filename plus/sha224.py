#coding=utf-8
import hashlib
from lib.helper import getPath

def plu_info():
	dict_plugin={};
	dict_plugin['name']="sha224"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"
	dict_plugin['description'] = "Used to crack SHA224 ciphertext."
	dict_plugin["usage"] = "python pwcracker.py -t sha224://58acb7acccce58ffa8b953b12b5a7702bd42dae441c1ad85057fa70b -P ./dic/general_password.txt"
	return dict_plugin

def doCheck(address,username,password):
	hash_str = getPath(address)
	if len(hash_str) != 56:
		return False,u'%s格式错误，sha224密文长度应该为56！' % hash_str	
	elif not (len(username) == 1 and username[0] == ''):
		return False,u'sha224破解，无需设置账号！'
	else:
		return True,None

def doCrack(address,username,password):
	hash_str = getPath(address)
	m = hashlib.sha224()
	m.update(password)
	encrypt_str = m.hexdigest()
	if encrypt_str.lower() == hash_str.lower():
		return True,'Crack success!'
	else:
		return False,'Crack fail!'
