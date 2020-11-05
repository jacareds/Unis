#Escreva uma função que:
#a) Receba uma frase como parâmetro.
#b) Retorne uma nova frase com cada palavra com as letras invertidas.

def inverText(text):
    inversor = (text)
    print(inversor[::-1])

entradInput = str(input("Digite uma frase:  "))
inverText(entradInput)

