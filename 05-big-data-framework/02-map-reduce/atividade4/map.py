#! /usr/bin/env python
import sys

for linha in sys.stdin:
	try:
		campos = linha.split(';')
		mercadoria = str(campos[3])
		print '%s\t%s' % (mercadoria, 1)
	except:
		continue

