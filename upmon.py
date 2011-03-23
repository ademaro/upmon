import os, sys

if (sys.platform == "win32"):
    # win
    pkey = 'n'
else:
    # posix
    pkey = 'c'

for hostname in open('servers.list'):
    f = os.popen('ping -' + pkey + ' 1' + str(hostname))
    if f.read().lower().count('ttl'):
        print(("{0} OK").format(hostname))
    else:
        print(("{0} NOK").format(hostname))
