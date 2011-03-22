import os, sys

if (sys.platform == "win32"):
        # win
    ping_arg = '-n 1'
else:
        # posix
    ping_arg = '-c 1'
#else:
#    print ('platform ' + sys.platform + ' is not supported')

for c in open('servers.list'):
        f = os.popen("ping "+ ping_arg+ ' ' + str(c))
        if f.read().lower().count('ttl'):
            print(("{0} DONE").format(c))
        else:
            print(("{0} is down").format(c))
#    else:
#        # POSIX
#        f = os.popen("ping -c 1 " + str(c))
#        if f.read().count('ttl'):
#            print(("{0} DONE").format(c))
#        else:
#            print(("{0} is down").format(c))

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
