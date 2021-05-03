import math
#Formulas Convexão
1/(h*A) #h do ar e A de agua

#Formulas Condução
d/(k*A)


#Dimensões Chaleira - CM
Diametro = 14
Raio = 7
Altura = 16
#Informações Chaleira
Condutividade = 0.06
Larg_Parede = 0.1
Pot= 1200
V_max = 1.7
Cal_Esp_pl = 0.21 - 0.43
#Informações Agua
Densidade = 1
Condutividade1 = 631.2372 
Cal_Esp = 1

#Informações objetivas
di= Diametro
r= Raio
al= Altura
cond = Condutividade
la = Larg_Parede
P = Pot
v = V_max
ca = Cal_Esp_pl
de= Densidade
con = Condutividade1
cal= Cal_Esp
pi =math.pi


#Função
def modelo(x,t):
    Qag= P
    Qconvx=
    Qconv=
    Qconx1=
    dTadt=
    dTadt=(1/(m*ca)) * (Qag - Qconx - Qconv)
    dTpdt= (1/) * ()

