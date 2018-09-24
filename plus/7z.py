#coding=utf-8
import sys
import os
from os import system
from lib.helper import del_dir

exe7z = "D:\\software\\7-Zip\\7z.exe" #7z.exe在系统中的路径

def plu_info():
	dict_plugin={};
	dict_plugin['name']="7z"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:24"
	dict_plugin['description'] = "Used to crack encrypted 7z files."
	dict_plugin["usage"] = "python pwcracker.py -t 7z://./test/test.7z -P ./dic/general_password.txt"
	return dict_plugin


def doCheck(address,usernames,passwords):
	if not (exe7z and os.path.lexists(exe7z)==True):
		return False,u'please set 7z.exe of path(exe7z) in your system!'
	else:
		return True,None

def doCrack(address,username,password):
	'''
	result = 0为解压成功，2为解压失败。
	'''
	#print sys.path[0],os.getcwd()
	tmp_path = os.getcwd() + '\\tmp\\crack7z'
	xieyi = address.split('://')[0]
	filename = address[len(xieyi+'://'):]
	cmd = '%s x %s -o%s -p%s' % (exe7z,filename,tmp_path,password)
	res = system(cmd,)
	if res == 0:
		del_dir(tmp_path)
		return True,u'解压成功'
	else:
		return False,u'解压失败'
	
