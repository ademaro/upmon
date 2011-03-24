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

#создаем таблицу с полями hostname,repeate_time_limit,primary
c.execute("create table hosts_for_ping(h,t,p)")

#init Import DB from file
#for hostname in open('servers.list'):
#    c.execute('update hosts_for_ping set h=?',(str(hostname).replace('\n','',),))
#or insert init data
for h in [('mysql.z-gu.ru', 5000, True),
          ('stat.z-gu.ru',  5000, True),
          ('tea.z-gu.ru',   5000, True),
          ('koc.z-gu.ru',   5000, True),
         ]:
    c.execute('insert into hosts_for_ping values (?,?,?)', h)

#удаляем таблицу
#cursor.execute("drop table hosts_for_ping")


#for hostname, time_limit in cursor.execute('select h,t from hosts_for_ping where p=?',(True,)):
#print(hostname, time_limit)

host_pim = []
hosts_pim = fetch_hosts()
print(hosts_pim)

for hostname in hosts_pim[0] :  ###TODO: false -> true
#    ins_db(hostname)
   if ping_host(hostname) is True:
        print(hostname + ' is OK' )
   else:
        print(hostname + ' is DOWN')