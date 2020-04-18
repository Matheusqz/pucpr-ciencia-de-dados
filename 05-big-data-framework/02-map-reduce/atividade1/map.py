#! /usr/bin/env python
import sys

for linha in sys.stdin:
	try:
		campos = linha.split(';')
		pais = campos[0]
		print '%s\t%s' % (pais, 1)
	except:
		continue

