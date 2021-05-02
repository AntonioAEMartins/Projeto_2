import math
#Informações Chaleira
#Diametro da Chaleira
di= 14
#Raio da Chaleira
r= 7
#Altura da Chaleira
al= 16
#Condutividade Termica da Chaleira
cond = 0.06
#Largura Parede Interna da Chaleira
la = 0.1
d=0.05
#Potencia da Chaleira
P = 1200
#Volume Maximo da Chaleira
v = 1.7
#Calor Escifico do Plastico
ca = 0.21
#Area de Superficie Chaleira
ar=2*math.pi*r*al

#Informações Agua
#Densidade da Agua
de= 1
#Condutividade termica da Agua
con = 631.2372
#Calor especifico da Agua
cal= 1
#Area de Superficie Agua
As=2*math.pi*r

#Informações do Ar
#Condutividade termica do Ar

#Temperaturas
#Tamb
Tamb=
#Ta

#Tp






#Função
def modelo(x,t):
    Qag=P
    Qconvx= (Ta-Tp)/((1/(con*As))+(d/cond*ar)) #Convexão Agua
    Qcond= (Tp-Tamb)/(1/#Condução Parede
    Qconx= #Convexão AR
    dTadt=
    dTadt=(1/(m*ca)) * (Qag - Qconx - Qcond)
    dTpdt= (1/) * ()

