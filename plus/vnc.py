from lib import helper as h
from time import time,sleep
import socket
from Crypto.Cipher import DES

class Timing:
	def __enter__(self):
		self.t1 = time()
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.time = time() - self.t1

class VNC_Error(Exception):
  pass

class VNC:
  def connect(self, host, port, timeout):
    self.fp = socket.create_connection((host, port), timeout=timeout)
    resp = self.fp.recv(99) # banner

    #print 'banner: %r' % resp
    self.version = resp[:11]

    if len(resp) > 12:
      raise VNC_Error('%s %r' % (self.version, resp[12:]))

    return self.version

  def login(self, password):
    #print 'Remote version: %r' % self.version
    major, minor = self.version[6], self.version[10]

    if (major, minor) in [('3', '8'), ('4', '1')]:
      proto = 'RFB 003.008\n'

    elif (major, minor) == ('3', '7'):
      proto = 'RFB 003.007\n'

    else:
      proto = 'RFB 003.003\n'

    #print 'Client version: %r' % proto[:-1]
    self.fp.sendall(proto)

    sleep(0.5)

    resp = self.fp.recv(99)
    #print 'Security types supported: %r' % resp

    if major == '4' or (major == '3' and int(minor) >= 7):
      code = ord(resp[0:1])
      if code == 0:
        raise VNC_Error('Session setup failed: %s' % B(resp))

      self.fp.sendall(b'\x02') # always use classic VNC authentication
      resp = self.fp.recv(99)

    else: # minor == '3':
      code = ord(resp[3:4])
      if code != 2:
        raise VNC_Error('Session setup failed: %s' % resp)

      resp = resp[-16:]

    if len(resp) != 16:
      raise VNC_Error('Unexpected challenge size (No authentication required? Unsupported authentication type?)')

    #print 'challenge: %r' % resp
    pw = password.ljust(8, '\x00')[:8] # make sure it is 8 chars long, zero padded
    key = self.gen_key(pw)
    #print 'key: %r' % key

    des = DES.new(key, DES.MODE_ECB)
    enc = des.encrypt(resp)

    #print 'enc: %r' % enc
    self.fp.sendall(enc)

    resp = self.fp.recv(99)
    #print 'resp: %r' % resp

    code = ord(resp[3:4])
    mesg = resp[8:]

    if code == 1:
      return code, mesg or 'Authentication failure'

    elif code == 0:
      return code, mesg or 'OK'

    else:
      raise VNC_Error('Unknown response: %r (code: %s)' % (resp, code))


  def gen_key(self, key):
    newkey = []
    for ki in range(len(key)):
      bsrc = ord(key[ki])
      btgt = 0
      for i in range(8):
        if bsrc & (1 << i):
          btgt = btgt | (1 << 7-i)
      newkey.append(btgt)

    return ''.join(chr(c) for c in newkey)

def plu_info():
	dict_plugin = {};
	dict_plugin['name'] = "vnc"
	dict_plugin['author'] = "c0ny1<root@gv7.me>"
	dict_plugin['date'] = "2018-09-24 18:24"
	dict_plugin['description'] = "Used to guess SQL Server database password."
	dict_plugin["usage"] = "python pwcracker.py -t vnc://192.168.1.108:5900 -u root -P ./dic/general_password.txt"
	return dict_plugin
	  
def doCrack(address,username,password=None):
	v = VNC()
	host = h.getPath(address)
	port = h.getPort(address)
	timeout='10'
	try:
		with Timing() as timing:
			code, mesg = 0, v.connect(host, int(port or 5900), int(timeout))

		with Timing() as timing:
			code, mesg = v.login(password)

	except VNC_Error as e:
		#print 'VNC_Error: %s' % e
		code, mesg = 2, str(e)
	print code,mesg
	if code == 0:
		return True,u'Crack success!'
	elif code == 1:
		return False,u'Crack fail!'
	else:
		return False,u'Crack fail!'