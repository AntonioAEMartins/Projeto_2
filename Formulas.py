from math import *
#Informações Básicas - Chaleira
di = 0.14 #M - Diametro
r = 0.07 #M - Raio
al = 0.16 #M - Altura
ms = #Massa
#Informações Avançadas - Chaleira
con =0.06 # - Condutividade
lap = 0.001/2 #M - Largura Parede Interna
volm = 0.00017 #Mˆ3 - Volume Maximo
cal = 0.21 # Calor Especifico 0.46
pot = 1800 #W - Potência
drec = volm/ms #Densidade
mr = drec*vr #Massa
hp = 10 # Transferencia Convectiva recepiente para o Ar
""
#Informações Básicos - Àgua
qt = #Quantidade(Litros)
de = 997 #Densidade
ma = qt*de
#Informações Avançadas - Àgua
hag = 0.0235 #Convectividade W*mˆ-1*kˆ-1
calag = 1 #Calor Especifico
emi = 0.93 #Emissividade (7.9 µm 8-14 µm)
""
#Temperaturas Iniciais
tamb = 27+273.15#K
""
#Areas
Ap = 2*pi*Raio*Altura #Contato Ex
Ar = Ap #Contato In
""
sigma=5.6703e-8 #Constante de Boltzman
""
#Função
def modelo(x,t):
    Ta=x[0]
    Tp=x[1]
    Qag=P
    Q1= (Ta-Tp)/((1/(hag*Ap))+(lap/con*Ap)) #Convexão Agua
    Q2= (Tp-Tamb)/(1/#Condução Parede
    Q3=
    Q4=
    dTadt=(1/(m*ca)) * (Qag - Qconx - Qconv)
    dTpdt= (1/) * ()
    dxdt=[dTadt,dTpdt]
    return dxdt

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
