import math
import matplotlib.pyplot as plt

GRAVIDADE = 9.6

def velocidade_valida(velocidade):
    while velocidade < 0:
        print("Valor invalido")
        print("Digite um valor valido para a velocidade (m/s)")
        velocidade = int(input())
    return velocidade

def angulo_valido(angulo):
    while angulo < 0:
        print("Valor invalido")
        print("Digite um valor valido para o angulo de lançamento (em graus)")
        angulo = int(input())
    return angulo

def calc_distancia(tempo, radiano, velocidade):
    return abs(velocidade)*math.cos(radiano)*tempo

def calc_altura(tempo, radiano, velocidade):
    return abs(velocidade)*math.sin(radiano)*tempo - (GRAVIDADE*(tempo**2))/2

def calc_parabola(velocidade, radiano):
    parabola = {
        'distancias' : [],
        'alturas' : [],
        'tempo' : 0.1
        
    }
    
    trajeto = True
    while trajeto:
        if calc_altura(parabola['tempo'], radiano, velocidade) > 0:
            parabola['distancias'].append( round(calc_distancia(parabola['tempo'], radiano, velocidade),1))
            parabola['alturas'].append( round(calc_altura(parabola['tempo'], radiano, velocidade),1))
            parabola['tempo'] += 0.1
        else:
            trajeto = False
    
    return parabola

print("Digite a velocidade (m/s):")
velocidade = velocidade_valida(int(input()))
print("Digite o angulo de lançamento (em graus):")
angulo = angulo_valido(float(input()))
radiano = math.radians(angulo)
parabola = calc_parabola(velocidade, radiano)
plt.plot(parabola['distancias'], parabola['alturas'],marker='o',color='blue')
plt.ylabel('altura (m)')
plt.xlabel('distância (m)') 
plt.show

print('*******************************************')
print('Distância percorida: {:.1f}'.format(parabola['distancias'][-1]))
print('Altura máxima atingida: {:.1f}'.format(max(parabola['alturas'])))
print('Duração do lançamento: {:.1f}'.format(parabola['tempo']))
print('*******************************************')