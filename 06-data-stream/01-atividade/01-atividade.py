import math 

# valores para teste

teste_1 = [0.2,0.3,0.1,0.99,0.99,0.99,0.2,0.1,0.2,0.2,0.2,0.1]

teste_2 = [0.2,0.3,0.1,0.99,0.99,0.99,0.2,0.1,0.2,0.2,0.2,0.1,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.1,0.2,0.3,0.1,
    0.99,0.99,0.99,0.2,0.1,0.2,0.2,0.2,0.1]

teste_3 = [0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,
0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,
0.2,0.2,0.3,0.1,0.9,0.9,0.9,0.8,0.8,0.9,0.8,0.9,1.0,0.9,0.9,0.9,0.8,0.8,0.9,0.8,0.9,1.0,0.9,0.9,0.9,
0.8,0.8,0.9,0.8,0.9,1.0,0.9,0.9,0.9,0.8,0.8,0.9,0.8,0.9,1.0,0.9,0.9,0.9,0.8,0.8,0.9,0.8,0.9,1.0,0.9,0.9
,0.9,0.8,0.8,0.9,0.8,0.9,1.0,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,
0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.3,
0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2,0.3,0.1,0.1,0.2,0.2,0.2,0.2,0.2,0.2]

def media_lista(lista):

    if type(lista) == list:
        return sum(lista) / len(lista)
    return lista

def ecut(w0, w1, delta):
    len_w = len(w0) + len(w1)
    m_denominador = (1 / len(w0)) + (1 / len(w1))
    m = 2 / m_denominador
    e_cut = math.sqrt( (1 / (2 * m) ) * math.log( (4 * len_w) / delta) )
    return e_cut

def teste(delta, stream):
    w = stream[0:2]
    count = len(w)
    for x in stream:
        w.insert(0, x)
        flag = False
        i = len(w) -1
        while (not flag) and (i > 1):
            w0 = w[0:i-1]
            w1 = w[i:len(w)]
            u0 = media_lista(w0)
            u1 = media_lista(w1)
            e_cut = ecut(w0, w1, delta)
            if(abs(u0 - u1) >= e_cut):
                flag = True
                del w[-1]
            i = i - 1
        if flag:
            print(f'Flag: {count}')
        count += 1

    return media_lista(w)


if __name__ == '__main__':
    delta = 0.9
    print(f'Primeiro teste: {teste(delta, teste_1)}')
    print(f'Segundo teste: {teste(delta, teste_2)}')
    print(f'Terceiro teste: {teste(delta, teste_3)}')