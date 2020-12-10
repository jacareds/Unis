# coding=utf-8

import sqlite3
import main

#criando conexão com server
con = sqlite3.connect('person.db')
cur = con.cursor()

#inserir registros
sql = 'insert into person values (null,?,?)'

#dados
recset = [(main.imc,main.mensG)]

#insert os registros
for rec in recset:
    cur.execute(sql,rec)

#confirma a transação
con.commit()

#fecha banco
con.close()