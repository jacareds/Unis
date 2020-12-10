# coding=utf-8

import sqlite3

#criando conexão com server
con = sqlite3.connect('person.db')
cur = con.cursor()

#cria tabela
sql = 'create table person'\
        '(id integer primary key,'\
        'condition varchar(50),'\
        'result numeric)'
cur.execute(sql)

#fecha banco sqlite3
con.close()

print("banco criado")

alt = float(input("digite sua altura em metros e centimentros:   "))
peso = float(input("digite seu peso em kilos:   "))
imc = peso / (alt ** 2)

if imc < 18.5:
    mensG = ("Abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    mensG = ("Peso normal!")
elif imc >= 25 and imc < 30:
    mensG = ("Sobre peso!")
elif imc >= 30 and imc < 40:
    mensG = ("Obesidade!")
elif imc >= 40:
    mensG = ("Obesidade mórbida!")

print(mensG)










