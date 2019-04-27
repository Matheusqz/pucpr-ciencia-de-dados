def var_input(num_input, type='int', list_text=[]):
    input_list = []
    while len(input_list) != num_input:
        if len(list_text) == len(input_list):
            list_text.append('Adicione um valor: ')
        if type == 'int':
            value_append = int_input(list_text[len(input_list)])
        elif type == 'float':
            value_append = float_input(list_text[len(input_list)])
        input_list.append(value_append)
    return input_list


def int_input(texto):
    return int(input(texto))

def float_input(texto):
    return float(input(texto))

# Criar um programa em Python para ajudar uma empresa a calcular a folha de pagamento mensal de um
# funcionário qualquer. O programa deve receber:
# • A quantidade de dias trabalhados no mês pelo funcionário.
# • A quantidade de horas regulares trabalhadas por dia.
# • A remuneração (em R$) por hora regular trabalhada.
# • A quantidade de horas extras feitas no mês.
# • A remuneração (em R$) por hora extra trabalhada.
# • O valor mensal do vale combustível fornecido pela empresa.
# • O valor mensal do vale-alimentação fornecido pela empresa.
# • A quantidade mensal de horas regulares descontadas por falta ao trabalho.
# • O desconto mensal devido ao plano de saúde empresarial.
# • O desconto mensal devido ao plano odontológico empresarial.
# • O desconto mensal devido ao auxílio escolar prestado ao(s) dependente(s) do funcionário.
input_quantidade = var_input(4, 'int', ['Dias trabalhados: ', 'horas dia: ', 'Horas extras: ', 'Horas descontadas: '])
input_valores = var_input(2, 'float', ['Remuneracao por hora: ', 'Remuneracao hora extra: '])
input_beneficios = var_input(2, 'float', ['vale-combustivel: ', 'vale-alimentacao: '])
input_desconto_beneficios = var_input(3, 'float', ['Desconto plano de saude: ', 'Desconto plano odonto: ', 'Desconto auxilio escolar: '])

horas_mes = input_quantidade[0]*input_quantidade[1]
horas_extras = input_valores[1] * input_quantidade[2]
salario_bruto = horas_mes * input_valores[0] + input_beneficios[0] + input_beneficios[1] + horas_extras
print('SALARIO BRUTO: ', salario_bruto)
# print('Horas Extras: ', horas_extras)
falta_desconto = input_quantidade[3]* input_valores[0]
print('Desconto horas faltantes: ',  falta_desconto)
print('Plano de Saude: ', input_desconto_beneficios[0])
print('Plano Odonto: ', input_desconto_beneficios[1])
print('Auxilio escolhar: ', input_desconto_beneficios[2])
salario_desconto = salario_bruto - falta_desconto - input_desconto_beneficios[0] - input_desconto_beneficios[1] - input_desconto_beneficios[2]
print('Salario com desconto: ', salario_desconto)
ir = salario_desconto*0.11
inss = salario_desconto*0.08
sindicato = salario_desconto*0.05
print('IR (11%) ', ir)
print('INSS (8%) ', inss)
print('Sindicato (5%) ', sindicato)
print('Salario Liquido: ', salario_desconto - ir - inss - sindicato)
# Depois, o programa deve imprimir:
# • O salário bruto do funcionário.
# • Os valores dos descontos.
# • O salário bruto com os descontos.
# • Os valores dos tributos: Imposto de Renda (11%), INSS (8%) e Sindicato (5%).
# • O salário líquido.

