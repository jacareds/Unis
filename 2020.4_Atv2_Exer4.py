# Implementar uma função que retorne verdadeiro se
# /o número for primo (falso caso contrário). Testar de 1 a 100.

print ( "Digite um numero de 1 a 100: " )
nunDig = int(input())  #criação de variavel

def rangeres(): #Funsão que checa numero primo
    for count in range(2,100):
        while nunDig % count != 0 or nunDig <= 2:
            print ( "verdadeiro para numero primo" )
            break

        if nunDig % count == 0 and nunDig != 2:
            print ( "falso para numero primo" )
            return False

        else:
            return True

if (nunDig > 0) and (nunDig < 101): #condição que checa se o usuario digitou certo
    rangeres() #chama a funsão se digitou certo

else:
    print ( "Digite um numero entre 1 e 100." )