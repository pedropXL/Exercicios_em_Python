#Fazer um programa para ler um número inteiro N (máximo = 10) e uma matriz quadrada de ordem N contendo números inteiros. Em seguida, mostrar a diagonal principal e a quantidade de valores negativos da matriz.

n=int(input("Qual a ordem da matriz? "))
mat:[[int]]=[[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
       for j in range(0, n):
             mat[i][j]=int(input(f"Elemento [{i},{j}]: "))

print("Diagonal principal:")
for i in range(0, n):
       for j in range(0, n):
             if i==j:
                print(f"{mat[i][j]} ", end="")

print()
negativos=0
for i in range(0, n):
       for j in range(0, n):
             if mat[i][j]<0:
                negativos=negativos+1

print(f"QUANTIDADE DE NEGATIVOS = {negativos}")
