# Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo.
# Supor que os valores lidos são inteiros e positivos.
# Caso os valores formem um triângulo, calcular e escrever a área deste triângulo.
# Se não formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo algum,
# se a é o maior).
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
# 5 ,10 ,9
# area = b.h/2

print ( "Entre com 3 valores de numeros inteiros e positivos,\nque formam um triangulo; para saber sua área." )
A = int ( input ( "primeiro valor, A:" ) )
B = int ( input ( "segundo valor, B:" ) )
C = int ( input ( "terceiro valor, C:" ) )

# checa maior e menor numero
maiorValor = C
if (A > maiorValor):
    maiorValor = A
if (B > maiorValor):
    maiorValor = B

menorValor = C
if (A < menorValor):
    menorValor = A
if (B < menorValor):
    menorValor = B

# descobrir o valor do Meio
if (menorValor == A) and (maiorValor == B):
    valordoMeio = ( C )
if (menorValor == B) and (maiorValor == A):
    valordoMeio = ( C )

if (menorValor == C) and (maiorValor == A):
    valordoMeio = ( B )
if (menorValor == A) and (maiorValor == C):
    valordoMeio = ( B )

if (menorValor == B) and (maiorValor == C):
    valordoMeio = ( A )
if (menorValor == C) and (maiorValor == B):
    valordoMeio = ( A )

# certificação de criação de triangulo
areaTriangulo = None
if B % C < A < B + C:
    if A % C < B < A + C:
        if A % B < C < A + B:
            areaTriangulo  = int (menorValor * valordoMeio / maiorValor)
            print ( "A área do triangulo é:%d" % (areaTriangulo) )

if areaTriangulo == None:
	print ( "Triangulo não formado, valores digitados: maior valor '{}', valor do meio '{}', menor valor '{}'".format ( maiorValor, valordoMeio, menorValor ) )


