import math

def var_int_input(num_input):
    input_list = []
    while len(input_list) != num_input:
        int_append = int_input('Adicione um valor inteiro: ')
        input_list.append(int_append)
    return input_list

def int_input(texto):
    return int(input(texto))

def float_input(texto):
    return float(input(texto))

exercicio = int(input('Digite numero do exercicio: '))
if exercicio == 1:
    print('1) Crie um algoritmo que imprime a soma entre dois valores fornecidos pelo usuário.')
    num1 = int_input('Primeiro valor: ')
    num2 = int_input('Segundo valor: ')
    print('A soma é ', num1 + num2)
elif exercicio == 2:
    print('2) Crie um algoritmo que imprime a média entre três notas parciais de um estudante fornecidas pelo usuário.')
    num1 = float_input('Primeira nota: ')
    num2 = float_input('Segunda nota: ')
    num3 = float_input('Terceira nota: ')
    media = (num1 + num2 + num3)/3
    print('Média: %.2f', media)

elif exercicio == 3:
    print('3) Crie um algoritmo que imprime a área e o perímetro de um retângulo cujas medidas (base e altura) são fornecidas pelo usuário.')
    triangulo = var_int_input(2)
    print('Area do triangulo ', (triangulo[0]*triangulo[1])/2)

elif exercicio == 4:
    print('4) Crie um algoritmo que imprime o valor da hipotenusa de um triângulo retângulo cujos catetos são fornecidos pelo usuário.')
    catetos = var_int_input(2)
    print('A hipotenusa é ', math.sqrt(catetos[0]**2 + catetos[1]**2))

elif exercicio == 5:
    print('5) Para auxiliar um lojista, crie um algoritmo que imprime o valor com desconto e sem desconto de uma compra')
    print('cuja quantidade de um produto fictício, preço unitário do produto e percentual de desconto são fornecidos pelo usuário.')
    loja = var_int_input(3)
    preco = loja[0]*loja[1]
    print('Preco sem desconto: ', preco)
    if loja[2] > 0:
        print('PReco com desconto: ', preco*(1/loja[2]))
    else:
        print('Não há desconto')

elif exercicio == 6:
    print('6) Para auxiliar um departamento de física, crie um algoritmo que imprime a energia cinética de um corpo em movimento.')
    print('Defina os dados de entrada com base na equação.')


elif exercicio == 7:
    print('7) Crie um algoritmo que imprime a velocidade média de um corpo que se moveu da posição X (em metros) até a posição Y (em metros) em Z segundos.')

elif exercicio == 8:
    print('8) Crie um algoritmo que, a partir do tamanho de um arquivo online (em MB) e da velocidade da internet (em Mbps)')
    print('informados pelo usuário, calcula e imprime o tempo aproximado de download daquele arquivo em minutos.')

elif exercicio == 9:
    print('9) Crie um algoritmo que, a partir dos coeficientes ‘a’, ‘b’ e ‘c’ de uma equação do 2o grau informados pelo usuário,')
    print('calcula e imprime o valor do ‘delta’ da fórmula de Bháskara.')

elif exercicio == 10:
    print('10) Crie um algoritmo que, a partir da temperatura em graus Fahrenheit lida do usuário, calcula e apresenta na tela')
    print('a temperatura em graus Celsius, sabendo-se que: C = (5 * (F-32) / 9)')

elif exercicio == 11:
    print('11) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,')
    print('usando a seguinte fórmula: (72.7*altura) – 58.')

elif exercicio == 12:
    print('12) Tendo como dados de entrada o peso (em kg) e a altura (em m) de uma pessoa, crie um algoritmo que calcula')
    print('o Índice de Massa Corporal (IMC) daquela pessoa.')

elif exercicio == 13:
    print('13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,')
    print('utilizando as seguintes fórmulas:')
    print('a) Para homens: (72.7*h) - 58')
    print('b) Para mulheres: (62.1*h) - 44.7')

elif exercicio == 14:
    print('14) Escreva um algoritmo que receba do usuário a quantidade de dias, horas, minutos e segundos e calcule o total em segundos.')
    print('Este total calculado deverá ser apresentado na tela.')

elif exercicio == 15:
    print('15) Embora esta prática não seja prevista por lei, muitos restaurantes costumam cobrar uma taxa de serviço de 10/%')
    print('sobre o valor total consumido. Crie um algoritmo que, a partir do total gasto com comida (em R$) e do')
    print('total gasto com bebida (em R$) informados pelo usuário, calcula e imprime: o valor total consumido, o valor da taxa de serviço e o valor final a ser pago.')


elif exercicio == 16:
    print('16) Crie um algoritmo que, a partir de um valor ‘x’ informado pelo usuário, calcula e imprime o resultado das seguintes equações:')
    print('a) y = (x/1 + x^2/2 + x^3/3). x')
    print('b) y = 2x/(raiz(2^2 + x^3))')
    
else:
    print('Exercicio não encontrado')

