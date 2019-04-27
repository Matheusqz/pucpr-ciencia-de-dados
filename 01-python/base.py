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

def print_for(num, add)