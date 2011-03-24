#создаем таблицу с полями hostname,repeate_time_limit,primary
#c.execute("create table hosts_for_ping(h,t,p)")

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

#удаляем таблицу
#cursor.execute("drop table hosts_for_ping")


#for hostname, time_limit in cursor.execute('select h,t from hosts_for_ping where p=?',(True,)):
#print(hostname, time_limit)