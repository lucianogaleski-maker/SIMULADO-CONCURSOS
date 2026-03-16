import sqlite3
from datetime import datetime

# Conectar ao banco
conn = sqlite3.connect('instance/simulado.db')
cursor = conn.cursor()

# Adicionar coluna criado_em na tabela usuario
try:
    cursor.execute("ALTER TABLE usuario ADD COLUMN criado_em TIMESTAMP")
    print("Coluna 'criado_em' adicionada à tabela usuario")
except sqlite3.OperationalError as e:
    print(f"Coluna já existe ou erro: {e}")

# Atualizar usuários existentes
cursor.execute("UPDATE usuario SET criado_em = ? WHERE criado_em IS NULL", (datetime.utcnow(),))
print(f"{cursor.rowcount} usuários atualizados")

# Criar tabela de acessos
cursor.execute('''
CREATE TABLE IF NOT EXISTS acesso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip VARCHAR(50),
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pagina VARCHAR(200),
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
)
''')
print("Tabela 'acesso' criada")

conn.commit()
conn.close()
print("\nBanco atualizado com sucesso!")
