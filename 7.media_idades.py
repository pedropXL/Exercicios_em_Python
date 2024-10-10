#Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, mostrar a mensagem "IMPOSSIVEL CALCULAR".


print("Digite as idades:")
x=int(input())
soma=0
quantidade=0
while x>=0:
            soma=soma+x
            x=int(input())
            quantidade=quantidade+1

if quantidade==0:
    print("IMPOSSIVEL CALCULAR")
else: 
    media=soma/quantidade
    print(f"MEDIA = {media:.2f}")
