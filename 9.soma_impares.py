#Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números impares entre eles.


print("Digite dois numeros:")
x=int(input())
y=int(input())
if x>y:
    z=x
    x=y
    y=z

soma=0
for i in range (x+1, y):
      if i%2!=0:
          soma=soma+i

print(f"SOMA DO SIMPARES = {soma}")
