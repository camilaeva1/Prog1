FAÇA UM PROGRAMA QUE LEIA UM NÚMERO N E IMPRIMA N LINHAS NA TELA COM O SEGUINTE FORMATO (MEIO LOSANGO)
n = int(input("Insira um número: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
for i in range(1, n+1):
    for j in range(1, n+1 - i):
        print(j, end = " ")
    print() 
