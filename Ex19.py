peso = float(input("Qual o seu peso(libras)? "))
alt = float(input("Qual a sua altura (polegadas)? "))
IMC = (peso/(alt * alt)) * 703
if IMC < 18.5:
  print("Seu IMC é ", IMC, " você está abaixo do peso ideal.")
elif IMC >= 18.5 and IMC <= 25:
  print("Seu IMC é ", IMC, " , você está no peso ideal.")
else: 
  print("Seu IMC é ", IMC, " você está acima do peso.")
