while True:
    print("Qual a sua idade?")
    idade = input()
    try:
        idade = int(idade)
    except:
        print("Digite numerais!")
        continue
    if idade < 1:
        print("Digite uma idade válida!")
        continue
    break
if idade < 18:
    print("Você não tem idade para dirigir!")
elif idade >= 18:
    print("Você tem idade legal para dirigir!")
else:
    print("Digite uma idade válida!")