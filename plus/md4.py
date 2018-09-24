#coding=utf-8
from Crypto.Hash import MD4
from lib.helper import getPath

def plu_info():
	dict_plugin={};
	dict_plugin['name']="md4"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"
	dict_plugin['description'] = "Used to crack MD4 ciphertext."
	dict_plugin["usage"] = "python pwcracker.py -t md4://f9d4049dd6a4dc35d40e5265954b2a46 -P ./dic/general_password.txt"
	return dict_plugin

def doCheck(address,username,password):
	hash_str = getPath(address)

	if len(hash_str) != 32:
		return False,u'%s格式错误，md4密文长度应该为32！' % hash_str	
	elif not (len(username) == 1 and username[0] == ''):
		return False,u'md4破解，无需设置账号！'
	else:
		return True,None

def doCrack(address,username,password):
	hash_str = getPath(address)
	m = MD4.new()
	m.update(password)
	encrypt_str = m.hexdigest()
	if encrypt_str.lower() == hash_str.lower():
		return True,'Crack success!'
	else:
		return False,'Crack fail!'