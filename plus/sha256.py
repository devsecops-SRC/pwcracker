#coding=utf-8
import hashlib
from lib.helper import getPath

puls_author = 'c0ny1'
puls_dest = 'Crack for sha256'
puls_help = 'Example:  -p admin'

def plu_info():
	dict_plugin={};
	dict_plugin['name']="sha256"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"
	dict_plugin['description'] = "Used to crack SHA256 ciphertext."
	dict_plugin["usage"] = "python pwcracker.py -t sha256://8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918 -P ./dic/general_password.txt"
	return dict_plugin

def doCheck(address,username,password):
	hash_str = getPath(address)
	if len(hash_str) != 64:
		return False,u'%s格式错误，sha256密文长度应该为64！' % hash_str	
	elif not (len(username) == 1 and username[0] == ''):
		return False,u'sha256破解，无需设置账号！'
	else:
		return True,None

def doCrack(address,username,password):
	hash_str = getPath(address)
	m = hashlib.sha256()
	m.update(password)
	encrypt_str = m.hexdigest()
	if encrypt_str.lower() == hash_str.lower():
		return True,u'Crack success!'
	else:
		return False,'Crack fail!'#搞不懂这里加u就报编码错误