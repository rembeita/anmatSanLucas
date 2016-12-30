#!/usr/bin/python
from ObtenerArchivo import ObtenerArchivo
import sys, time
from daemon import Daemon

def Sistema():
	archivo = ObtenerArchivo()
	filedata = archivo.leerInfo("entrada/archivo2.txt")
	if ( filedata != False ):
		archivo.grabarInfo("salida/archivo.txt", filedata)



class MyDaemon(Daemon):
	def run(self):
		while True:
			Sistema()
			time.sleep(1)

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)

