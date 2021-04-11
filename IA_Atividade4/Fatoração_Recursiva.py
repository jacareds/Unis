'''def fatorial(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * fatorial(n-1)'''


lista = [12,15,7]

def fatR(n):
	if n == 0:
		return 1
	else:
		return n * fatR(n-1)


cal = max(lista)
print("Usando a lista ", lista, ". Valor máximo dos números encontrado em sua fatoração recursiva: ",  fatR(cal))
