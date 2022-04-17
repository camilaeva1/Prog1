#Saying hello
#Crie um programa que solicite seu nome e imprima uma saudação usando seu nome

nome = input("Qual o seu nome? ")
print("Olá", nome, "prazer em te conhecer!", sep = " ", end = "\n")

#Desafio 01
#Imprimir a entrada do usuário sem necessariamente usar uma variável um input. Nesse caso usei uma função (def)

def hello(nome):
     print("Olá " + nome + ", prazer em te conhecer!", sep = " ", end = "\n")
#Programa principal
hello("Camila")


