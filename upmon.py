import os, sys
import apsw

connection = apsw.Connection("mondb")
cursor = connection.cursor()

def ins_db(hostname = [],repit_t = 5000,ch = False):
        cursor.execute("insert into hosts_for_ping values(?,?,?)", (hostname.replace('\n',''),repit_t,ch))

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

def fetch_hosts(primary = True):
    hostnames = []
    times = []
    for hostname, time in cursor.execute('select h,t  from hosts_for_ping where p=?',(primary,)):
        hostnames.append(hostname)
        times.append(time)
    return hostnames, times

#def fetch_all():
#    hostnames = []
#    for hostname in cursor.execute('select * from hosts_for_ping where p=?',(primary,)):
#        hostnames.append(hostname[0])
#    return hostnames


#создаем таблицу hostname,repeate_time,primary
#cursor.execute("create table hosts_for_ping(h,t,p)")
#cursor.execute("drop table hosts_for_ping")



#for hostname in  cursor.execute('select h from hosts_for_ping'):
#    cursor.execute('update hosts_for_ping set h=?',(str(hostname).replace('\n','',),))


#cursor.execute('drop table hosts_for_ping')


#for hostname, time_limit in cursor.execute('select h,t from hosts_for_ping where p=?',(True,)):
#print(hostname, time_limit)

#  Import DB from file
host_pim = []
hosts_pim = fetch_hosts(False)
print(hosts_pim)

for hostname in hosts_pim[0] :  ###TODO: false -> true
#    ins_db(hostname)
   if ping_host(hostname) is True:
        print(hostname + ' is OK' )
   else:
        print(hostname + ' is DOWN')