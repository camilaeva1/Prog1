#import math
print("Pressione C se deseja converter Fahrenheit em Celcius.")
print("Pressione F se deseja converter Celcius em Fahrenheit.")
med = input("C ou F? ")
if med == 'C':
    fa = float(input("Por favor entre com a temperatura em Fahrenheit: "))
    temp = ((fa - 32) * 5)/9
    print("A temperatura em celcius é ", temp)
elif med == 'F':
    ce = float(input("Por favor entre com a temperatura em celcius: "))
    temp = (ce * 9/5) + 32
    print("A temperatura em fahrenheit é ", temp)
else:
    print("Entre com uma medida válida!")