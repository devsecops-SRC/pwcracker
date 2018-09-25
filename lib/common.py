#coding=utf-8

import os
import sys
from lib.printer import printInfoMsg,printErrorMsg

def read_file(filepath):
	f = open(filepath).readlines()
	return f

def loadplus(plusname):
	plus_path = './plus/' + plusname + '.py'
	if os.path.lexists(plus_path)==True:
		__import__('plus.'+plusname)
		printInfoMsg('Load plugin: %s.py' % plusname)
		return sys.modules['plus.'+plusname]
	else:
		msg = u'Load Pulign Failed: %s.py插件不存在！' % plusname
		printErrorMsg(msg)
		printInfoMsg('System exit!')
		exit()