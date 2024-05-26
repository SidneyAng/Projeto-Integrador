# -*- coding: utf-8 -*-
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('donations.db')
cursor = conn.cursor()

# Apagar todas as solicitações
cursor.execute('DELETE FROM solicitacao')

# Confirmar a transação
conn.commit()

# Fechar a conexão
conn.close()

print("Todas as solicitações foram removidas!")
