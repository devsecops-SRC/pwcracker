#coding=utf-8
import zipfile

def plu_info():
	dict_plugin={};
	dict_plugin['name']="zip"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:29"
	dict_plugin['description'] = "Used to crack encrypted zip files."
	dict_plugin["usage"] = "python pwcracker.py -t zip://./test/test.zip -P ./dic/general_password.txt"
	return dict_plugin


def doCrack(address,username,password):
	try:
		xieyi = address.split('://')[0]
		filename = address[len(xieyi+'://'):]
		zfile = zipfile.ZipFile(filename)
		zfile.extractall(pwd=password)
		return True,None
	except:
		return False,u'解压失败！'