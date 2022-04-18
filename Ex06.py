#Retirement Calculator
import datetime
from xmlrpc.client import DateTime

idatual = int(input("Qual sua idade atual? "))
aposentar = int(input("Com que idade quer se aposentar? "))
falta = aposentar - idatual
print("Faltam", falta, "anos para você se aposentar.", sep = " ", end = "\n")
date = datetime.date.today()
year = int(date.strftime("%Y"))
print("Estamos em ", year, " faltam ", year+falta, " para você se aposentar.", sep = " ", end = "\n")
