import math
valor = float(input("Qual o valor do pedido? "))
estado = input("Qual o seu estado de residência? ")
if estado == "Wiscosin":
  munic = input("Qual o seu município? ")
  if munic == "Eau Claire":
    valor1 = valor + valor*0.06
  elif munic == "Dunn":
    valor1 = valor + valor*0.059
  else:
    valor1 = valor + valor*0.055
elif estado == "Illinoiis":
  valor1 = valor +valor*0.08
else:
  valor1 = valor
print("O valor a ser pago é ", valor1)

