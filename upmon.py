import os, sys

def ping_host(srv_hostname):
    if (sys.platform == "win32"):
        # win
        pkey = 'n'
    else:
        # posix
        pkey = 'c'
    f = os.popen('ping -' + pkey + ' 1 ' + str(srv_hostname))
    if f.read().lower().count('ttl'):
        return True

for hostname in open('servers.list'):
    if ping_host(hostname) is True:
        print(hostname[:(len(hostname)-1)] + ' is OK')
    else:
        print(hostname[:(len(hostname)-1)] + ' is DOWN')



