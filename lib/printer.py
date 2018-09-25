#coding=utf-8

import sys
from lib.console import getTerminalSize
from lib.data import th
import time

COLOR_BLACK = 30
COLOR_RED = 31
COLOR_GREEN = 32
COLOR_YELLOW = 33
COLOR_BLUE = 34
COLOR_MAGENTA = 35
COLOR_CYAN = 36
COLOR_WHITE = 37

console_width = getTerminalSize()[0] - 2

def printSuccessMsg(msg):
	msg = '[+] %s' % (msg)
	printMessage(msg,COLOR_GREEN)

def printInfoMsg(msg):
	msg = '[*] %s' % (msg)
	printMessage(msg,COLOR_BLUE)

def printWarningMsg(msg):
	msg = '[!] %s' % (msg)
	printMessage(msg,COLOR_YELLOW)

def printErrorMsg(msg):
	msg = '[-] %s' % (msg)
	printMessage(msg,COLOR_RED)
	
def printMessage(msg,color):
	'''
	success 绿 [+]
	info 蓝 [*]
	warning 黄 [!]
	error 红 [-]
	'''
	
	msg_len = len(msg)
	msg = setColor(msg,color)
	out = '\r' + msg + ' ' * (console_width - msg_len) + '\n\r'
	dataToStdout(out)
	
def printProgress():
	msg = '%s found | %s | cracked in %.2f seconds' % (th.find_num,th.process_info,time.time() - th.start_time)
	out = '\r' + ' ' * (console_width - len(msg)) + msg
	dataToStdout(out)

def setColor(str,color):
	render_str = '\033[1;%dm%s\033[0m' % (color,str)
	return render_str

def dataToStdout(msg):
	"""
	Writes text to the stdout (console) stream
	"""
	sys.stdout.write(msg)
	try:
		sys.stdout.flush()
	except IOError:
		pass
	return
	
