import numpy as np

ctba = [27.5, 26.4, 21.1, 22.1, 22.5, 16.9, 15.0, 09.7, 19.7, 22.7, 22.8, 24.7]
lond = [31.3, 33.0, 24.8, 25.4, 27.9, 23.4, 23.9, 12.7, 23.9, 28.2, 29.2, 30.4]

frio = 15
quente = 25


def max(arr):
    maxx = arr[0]
    for x in arr:
        if x > maxx:
            maxx = x
    return maxx

def min(arr):
    minx = arr[0]
    for x in arr:
        if x < minx:
            minx = x
    return minx

def media(arr):
    soma = 0
    for x in arr:
        soma += x
    return soma/len(arr)

def desvp(arr):
    med = media(arr)
    sum_dp = 0
    for x in arr:
        sum_dp += (x - med)**2
    return np.sqrt(sum_dp/len(arr))


def meses_quentes(temp, arr):
    cont_mes = 0
    for x in arr:
        if x >= temp:
            cont_mes += 1
    perc = cont_mes / len(arr)
    return [ cont_mes, perc ]

def meses_frios(temp, arr):
    cont_mes = 0
    for x in arr:
        if x <= temp:
            cont_mes += 1
    perc = cont_mes / len(arr)
    return [ cont_mes, perc ]

def meses_amenos(temp_frio, temp_quente, arr):
    cont_mes = 0
    for x in arr:
        if temp_frio < x < temp_quente:
            cont_mes += 1
    perc = cont_mes / len(arr)
    return [ cont_mes, perc ]


print(desvp(ctba)==np.std(ctba))