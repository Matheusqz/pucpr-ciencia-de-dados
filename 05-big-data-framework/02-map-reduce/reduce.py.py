#!/usr/bin/env python
import sys

ocorrencias = {}

for linha in sys.stdin:
	chave, valor = linha.split('\t', 1)
    
    try:
        valor = int(valor)
    except ValueError:
        continue;
        
    try:
        ocorrencia[chave] = ocorrencia[chave] + valor
    except:
        ocorrencia[chave] = valor
        
for pais in ocorrencia.keys():
    print '%s\t%s' % (pais, ocorrencia[pais])