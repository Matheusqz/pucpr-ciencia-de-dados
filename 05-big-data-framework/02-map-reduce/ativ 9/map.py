#! /usr/bin/env python

import sys

for linha in sys.stdin:
    try:
        campos = linha.split(';')
        pais = campos[0]
        ano = campos[1]
        cod = campos[2]
        mercadoria = campos[3]
        fluxo = campos[4]
        valor = campos[5]
        peso = campos[6]
        unid = campos[7]
        qt = campos[8]
        print '%s-%s:%s:%s' % (ano, mercadoria, peso, qt)
    except:
        continue