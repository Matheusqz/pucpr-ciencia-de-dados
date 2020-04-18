#! /usr/bin/env python
import sys

for linha in sys.stdin:
	try:
		campos = linha.split(';')
		ano = str(campos[1])
		print '%s\t%s' % (ano, 1)
	except:
		continue

