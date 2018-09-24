#coding=utf-8
from Crypto.Hash import MD2
from lib.helper import getPath

def plu_info():
	dict_plugin={};
	dict_plugin['name']="md2"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:23"
	dict_plugin['description'] = "Used to crack MD2 ciphertext."
	dict_plugin["usage"] = "python pwcracker.py -t md2://3e3e6b0e5c1c68644fc5ce3cf060211d -P ./dic/general_password.txt"
	return dict_plugin


def doCheck(address,username,password):
	hash_str = getPath(address)

	if len(hash_str) != 32:
		return False,u'%s格式错误，md2密文长度应该为32！' % hash_str	
	elif not (len(username) == 1 and username[0] == ''):
		return False,u'md2破解，无需设置账号！'
	else:
		return True,None

def doCrack(address,username,password):
	hash_str = getPath(address)
	m = MD2.new()
	m.update(password)
	encrypt_str = m.hexdigest()
	if encrypt_str.lower() == hash_str.lower():
		return True,'Crack success!'
	else:
		return False,'Crack fail!'