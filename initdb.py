import sqlite3

connection =  sqlite3.connect("upmondb")
c = connection.cursor()

#создаем таблицу с полями hostname,repeate_time_limit,primary
#c.execute("create table hosts_for_ping(h,t,p)")

#создаем таблицу с полями hostname,time_check,servname,answer_time
c.execute("create table hosts_status(h,t,s,a)")

#init Import DB from file
#for hostname in open('servers.list'):
#    c.execute('update hosts_for_ping set h=?',(str(hostname).replace('\n','',),))

#or insert init data
#for h in [('mysql.z-gu.ru', 5000, True),
#          ('stat.z-gu.ru',  5000, True),
#          ('tea.z-gu.ru',   5000, True),
#          ('koc.z-gu.ru',   5000, True),
#         ]:
#    c.execute('insert into hosts_for_ping values (?,?,?)', h)

#save changes
connection.commit()

#удаляем таблицу
#cursor.execute("drop table hosts_for_ping")

print('all changes writen')
#close the cursor if we are done with it
c.close()

#hz:
#for hostname, time_limit in cursor.execute('select h,t from hosts_for_ping where p=?',(True,)):
#print(hostname, time_limit)

#def ins_db(hostname = [],repit_t = 5000,ch = False):
#    c.execute("insert into hosts_for_ping values(?,?,?)", (hostname.replace('\n',''),repit_t,ch))

