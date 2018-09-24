#coding=utf-8
import hashlib
from lib.helper import getPath

def plu_info():
	dict_plugin={};
	dict_plugin['name']="sha512"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"	
	dict_plugin['description'] = "Used to crack SHA512 ciphertext."
	dict_plugin["usage"] = "python pwcracker.py -t sha512://c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec -P ./dic/general_password.txt"
	return dict_plugin

def doCheck(address,username_list,password_list):
	hash_str = getPath(address)
	if len(hash_str) != 128:
		return False,u'%s格式错误，sha512密文长度应该为128！' % hash_str	
	elif not (len(username_list) == 1 and username_list[0] == ''):
		return False,u'sha512破解，无需设置账号！'
	else:
		return True,None
		
def doCrack(address,username,password):
	hash_str = getPath(address)
	m = hashlib.sha512()
	m.update(password)
	encrypt_str = m.hexdigest()
	if encrypt_str.lower() == hash_str.lower():
		return True,u'Crack success!'
	else:
		return False,u'Crack fail!'