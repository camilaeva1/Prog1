n = int(input("Insira o número total de eleitores: "))
cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
for i in range(0, n+1):
    voto = str(input("EM QUEM VOCÊ VAI VOTAR? "))
    if voto == "LULA":
        cont = cont + 1
    if voto == "BOLSONARO":
        cont1 = cont1 + 1
    if voto == "CIRO":
        cont2 = cont2 + 1
    if voto == "SIMONE":
        cont3 = cont3 + 1
    if voto == "FELIPE":
        cont4 = cont4 + 1
    if voto == "SORAYA":
        cont5 = cont5 +1
print("O candidato Lula obteve {} votos".format(cont))
print("O candidato Bolsonaro obteve {} votos".format(cont1))
print("O candidato Ciro obteve {} votos".format(cont2))
print("O candidato simone obteve {} votos".format(cont3))
print("O candidato Felipe obteve {} votos".format(cont4))
print("O candidato Soraya obteve {} votos".format(cont5))
