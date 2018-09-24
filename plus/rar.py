#coding=utf-8
from unrar import rarfile
from lib.helper import getPath

def plu_info():
	dict_plugin={};
	dict_plugin['name']="rar"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:24"
	dict_plugin['description'] = "Used to crack encrypted rar files."
	dict_plugin["usage"] = "python pwcracker.py -t rar://./test/test.rar -P ./dic/general_password.txt"
	return dict_plugin

def doCrack(address,username,password):
	try:
		filename = getPath(address)
		print filename
		#rfile = rarfile.RarFile(filename)
		#rfile.extractall(path=getTmpPath(), pwd=password)
		return True,None
	except:
		return False,u'解压失败'

if __name__ == '__main__':
	doCrack("rar://F:/Code/python/pwcracker/test/test.rar","","admin")