#Faça um programa que leia 3 números inteiros e mostre o menor deles.
print("Digite 3 valores de numeros inteiros:")
A = int(input())
B = int(input())
C = int(input())

menorValor = C
if (A < menorValor):
    menorValor = A
if (B < menorValor):
    menorValor = B

print("O menor valor digitado é: %d" % (menorValor))

