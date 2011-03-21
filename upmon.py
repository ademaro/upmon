import os, sys

for c in open('servers.list'):
#	f = os.popen("ping -n 1 " + str(c))     #for win.os
	f = os.popen("ping -c 1 " + str(c))
	if f.read().count('ttl'):
		print(("{0} DONE").format(c))
	else:
		print(("{0} is down").format(c))

# cmd1 = 'ping -n 1 ' + str(c)
# f = subprocess.getstatusoutput(cmd1)
# print(str(f).encode())
# f = str(f)
# print(f)
# if f.count('TTL=62') > 0:
# print('DONE '*5)
# else:
# print('FALSE '*5)
# for ttl in f[0:]:
# print (ttl)
# if 'TTL' in ttl:
# print('done')
