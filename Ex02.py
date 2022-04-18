#Counting the Number of Characters
#Desafio 01 Informar ao uduário que ele deve inserir algo no programa
texto = input("What is the input string? ")
ncaracter = len(texto)
print(ncaracter)
if(ncaracter == 0):
  print("Digite algo no programa!")
else:
  print(texto, "has", ncaracter, "caracther.", sep = " ", end = "\n")





 
