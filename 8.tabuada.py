#Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo.

x=int(input("Deseja a tabuada para qual valor? "))
for i in range(0, 10):
      resultado=(i+1)*x
      print(f"{x} x {i} = {resultado}")
