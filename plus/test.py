import random

author = 'c0ny1'
help = 'Crack for test'
usa = "Example: python pwcracker.py -t test://tttteeeeessssttttt:80' -u admin -p admin"



def doCrack(address,username,password):
	# print 'address:' + address
	# print 'username:' + username
	# print 'password:' + password
	num = random.randint(0,9)
	if num % 2 == 0:
		return True
	else:
		return False

if __name__ == '__main__':
	print doCrack("zip://c://windows/a.rar","","sssss")