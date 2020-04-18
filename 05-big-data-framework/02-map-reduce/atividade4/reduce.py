#! /usr/bin/env python
import sys

ocorrencia = {}

for linha in sys.stdin:
	chave, valor = linha.split('\t', 1)
	
	valor = int(valor)

	try:
		ocorrencia[chave] = ocorrencia[chave] + valor
	except:
		ocorrencia[chave] = valor

for chave in ocorrencia.keys():
	print '%s\t%s' % (ocorrencia[chave], chave)
