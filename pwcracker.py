#coding=utf-8
import os
import sys
from lib.helper import del_dir
from lib.common import *
from lib.printer import printSuccessMsg,printInfoMsg,printWarningMsg,printErrorMsg,printProgress
from lib.data import *
from lib.cmdline import parse_args,showAllPluInfo,showPluInfo
from lib.config import *
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def crackManager(address,user,pwd):
	print BANNER
	printInfoMsg('Load targets: %d' % len(address))
	printInfoMsg('Load usernames: %d' % len(user))
	printInfoMsg('Load passwords: %d' % len(pwd))
	th.num = 0
	th.find_num = 0
	th.sum = len(address)*len(user)*len(pwd)
	th.start_time = time.time()
	for a in address:
		isSuccess = False
		plusname = a.split(':')[0]
		plu_module = loadplus(plusname)
		
		#爆破前的检查
		if hasattr(plu_module,'doCheck'):
			res,check_msg = plu_module.doCheck(a.strip(),user,pwd)
			if not res:
				printErrorMsg(check_msg)
				break # 到底如何区分此处改是break还是continue，同时又不增加插件编写难度。
		
		printInfoMsg('Start crack target:%s' % a.strip())
		for u in user:
			for p in pwd:
				isSuccess,msg = sys.modules['plus.'+plusname].doCrack(a.strip(),u.strip(),p.strip())
				th.num += 1
				process = ((1.0*th.num)/th.sum)*100
				#process_info = '{0}/{1}({2}%)'.format(num,sum,round(process,2))
				th.process_info = '%d/%d(%.2f)' % (th.num,th.sum,process) + '%'
				printProgress()
				if u.strip() == '':
					info_temp = 'password:%s' % p.strip()
				else:
					info_temp = 'username:%s password:%s' % (u.strip(),p.strip())
				
				if isSuccess == True:
					th.find_num += 1
					if conf.show_detail:
						printSuccessMsg("find %s | %s" % (info_temp,msg))
					else:
						printSuccessMsg(info_temp)
					break
				else:
					if conf.show_detail:
						printErrorMsg("%s | %s" % (info_temp,msg))
						pass
					continue
				time.sleep(0.01)
				
if __name__ == '__main__':
	args = parse_args()
	
	if args.show_plus:
		showAllPluInfo()
	
	if args.show_plugin_info:
		plugin_name = args.show_plugin_info.strip()
		showPluInfo(plugin_name)
		
	if args.target:
		cack_target = [args.target]
	elif args.T:
		cack_target = read_file(args.T)
	else:
		printWarningMsg('please set targets!')
		printInfoMsg('System exit.')
		exit()
	
	if args.username:
		cack_username = [args.username]
	elif args.U:
		cack_username = read_file(args.U)
	else:
		cack_username = ['']
	
	if args.password:
		cack_password = [args.password]
	elif args.pw_file:
		cack_password = read_file(args.pw_file)
	else:
		printWarningMsg('please set password!')
		exit()
	
	if args.show_detail:
		conf.show_detail = True
	else:
		conf.show_detail = False
	
	crackManager(cack_target,cack_username,cack_password)
	printInfoMsg('System exit.')