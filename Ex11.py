import os
os.system('cls')

moeda = input("Qual a moeda que vc quer trocar? ")
if moeda == 'euros':
    euros1 = float(input("Quantos euros vc está trocando? "))
    exchange_rate = float(input("Qual a taxa de câmbio do euro?"))

    dollars = (euros1 * exchange_rate) // 100
    print(dollars)
    print(f"{euros1:.2f} euros a uma taxa de câmbio de  {exchange_rate} é "+ f"{dollars:.2f} dólares americanos.")
elif moeda == 'dolar' or moeda == 'dólar':
    dolar = float(input("Quantos dólares vc está trocando? "))
    exchange_rate2 = float(input("\nQual a taxa de câmbio do dolar?"))

    euros2 = (dolar * exchange_rate2) // 100
    print(euros2)
    print(f"{dolar:.2f} euros a uma taxa de câmbio de  {exchange_rate2} é "+ f"{euros2:.2f} dólares americanos.")
else:
    print("Digite uma moeda válida!")
