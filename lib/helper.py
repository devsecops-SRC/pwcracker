#coding=utf-8
import os

#清空文件夹下的文件和子目录
def  del_dir(path):
	for i in os.listdir(path):
		path_file = os.path.join(path,i)  #取文件绝对路径
		if os.path.isfile(path_file):
			os.remove(path_file)
		else:
			del_file(path_file)

def getTmpPath():
	root_path = os.getcwd()
	return root_path + '\\tmp\\'
	
#从地址中解析出协议
def getProtocol(address):
	protocol = address.split("://")[0]
	return protocol

#从地址中解析出路径
def getPath(address):
	protocol = getProtocol(address)
	path = address[len(protocol + '://'):]
	path = path.split('?')[0]
	path = path.split(':')[0]
	return path

def getParameters(address):
	param = {}
	key_value_list = address.split("?")[1].split('&')
	for k_y in key_value_list:
		ky = k_y.split('=')
		param[ky[0]] = ky[1]
	
	return param


#从地址中解析出端口
def getPort(address):
	tmp = address.split(':')
	if len(tmp) >= 3:
		port = tmp[-1].strip()
		try:
			port = int(port)
			return  port
		except:
			return None
	else:
		return None

		
		
def checkIP(ip_str):
	'''
	检查传入的IP是否正确的IP格式
	'''
	rex_ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
	if rex_ip.match(ip_str):  
		return True  
	else:  
		return False

def checkPort(port):
	'''
	检查传入的端口是否是正确的端口范围
	'''
	if type(port) != int:
		return False
	
	if port >= 0 and port <= 65535:
		return True
	else:
		return False

def scanPort(host,port):
	pass
	