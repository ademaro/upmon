import os, sys
import sqlite3
import ping_delay
import threading
from platform import node

SERVERNAME = node()

class Ping_host(threading.Thread):

    def __init__(self, host):
        self.host = host
        threading.Thread.__init__(self)

    def run(self):
        print('bbbb ',self.host, 'self_host \n', ping_delay.ping_result(self.host))
        sqlite3.connect("upmondb").cursor().execute("insert into ping_stat values(?,?,?)", (self.host,'koc',ping_delay.ping_result(self.host)))
#        ping_add_result_in_db(self.host)



def hlp():
    print('''Usage: [function] [parameters] \n
      [function] \n
        -add hostname [time(default 5000)]  - to add host in DB\n
        -del hostname - to delete host from DB\n
        -d - to run demon
          example:\n
           upmon.py -add 192.168.1.1 5000\n
           upmon.py -del dev.z-gu.ru
                        ''')
def ping_add_result_in_db (hostname):
        ho = ping_delay.ping_result((hostname))
        c.execute("insert into ping_stat values(?,?,?)", (hostname,SERVERNAME,ho))
        connection.commit()

def ins_db(hostname,repit_t = 5000,ch = True):
    try:
        c.execute('create table hosts_for_ping(h,t,p)')
    except sqlite3.OperationalError: pass
    else:
        c.execute("insert into hosts_for_ping values(?,?,?)", (hostname,repit_t,ch))
        connection.commit()
        c.close()

def del_db(hostmane):
    try:
        c.execute('delete from hosts_for_ping where h=?',(hostmane,))
    except sqlite3.OperationalError:
        print("""Host dont find \n
              enter correct hostname""")
    else:
        connection.commit()
        c.close()

def fetch_hosts(primary = True):
    hostnames = []
    times = []
    try:
        for hostname, time in c.execute('select h,t  from hosts_for_ping where p=?',(primary,)):
            hostnames.append(hostname)
            times.append(time)
    except sqlite3.OperationalError:
        print('DB is empty, add host first \n')
        hlp()
    else:
        c.close()
        return hostnames, times


connection =  sqlite3.connect("upmondb")
c = connection.cursor()
hosts_primary = []
h_times = []
hosts_primary , h_times = fetch_hosts()


#try:
#    c.execute('create table ping_stat(h,s,t)')
#except sqlite3.OperationalError:                   :TODO разобраться как это должно выглядеть
#    pass
if len(sys.argv) > 1:
    try:
        if sys.argv[1] in ('-h','-help','--help'):
            hlp()
        elif sys.argv[1] == '-add':             #Р ВµРЎРѓР В»Р С‘ Р Т‘Р С•Р В±Р В°Р Р†Р В»РЎРЏР ВµР С
            if len(sys.argv) == 3:
                ins_db(sys.argv[2])
            else:
                ins_db(sys.argv[2],sys.argv[3])
        elif sys.argv[1] == '-del':
            del_db(sys.argv[2])
#        elif sys.argv[1] == '-d':
#            while True:
#                ping_add_result_in_db()
    except IndexError:
        print(hlp())


for hostname in hosts_primary:
    print (hostname, 'hostname \n !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
    Ping_host(hostname).start()


#print('Table 1\n')
#for i in c.execute('select * from hosts_for_ping'):
#    print(i, ' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
#print('Table 2\n')
#for i in c.execute('select * from ping_stat'):
#    print(i)
c.close()