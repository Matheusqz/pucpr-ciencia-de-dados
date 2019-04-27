# Matheus Queiroz

# Criar um programa em Python que calcula o número PI por meio do somatório da série de Leibniz, dada por:
# π = 4 ∗ (1 − 1/3 + 1/5 - 1/7 + 1/9 ....)
# A série deve ser calculada para um número N de termos informado pelo usuário (garanta que o valor lido
# seja válido). Quando mais termos forem utilizados no cálculo, mais preciso será o resultado. Além disso,
# deve-se permitir que o usuário possa repetir a execução do programa quantas vezes desejar

def calculo_pi_soma_termos(termos):
    soma = 0
    sinal = 1
    for termo in range(termos):
        soma += sinal/(2*termo +1)
        sinal = -sinal
    return 4*soma

def termos_valido(termos):
    while termos <= 0:
        print("Erro, número inválido!")
        print("Digite o número N de termos: ")
        termos = int(input())
    return termos

execute = True

print("Programa em Python que calcula o número PI por meio do somatório da série de Leibniz")
print("****")
while execute:
    print( "Digite o número N de termos: ")
    termos = termos_valido(int(input()))
    pi = calculo_pi_soma_termos(termos)
    print("Resultado para {:d} termos {:.4f}: ".format(termos, pi))
    print("Deseja executar novamente? (S/n)")
    continuar = input()
    if continuar and continuar[0].lower() == 'n':
        print('FIM DA EXECUÇÃO')
        execute = False