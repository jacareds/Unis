# Exer1 Atividade2

# Faça um programa que leia a idade de uma pessoa expressa em dias e
# mostre-a expressa em anos, meses e dias.
#29212
#0 meses
#12 dias

#entrada de dados
idade = int(input("Digite sua idade em dias:"))

#obtensão dos anos em numero inteiro
modAno = int(idade / 365)

#modulo da idade para se obter dias(resto da divisão)
modMeses = int(idade % 365)

#if para saber a diferença entre mês e dia
if modMeses <= 30:
	modMeses = 0
	modDias = int(idade % 365)
else:
	modMeses = int(modMeses % 12)
	modDias = int(idade % 30)

#saida
print (" Voce tem ", (modAno),"anos,",(modMeses),"meses e ",(modDias)," dias.")
