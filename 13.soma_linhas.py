#Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida, ler uma matriz de M linhas e N colunas contendo números reais. Gerar um vetor de modo que cada elemento do vetor seja a soma dos elementos da linha correspondente da matriz. Mostrar o vetor gerado. 

m=int(input("Qual quantidade de linhas da matriz? "))
n=int(input("Qual quantidade colunas da matriz? "))
mat:[[float]]=[[0 for x in range(n)] for x in range(m)]
vet:[float]=[0 for x in range(m)]

for i in range(0, m):
       print(f"Digite os elementos da {i+1}a linha: ")
       for j in range(0, n):
             mat[i][j]=float(input())

for i in range(0, m):
       for j in range(0,n):
             vet[i]=vet[i]+mat[i][j]

print("VETOR GERADO:")
for i in range(0, m):
       print(f"{vet[i]:.1f}")
