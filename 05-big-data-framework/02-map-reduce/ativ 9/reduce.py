#! /usr/bin/env python

import sys

qtd = {}
pesos = {}

for linha in sys.stdin:
    chave, valor, qt = linha.split(':', 2)
    try:
        valor = int(valor)
        qt = int(qt)
        try:
            qtd[chave] = qtd[chave] + qt
            pesos[chave] = pesos[chave] + valor
        except:
            qtd[chave] = qt
            pesos[chave] = valor
    except:
        continue

for chave in pesos.keys():
    media = pesos[chave] / qtd[chave]
    print '%s:%s' % (  media , chave)
