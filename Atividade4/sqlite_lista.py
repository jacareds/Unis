# coding=utf-8

import sqlite3

#criando conexão com server
con = sqlite3.connect('person.db')
cur = con.cursor()

#select nos registros
cur.execute('select * from person')

#recupera lista
recset = cur.fetchall()

#mostra lista
for rec in recset:
    print ("%d: %s(%s)" % rec)

#fecha a conexão
con.close()