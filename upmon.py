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
        ans_time = 50#TODO f.read()[:]
        return ans_time
    else:
        return 0

def hlp():
    print('''Usage: [function] [parameters] \n
      [function] \n
        add hostname [time(default 5000)]  - to add host in DB\n
        del hostname - to delete host from DB\n
          example:\n
           upmon.py add 192.168.1.1 5000\n
           upmon.py del dev.z-gu.ru
                        ''')


def read_arg():
    args = []
    for arg in sys.argv[2:4]:
      args.append(arg)
    if len(args) ==1 :
        return args[0]
    else:
        print(args[0],args[1])
        return args[0] #, args[1]  #TODO: убрать костыль
    
def ins_db(hostname = [],repit_t = 5000,ch = True):
    try:
        c.execute('create table hosts_for_ping(h,t,p)')
    except sqlite3.OperationalError:
        c.execute("insert into hosts_for_ping values(?,?,?)", (hostname,repit_t,ch))
        connection.commit()

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



if len(sys.argv) > 1:
    if sys.argv[1] in ('-h','-help','--help'):
        hlp()
    elif sys.argv[1] == 'add':                  #если добавляем
        ins_db(read_arg())

###c.execute('drop table ping_stat')


host_primary = []
hosts_primary = fetch_hosts()
for hostname in hosts_primary[0]:
#    ins_db(hostname)
    servname = 'test'#TODO insert servn
    try:
        c.execute('create table ping_stat(h,s,t)')
    except sqlite3.OperationalError:
        c.execute("insert into ping_stat values(?,?,?)", (hostname,servname,ping_host(hostname)))
        connection.commit()


        
print('Первая табл\n')
for i in c.execute('select * from hosts_for_ping'):
    print(i)
print('\n2 табл\n')
for i in c.execute('select * from ping_stat'):
    print(i)
c.close()