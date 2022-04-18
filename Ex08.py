#import math
pes = int(input("Quantas pessoas? "))
piz = int(input("Quantas pizzas você tem? "))
print(pes, " pessoas com ", piz, " pizzas;")
pedaco = piz * 8
pizt = pedaco//pes
print("Cada pessoa comerá ", pizt, "pedaços de pizza.")
rest = pedaco - (pes*pizt)
print("Restarão ", rest, " pedaços.")