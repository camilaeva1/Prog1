#import math
comp = int(input("Qual o comprimento da parede? "))
larg = int(input("Qual a largura da parede? "))
area = comp*larg
if area > 360:
    galao = (area//350) + 1
else:
    galao = 1
print("Voce precisará de ", galao, " galões para cobrir ", area, " m².")