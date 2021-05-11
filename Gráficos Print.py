from math import *
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def DadosMedidos():    
    lisTempoMedido = [0.30,1.00,1.30,2.00,2.30,3.0,3.30,4.00,4.30,5.00,5.16] #em minutos
    lisTemperaturaMedida = [37.9,47.3,54.9,63.1,71.0,78.5,84.9,91.2,96.6,99.8,100.1] #em graus celsius
    x = [lisTempoMedido, lisTemperaturaMedida]
    return x

y = DadosMedidos()
plt.plot(y[0],y[1] ,'r')
plt.plot(y[0],y[1] ,'ro')

plt.ylabel('Temperatura- °C')
plt.xlabel('Tempo- minutos')
plt.title("Gráfico Dados Medidos")
plt.grid(True)
plt.show()

# Informações básicas
di = 0.14 #Diâmetro (Metros)
r = 0.07 #Raio (Metros)
al = 0.16 #Altura (Metros)
ms = 1.4 #Massa (QuiloGramas)

# Informações avançadas
con =0.06 #Condutividade (W/(m•K))
lap = 0.001/2 #Largura parede interna (Metros)
volm = 0.0017 #Volume máximo (Mˆ3)
cal = 0.21 # Calor Especifico
pot = 1800 #Potência (Watts)
drec = volm/ms #Densidade (Kg/L)
mr = 1.4 #Massa (QuiloGramas)
hp = 70 # Transferencia Convectiva recepiente para o Ar (W/(m•K))

#  Informação básica
de = 997 #Densidade (Kg/L)

# Informações avançadas
hag = 50 #Convectividade W*mˆ-1*kˆ-1
calag = 1 #Calor Especifico
emi = 0.93 #Emissividade (7.9 µm 8-14 µm)
qt=1.5 #Quantidade de Água (Litros)

har = 10 # Transferencia Convectiva Agua para Ar (W/(m•K))

Tamb = 27+273.15 #Temperatura Ambiente (Kelvin)
Ap = (2*pi*r*al) + (2*pi*r) #Area de Contato Externa (Mˆ2)
Ap2 = (2*pi*r*al) # Area de Contato (Primeira Iteração em Mˆ2)
Ar = Ap #Area de Contato Interna (Mˆ2)
Aar = 2*pi*r
sigma= 5.6703e-8 #Constante de Boltzman

emissividade = 0.96 #Emissividade da água (ε)

def modelo(x,t):
    ma=qt*de
    Ta= x[0]
    Tp= x[1]
    Qag= pot
    Q1= (Ta-Tp) / ((1/(hag*Ap))+(lap/(con*Ap))) #Convexão Água
    Q2= (Tp-Tamb) / ((1/(hp*Ap))+(lap/(con*Ap))) #Condução Parede
    dTadt=(1/(ma*calag)) * (Qag - Q1)
    dTpdt= (1/(mr*cal)) * (Q1-Q2)
    dxdt=[dTadt,dTpdt]
    return dxdt

delta_t = 10**(-3) #Delta Tempo
Tmax = 120 # Tempo Maximo
lista_tempo = np.arange(0,Tmax,delta_t) #Criação Lista de Tempo
Temp_ag = 27 #Temperatura inicial da Água (°C)
Temp_pd = 27 #Temperatura Inicial da parede (°C)
x0 = [Temp_ag+273.15, Temp_pd +273.15] #Condiões Iniciais 

y_lista = odeint(modelo,x0,lista_tempo) #ODEINT

Temp_agua= y_lista [:,0]
Temp_parede= y_lista [:,1]

Ta_a=[]
for e in Temp_agua:
        if e > 373.15:
            Ta_a.append(373.15 -273.15)
        else:
            Ta_a.append(e-273.15)
Tp=[]
for i in Temp_parede:
    Tp.append(i-273.15)
H_tempo=[]
M_tp=[]
for h in lista_tempo:
    H_tempo.append(h/3600)
    M_tp.append(h/60)

'''plt.plot(H_tempo, Ta_a, label="Temp. Àgua")
plt.plot(H_tempo, Tp ,label="Temp.Parede")
plt.xlabel("Tempo(H)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()'''

