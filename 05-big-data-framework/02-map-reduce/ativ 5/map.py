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
        if ano == '2016':
            print '%s:%s' % (mercadoria, 1)
    except:
        continue