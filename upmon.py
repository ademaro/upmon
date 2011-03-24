import os, sys
import sqlite3

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

#def ins_db(hostname = [],repit_t = 5000,ch = False):
#    c.execute("insert into hosts_for_ping values(?,?,?)", (hostname.replace('\n',''),repit_t,ch))

def fetch_hosts(primary = True):
    hostnames = []
    times = []
    for hostname, time in c.execute('select h,t  from hosts_for_ping where p=?',(primary,)):
        hostnames.append(hostname)
        times.append(time)
    return hostnames, times

#def fetch_all():
#    hostnames = []
#    for hostname in cursor.execute('select * from hosts_for_ping where p=?',(primary,)):
#        hostnames.append(hostname[0])
#    return hostnames


connection =  sqlite3.connect("upmondb")
c = connection.cursor()

host_pim = []
hosts_pim = fetch_hosts()
print(hosts_pim)

for hostname in hosts_pim[0]:
#    ins_db(hostname)
   if ping_host(hostname) is True:
        print(hostname + ' is OK' )
   else:
        print(hostname + ' is DOWN')