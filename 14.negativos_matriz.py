#Ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros, conforme exemplo. Em seguida, mostrar na tela somente os números negativos da matriz.

m=int(input("Qual a quantidade de linhas da matriz? "))
n=int(input("Qual a quantidade colunas da matriz? "))
mat:[[int]]=[[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
       for j in range(0, n):
             mat[i][j]=int(input(f"Elemento [{i},{j}]: "))

print("VALORES NEGATIVOS:")
for i in range(0, m):
      for j in range(0, n):
            if mat[i][j]<0:
               print(f"{mat[i][j]}")
