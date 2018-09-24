#coding=utf-8
import PyPDF2
import sys
from lib.helper import getPath


def plu_info():
	dict_plugin={};
	dict_plugin['name']="pdf"
	dict_plugin['author']="c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:24"
	dict_plugin['description'] = "Used to crack encrypted pdf files."
	dict_plugin["usage"] = "python pwcracker.py -t pdf://./test/test.pdf -P ./dic/general_password.txt"
	return dict_plugin


def doCrack(address,username,password):
	filename = getPath(address)
	pdfReader = PyPDF2.PdfFileReader(open(filename,'rb'))

	if pdfReader.isEncrypted:
		if pdfReader.decrypt(password):
			return True,u'破解成功'
		else:
			return False,u'破解失败'
	else:
		return False,u'该pdf未加密'


if __name__ == '__main__':
	doCrack('pdf://../test/test.pdf','','admin')