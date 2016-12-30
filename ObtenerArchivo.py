#!/usr/bin/python

class ObtenerArchivo():
	def leerInfo(self, filelocation):
		try:
			of = open(filelocation,"r")
			filedata = of.read()
			of.close()
			return filedata
		except IOError:
			return False


	def grabarInfo(self, filelocation, stringdata):
		of = open(filelocation,"a")
		filedata = of.write(stringdata)
		of.close()
		
