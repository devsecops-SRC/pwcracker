import os
import sys
import argparse
import glob
from lib.common import *
from lib.printer import printInfoMsg

def parse_args():
	parser = argparse.ArgumentParser(prog='pwcracker',
									formatter_class=argparse.RawTextHelpFormatter,
									description='* An expandable password cracking framework. *\n'
												'By c0ny1 (http://gv7.me)',
									usage='pwcracker.py [options]')
									
	crack_option = parser.add_argument_group('CRACK')
	crack_option.add_argument('-t',metavar='TARGET',dest='target', type=str, default='', 
						help='The target to crack,target format:protocol://path:port')
						
	crack_option.add_argument_group('DIC')
	crack_option.add_argument('-T', metavar='FILE', type=str, default='',
						help='Load the target file to be cracked.')
	
	crack_option.add_argument('-u','--username', metavar="USERNAME",dest='username', default='',
						help='The user name to crack.')
						
	crack_option.add_argument('-U', metavar="FILE",dest='U', default='',
						help='The user name dictionary file to load.')

	crack_option.add_argument('-p', '--password', metavar="PASSWORD",dest='password', default='',
						help='Passwords to crack.')

	crack_option.add_argument('-P', metavar="FILE",dest='pw_file', type=str ,default='',
						help='Load the password dictionary file to be cracked.')
						
	crack_option.add_argument_group('OTHER')
	crack_option.add_argument('-r', metavar='THREADS', type=int, default=3,
						help='Num of scan threads for each scan process, 3 by default')
	
	show_option = parser.add_argument_group('SHOW')
	show_option.add_argument('-s', '--show', dest='show_plus', default=False, action='store_true',
						help='Show all plugins')

	show_option.add_argument('-i', '--info', metavar="PLUGIN_NAME",dest='show_plugin_info', default='', 
						help='Show one plugins')
	
	show_option.add_argument('-v', dest='show_detail', default=False, action='store_true',
				help='Show the details of the cracking password.')
	show_option.add_argument('-V','--version' ,action='version', version='%(prog)s 0.1\nBy c0ny1 (http://gv7.me)')

	if len(sys.argv) == 1:
		sys.argv.append('-h')

	args = parser.parse_args()
	#check_args(args)
	return args

def showAllPluInfo():
	module_name_list = glob.glob(os.path.join('./plus/', '*.py'))	
	msg = 'Plugin Name (total:%s)\n' % str(len(module_name_list) - 1)
	for each in module_name_list:
		_str = os.path.splitext(os.path.split(each)[1])[0]
		if _str not in ['__init__']:
			msg += '[+] %s\n' % _str	
	sys.exit(msg)

def getPlugInfo(plusname):
	loadplus(plusname)
	info = sys.modules['plus.'+plusname].plu_info()
	plus_info = {}
	
	plus_info['name'] = plusname
	
	try:
		plus_info['author'] = info.get('author')
	except:
		plus_info['author'] = 'unknown'

	try:
		plus_info['date'] = info.get('date')
	except:
		plus_info['date'] = 'unknown'
		
	try:
		plus_info['description'] = info.get('description')
	except:
		plus_info['author'] = 'NULL'
	
	try:
		plus_info['usage'] = info.get('usage')
	except:
		plus_info['usage'] = 'NULL'
		
	return plus_info

def showPluInfo(plusname):
	plu_info = getPlugInfo(plusname)
	print '[+] name:' + str(plu_info.get('name'))
	print '[+] author:' + str(plu_info.get('author'))
	print '[+] date:' + str(plu_info.get('date'))
	print '[+] description:' + str(plu_info.get('description'))
	print '[+] usage:' + str(plu_info.get('usage'))
	printInfoMsg('System exit.')
	exit()
		
if __name__ == '__main__':
	showAllPluInfo()