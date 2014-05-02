#! /usr/bin/python
#!encoding: UTF-8

import time
import timeit
import os
import platform
import shutil
   
def CPUinfo():
   #infofile on Linux machines:
   infofile = '/proc/cpuinfo'
   cpuinfo = {}
   if os.path.isfile(infofile):
      f = open(infofile, 'r')
      for line in f:
	 try:
	    name, value = [w.strip() for w in line.split(':')]
	 except:
	    continue
	 if name == 'model name':
	    cpuinfo['CPU type'] = value

	 elif name == 'cache size':
	    cpuinfo['cache size'] = value
	 elif name == 'cpu MHz':
	    cpuinfo['CPU speed'] = value + 'Hz'
	 elif name == 'vendor_id':
	    cpuinfo['vendor ID'] = value
      f.close()
   return cpuinfo
   
   
#Cuerpo principal si lo ejecutamos
if __name__=="__main__":
   f= open("fichero.txt", "w")
   #time
   f.write('time' + '\n')
   eO = time.time()   #Unix epoch time
   cO = time.time()  #CPU time
   f.write('elapsed_time' + '\n')
   elapsed_time = time.time() - eO
   f.write(str((elapsed_time)) + '\n')
   f.write('cpu_time' + '\n')
   cpu_time = time.clock() - cO
   f.write(str(cpu_time) + '\n')
   f.write('\n')
   #timeit
   f.write('timeit' + '\n')
   t_upla_valor = (10, 100, 1000, 10000, 100000, 1000000, 10000000)
   for i in range (len(t_upla_valor)):
      t = timeit.Timer('sin(1.2)', setup='from math import sin')
      t.timeit(t_upla_valor[i])
      f.write(str(t_upla_valor[i]) + '\n')
      f.write('sin(1.2)= ')
      f.write(str(t.timeit(t_upla_valor[i])) + '\n')
      t = timeit.Timer('math.sin(1.2)', setup='import math')
      t.timeit(t_upla_valor[i])
      f.write('math.sin(1.2)= ')
      f.write(str(t.timeit(t_upla_valor[i])) + '\n')
   #CPU
   f.write('\n')
   f.write('CPU' + '\n')
   f.write(str(CPUinfo()) + '\n')
   #Sistema operativo y compilador
   f.write('\n')
   f.write('platform' + '\n')
   f.write('platform.uname()' + '\n')
   a=platform.uname()
   f.write(str(a) + '\n')
   f.write('platform.platform()' + '\n')
   b=platform.platform()
   f.write(str(b) + '\n')
   f.write('platform.python_version()' + '\n')
   c=platform.python_version()
   f.write(str(c) + '\n')
   f.write('platform.python_buil()' + '\n')
   d=platform.python_build()
   f.write(str(d) + '\n')
   f.close
   