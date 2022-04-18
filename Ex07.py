#import math
while True:
    print("Qual o comprimento da sala em pés?")
    comp = input()
    try:
        comp = int(comp)
    except:
        print("Por favor use dígitos numéricos.")
        continue
    if comp < 1:
        print("Por favor use um número positivo.")
        continue
    break
while True:
    print("Qual a largura da sala em pés?")
    larg = input()
    try:
        larg = int(larg)
    except:
        print("Por favor use dígitos numéricos.")
        continue
    if larg < 1:
        print("Por favor use um número positivo.")
        continue
    break
print("Você inseriu ", comp, " por ", larg, "pés.")
area = comp * larg
aream = area * 0.09290304
print("A área é ", area, " pés. Corresponde a ", aream, " m².")


