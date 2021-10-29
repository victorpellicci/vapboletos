import sqlite3

# conectando...
conn = sqlite3.connect('database.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE database (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        idexterno INTEGER,
        numero TEXT NOT NULL,
        cor     VARCHAR(111) NOT NULL,
        
        criado_em DATE NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()