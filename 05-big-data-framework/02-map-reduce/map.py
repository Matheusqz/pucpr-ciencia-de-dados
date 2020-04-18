#!/usr/bin/env python
import sys

for linha in sys.stdin:
	campos = linha.split(';')
	
	pais = campos[0]
	
	print '%s\t%s' % (pais, "1")