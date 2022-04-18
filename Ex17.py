#import math
a1 = float(input("Qual a quantidade de álcool consumido em (ml)? "))
a2 = a1/29.5735
w = float(input("Qual o seu peso? "))
H = int(input("Quantas horas após o último drink? "))
gen = str(input("Qual o seu gênero? "))
if gen == "Feminino" or gen == "feminino":
    r = 0.13
elif gen == "Masculino" or gen == "masculino":
    r = 0.66
else:
    print("Digite um gênero válido.")
bac = (a2*5.14/w*r) - 0.015*H
print("Seu BAC é ", bac)
print("É ilegal que você dirija.") if bac >= 0.08 else print("É legal que você dirija.")