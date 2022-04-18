valor = float(input("Digite o valor inicial: "))
taxa = float(input("Sob qual taxa (%)? "))
anos = float(input("Qual o tempo em anos? "))
taxa1 = taxa / 100
A = valor * (1 + (taxa1 * anos))
print("Após {} anos à taxa de {} %, o investimento será de {}".format(anos, taxa, A))
