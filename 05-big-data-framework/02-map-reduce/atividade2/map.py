#! /usr/bin/env python
import sys

for linha in sys.stdin:
	try:
		campos = linha.split(';')
		if campos[0] == 'Brazil':
			mercadoria = str(campos[3])
			print '%s\t%s' % (mercadoria, 1)
	except:
		continue

