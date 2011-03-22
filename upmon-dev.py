#!/usr/bin/env python
# coding=utf-8

import ping, socket
try:
    delay = ping.do_one('z-gu.ru', timeout=2)
    print ("OK")
except socket.error as e:
    print ("Ping Error:", e)

"""
import subprocess

host = "mysql.z-ru.ru"

ping = subprocess.Popen(
    ["ping", "-c", "1", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print (out)
"""

#import re
#matcher = re.compile("round-trip min/avg/max/stddev = (\d+.\d+)/(\d+.\d+)/(\d+.\d+)/(\d+.\d+)")
#print (matcher.match(out).groups())