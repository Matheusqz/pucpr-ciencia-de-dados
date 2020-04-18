#! /usr/bin/env python

import sys

dic = {}

for linha in sys.stdin:
    chave ,valor = linha.split(':', 1)
    try:
        valor = int(valor)
        try:
            dic[chave] = dic[chave] + valor
        except:
            dic[chave] = valor
    except:
        continue

for chave in dic.keys():
    print '%s:%s' % (dic[chave], chave)
