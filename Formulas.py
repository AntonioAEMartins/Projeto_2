from math import *
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
#Informações Básicas - Chaleira
di = 0.14 #M - Diametro
r = 0.07 #M - Raio
al = 0.16 #M - Altura
ms = 1.4 #Kg - Massa
#Informações Avançadas - Chaleira
con =0.06 # - Condutividade
lap = 0.001/2 #M - Largura Parede Interna
volm = 0.00017 #Mˆ3 - Volume Maximo
cal = 0.21 # Calor Especifico 0.46
pot = 1800 #W - Potência
drec = volm/ms #Densidade
mr = 1.4 #Massa
hp = 10 # Transferencia Convectiva recepiente para o Ar
"" #Comentar unidades
#Informações Básicos - Àgua
#qt = 0.5#Quantidade(Litros)
de = 997 #Densidade
#ma = qt*de
#Informações Avançadas - Àgua
hag = 50 #Convectividade W*mˆ-1*kˆ-1
calag = 1 #Calor Especifico
emi = 0.93 #Emissividade (7.9 µm 8-14 µm)
""
#Temperaturas Iniciais
Tamb = 27+273.15#K
""
#Areas
Ap = 2*pi*r*al + 2*pi*r #Contato Ex
Ar = Ap #Contato In
""
sigma=5.6703e-8 #Constante de Boltzman
""
#Função
"""def modelo(x,t):
    Ta= x[0]
    Tp= x[1]
    Qag= pot
    Q1= (Ta-Tp) / ((1/(hag*Ap))+(lap/con*Ap)) #Convexão Agua
    Q2= (Tp-Tamb) / ((1/hp*Ap)+(lap/con*Ap)) #Condução Parede
    dTadt=(1/(ma*calag)) * (Qag - Q1)
    dTpdt= (1/mr*cal) * (Q1-Q2)
    dxdt=[dTadt,dTpdt]
    return dxdt"""

def modelo_novo(x,t,qt):
    Ta= x[0]
    Tp= x[1]
    Qag= pot
    Q1= (Ta-Tp) / ((1/(hag*Ap))+(lap/con*Ap)) #Convexão Agua
    Q2= (Tp-Tamb) / ((1/hp*Ap)+(lap/con*Ap)) #Condução Parede
    dTadt=(1/(qt*de*calag)) * (Qag - Q1)
    dTpdt= (1/mr*cal) * (Q1-Q2)
    dxdt=[dTadt,dTpdt]
    return dxdt

#IMPLEMENTE AQUI A PRIMEIRA ITERAÇÃO DO MODELO
delta_t = 10**(-3)
Tmax = 120
lista_tempo = np.arange(0,Tmax,delta_t)
x0 = [27+273.15, 27+273.15]
#y_lista=odeint(modelo, x0, lista_tempo)

#alterando os volumes da água
lista_qt = [0.5, 1.0 , 1.5 , 1.7]

for i in range(len(lista_qt)):
    Ta = 27 + 273.15
    Tp = 27 + 273.15
    x0 = [Ta,Tp]

    x = odeint (modelo_novo,x0,lista_tempo, args=(lista_qt[i],))
    Ta = x[:,0]
    Tp = x[:,1]
    Ta_a=[]
    for e in Ta:
        if e > 373.15:
            Ta_a.append(373.15)
        else:
            Ta_a.append(e)

    plt.plot(lista_tempo, Ta_a, label = "Temp. Àgua: {0}L".format(lista_qt[i]))
    plt.plot(lista_tempo, Tp, label = "Temp. Par: {0}L".format(lista_qt[i]))

#Plot Gráfico
"""temp_agua=y_lista[:,0]
temp_parede=y_lista[:,1]"""
#plt.plot(lista_tempo, temp_agua, label="Temp. Àgua")
#plt.plot(lista_tempo,temp_parede,label="Temp.Parede")
plt.xlabel("Tempo(s)")
plt.ylabel("Temperatura (k)")
plt.legend()
plt.grid(True)
plt.show()
#Iteração
'''Aprimorando informações a partir do exercício de modelagem da coxinha''' 

'''#volume de óleo - vamos deixar 10cm abaixo da altura do recipiente
vo=1*1*0.5
#volume do recipiente
vr=0.05*1*1*5'''

''''
#calor específico da garrafa
cr=377
'''

'''#área da superfície de contato entre o óleo e o ar
As=1*1'''

'''#condutividade térmica do aço --> 80W/mk
kr=
#coeficiente de transferência convectiva da superfície do óleo para o ar --> 10W/m2k
hs=
#coeficiente de transferência convectiva das paredes do recipiente para o ar --> 10W/m2k
hp=10'''
