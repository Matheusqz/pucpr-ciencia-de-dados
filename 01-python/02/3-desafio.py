# Matheus Queiroz

# Criar um programa em Python que calcula o número de Euler (e = 2,71828 ) por meio da série de Taylor,
# dada por:
# e = 1/0! + 1/1! + 1/2! + 1/3! + ⋯ 
# A série deve ser calculada para um número N de termos informado pelo usuário (garanta que o valor lido
# seja válido). Quando mais termos forem utilizados no cálculo, mais preciso será o resultado (10 termos já
# convergem para um resultado satisfatório). Além disso, deve-se permitir que o usuário possa repetir a exe-
# cução do programa quantas vezes desejar. Veja abaixo um exemplo de execução.

import math

def calculo_euler(termos):
    soma = 0
    for termo in range(termos):
        soma += 1/math.factorial(termo)
    return soma

def termos_valido(termos):
    while termos <= 0:
        print("Erro, número inválido!")
        print("Digite o número N de termos: ")
        termos = int(input())
    return termos

execute = True

print("Programa em Python que calcula o número de Euler (e = 2,71828 ) por meio da série de Taylor")
print("****")
while execute:
    print( "Digite o número N de termos: ")
    termos = termos_valido(int(input()))
    euler = calculo_euler(termos)
    print("Resultado para {:d} termos {:.4f}: ".format(termos, euler))
    print("Deseja executar novamente? (S/n)")
    continuar = input()
    if continuar and continuar[0].lower() == 'n':
        print('FIM DA EXECUÇÃO')
        execute = False