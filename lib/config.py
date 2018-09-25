import subprocess

AUTHOR = 'c0ny1'
VERSION = '0.1'
MAIL = 'root@gv7.me'
IS_WIN = subprocess.mswindows
UNICODE_ENCODING = "utf-8"


BANNER = """\033[01;32m	  
    ____     __  __  __             \033[01;32m_____\033[01;32m
   / __ \   / / / / / / \033[01;31m  \__/     \033[01;32m/ ___/\033[01;32m 
  / /_/ /  / /_/ /_/ /  \033[01;31m--(__)--  \033[01;32m/ /___ \033[01;32m  
 /  ___/   \________/   \033[01;31m  /  \    \033[01;32m\____/\033[01;32m
/_/ \033[01;37m\\\033[01;34mVersion %s by %s mail:%s\033[01;37m/\033[0m                    
\n""" % (VERSION, AUTHOR, MAIL)