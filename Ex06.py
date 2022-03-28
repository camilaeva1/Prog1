#Retirement Calculator
import datetime
from xmlrpc.client import DateTime

idatual = int(input("What is your current age? "))
aposentar = int(input("At what age would you like to retire? "))
falta = aposentar - idatual
print("You have", falta, "years left until you can retire.", sep = " ", end = "\n")
date = datetime.date.today()
year = int(date.strftime("%Y"))
print("It's ", year, "so you can retire in", year+falta, ".", sep = " ", end = "\n")