import math  
preco1 = float(input("Insira o preço do item 1: "))
quant1 = float(input("\nInsira a quantidade do item 1: "))
preco2 = float(input("\nInsira o preço do item 2: "))
quant2 = float(input("\nInsira a quantidade do item 2: "))
preco3 = float(input("\nInsira o preço do item 3: "))
quant3 = float(input("\nInsira a quantidade do item 3: "))
totalbruto = ((preco1 * quant1) + (preco2 * quant2) + (preco3 * quant3))
print("Subtotal = R$ ", round(totalbruto,2))
Taxa = totalbruto * 0.055
print("Taxa = R$ ", round(Taxa,2))
total = totalbruto - Taxa
print("Total = R$ ", round(total,2))