'''plt.plot(y[0],y[1] ,'r', label = "Temp. Àgua no Experimento")
plt.plot(y[0],y[1] ,'ro')'''
plt.title("Gráfico Modelo")
plt.plot(M_tp , Ta_a, label = "Temp. Àgua no Modelo")
#plt.plot(M_tp , Tp ,label = "Temp.Parede")
plt.xlabel("Tempo(M)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()

plt.title("Gráfico Modelo e Experimento")
plt.plot(y[0],y[1] ,'ro', label = "Temp. Àgua no Experimento")
#plt.plot(y[0],y[1] ,'r')
plt.plot(M_tp , Ta_a, label = "Temp. Àgua")
plt.xlabel("Tempo(h)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()


#Aar = Area de Contato Agua - Ar
#App = Area de contato Ar - Parede
#Apr = Area de Contato Agua - Parede
def p_iteracao(x,t, qt):
    volume = qt/1000
    Al = volume*pi*(r**2)
    Apr = Ap2 - (2*pi*r*Al)
    #Formula App
    App = (Ap2 - Apr) + (2*pi*r)
    #Massa
    ma=qt*de
    #Divisão de X
    Ta= x[0]
    Tp= x[1]
    #Potência
    Qag= pot
    #Fluxos de Calor
    Q1= (Ta-Tp) / ((1/(hag*Apr))+(lap/(con*(Apr)))) #Convexão Água
    Q3= (Ta-Tp) / ((1/(har*Aar)) + (1/(hp*App)) +(lap/(con*App)))#Convexão Agua-Ar e Ar-Parede
    
    Q2= (Tp-Tamb) / ((1/(hp*Ap))+(lap/(con*Ap))) #Condução Parede
    #Derivadas
    dTadt=(1/(ma*calag)) * (Qag - (Q1+Q3))
    dTpdt= (1/(mr*cal)) * ((Q1+Q3)-Q2)
    #Junção de Derivadas
    dxdt=[dTadt,dTpdt]
    #Retornar
    return dxdt



y1_lista = odeint (p_iteracao,x0, lista_tempo,args=(qt,))
Temp1_agua= y1_lista [:,0]
Temp1_parede= y1_lista [:,1]

Ta_a1=[]
for e in Temp1_agua:
        if e > 373.15:
            Ta_a1.append(373.15 -273.15)
        else:
            Ta_a1.append(e-273.15)
Tp1=[]
for i in Temp1_parede:
    Tp1.append(i-273.15)
    
'''plt.plot(H_tempo, Ta_a1, label="Temp. Àgua")
plt.plot(H_tempo, Tp1 ,label="Temp.Parede")
plt.xlabel("Tempo(H)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()'''

#plt.plot(y[0],y[1] ,'r')
plt.title("Gráfico Comparação PI e Experimento")
plt.plot(y[0],y[1] ,'ro', label = "Temp. Àgua no Experimento")
plt.plot(M_tp , Ta_a1, label = "Temp. Àgua")
#plt.plot(M_tp , Tp1 ,label = "Temp.Parede")
plt.xlabel("Tempo(min)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()

hp=30
har=5

def s_iteracao(x,t,qt):
    e=2.718281828459045 #Constante de Euler
    o=sigma 
    volume = qt/1000
    Al = volume*pi*(r**2)
    Apr = Ap2 - (2*pi*r*Al)
    #Formula App
    App = (Ap2 - Apr) + (2*pi*r)
    #Massa
    ma=qt*de
    #Divisão de X
    Ta= x[0]
    Tp= x[1]
    #Potência
    Qag= pot
    #Fluxos de Calor
    Q1= (Ta-Tp) / ((1/(hag*Apr))+(lap/(con*(Apr)))) #Convexão Água
    Q3= (Ta-Tp) / ((1/(har*Aar)) + (1/(hp*App)) +(lap/(con*App)))#Convexão Agua-Ar e Ar-Parede
    
    Q2= (Tp-Tamb) / ((1/(hp*Ap))+(lap/(con*Ap))) #Condução Parede
    
    Q4= e*o*Ap*(Ta**4)
    #Derivadas
    dTadt=(1/(ma*calag)) * (Qag -Q1-Q3-Q4)
    dTpdt= (1/(mr*cal)) * ((Q1+Q3)-Q2)
    #Junção de Derivadas
    dxdt=[dTadt,dTpdt]
    #Retornar
    return dxdt
qt=1.5
t2_lista =np.arange (0,400,0.1)
y2_lista = odeint (s_iteracao,x0, t2_lista,args=(qt,))
Temp2_agua= y2_lista [:,0]
Temp2_parede= y2_lista [:,1]

Ta_a2=[]
for m in Temp2_agua:
        if m > 373.15:
            Ta_a2.append(373.15 -273.15)
        else:
            Ta_a2.append(m-273.15)
Tp2=[]
for n in Temp2_parede:
    Tp2.append(n-273.15)
tm2=[]
th2=[]
for H in t2_lista:
    th2.append(H/3600)
    tm2.append(H/60)
    

#plt.plot(th2, Ta_a2, label="Temp. Àgua")
#plt.plot(th2, Tp2 ,label="Temp.Parede")
plt.xlabel("Tempo(H)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
#plt.show()
plt.title("Gráfico Comparação PS e Experimento")
plt.plot(y[0],y[1] ,'r', label = "Temp. Àgua no Experimento")
plt.plot(y[0],y[1] ,'ro')
plt.plot(tm2 , Ta_a2, label = "Temp. Àgua")
#plt.plot(tm2 , Tp2 ,label = "Temp.Parede")
plt.xlabel("Tempo(Min)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)
plt.show()


#Função para encontrar tempo até 100°C
def tempoate100 (Temperatura_agua,Tempo):
    tempo=1000
    for c, temperatura in enumerate(Temperatura_agua):
        if temperatura >= 100:
            tempo=tm2[c]
            break 
    return tempo

Listatempos = []

#Lista de Quantidades
Lista_Qt = np.arange (0.01,1.71,0.01)
#Lista_Qt = [0.5,0.7,1,1.5,1.7]
for qt in Lista_Qt:
    #Odeint
    Yqt_lista=odeint(s_iteracao,x0,t2_lista,args=(qt,))
    Lista_elementos=[]
    for elemento in Yqt_lista[:,0]:
        if elemento > 373.15:
            Lista_elementos.append(100)
        else: 
            Lista_elementos.append(elemento-273.15)
    #Plot Gráfico
    plt.plot (tm2,Lista_elementos,label="{0}L".format(qt))
    #Encontra Tempo
    Listatempos.append(tempoate100(Lista_elementos,tm2))
#print (Listatempos)
plt.title("Gráfico ODEINT")
plt.ylabel("Temperatura (°C)")
plt.xlabel("Tempo (Minutos)")
plt.grid(True)
plt.show()

#plotando o gráfico conclusivo
ax=plt.axes()
ax.set_facecolor('xkcd:ivory')
plt.title("Gráfico conclusivo")
plt.plot(Lista_Qt, Listatempos, 'r-o')
plt.xlabel("Volumes (L)")
plt.ylabel("Tempo para atingir 100°C")
plt.grid(True)
plt.show()



