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


'''Aprimorando informações a partir do exercício de modelagem da coxinha''' 

#densidade da água - '''0,997 kg/L --> 997 kg/m3'''
do=
#densidade do recipiente (garrafa)
drec=
'''#volume de óleo - vamos deixar 10cm abaixo da altura do recipiente
vo=1*1*0.5
#volume do recipiente
vr=0.05*1*1*5'''
#massa de óleo
mo=do*vo
#massa do recipiente
mr=drec*vr
'''#calor específico do óleo de soja
co=1814.9
#calor específico do latão
cr=377'''
#temperatura ambiente, em kelvin
Ta=26+273.15
#espessura do recipiente: 0.1 mm: vamos dividi-lo ao meio na modelagem da condução térmica
dr=0.01/2
'''#área da superfície de contato entre o óleo e o ar
As=1*1'''
#área de contato das paredes externas do recipiente -->área do cilindro
Ap=14*16
#área de contato das paredes internas recipiente (vamos simplificar e igualá-las aqui) --> área do cilindro
Ar=Ap
'''#condutividade térmica do aço --> 80W/mk
kr=160
#coeficiente de transferência convectiva da superfície do óleo para o ar --> 10W/m2k
hs=10
#coeficiente de transferência convectiva das paredes do recipiente para o ar --> 10W/m2k
hp=10'''
#potência térmica dos aquecedor --> W
P=1800
#constante de Boltzman
sigma=5.6703e-8
#emissividade da água (	7.9 µm 8-14 µm)
emissividade = 0.93




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

