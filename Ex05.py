#Simple Math

n1 = int(input("What is the first number? "))
n2 = int(input("What is the second number? "))
print(n1, "+", n2, "=", n1+n2, sep = " ", end = "\n")
print(n1, "-", n2, "=", n1-n2, sep = " ", end = "\n")
print(n1, "*", n2, "=", n1*n2, sep = " ", end = "\n")
print(n1, "/", n2, "=", n1/n2, sep = " ", end = "\n")

#Desafio 01: verificar se foram inseridos valores numéricos

n1 = input("What is the first number? ")
print(ord(n1))
if(ord(n1) >= 48 and ord(n1) <= 57):
    n2 = input("What is the second number? ")
    n1n = int(n1)
    n2n = int(n2)
    if(ord(n2) >= 48 and ord(n2) <= 57):
      print(n1n, "+", n2n, "=", n1n+n2n, sep = " ", end = "\n")
      print(n1n, "-", n2n, "=", n1n-n2n, sep = " ", end = "\n")
      print(n1n, "*", n2n, "=", n1n*n2n, sep = " ", end = "\n")
      print(n1n, "/", n2n, "=", n1n/n2n, sep = " ", end = "\n")
    else:
      print("It is Not a Number")
else:
    print("It is Not a Number")
