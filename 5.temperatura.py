temperatura=input("Voce vai digitar a temperatura em qual escala (C/F)? ")
if temperatura=="F":
   f=float(input("Digite a temperatura em Fahrenheit: "))
   c=5/9*(f-32)
   print(f"Temperatura equivalente em Celcius: {c:.2f}")
else:
   c=float(input("Digite a temperetura em Celcius: "))
   f=(9/5*c)+32
   print(f"Temperatura equivalente em Fahrenheit: {f:.2f}")
