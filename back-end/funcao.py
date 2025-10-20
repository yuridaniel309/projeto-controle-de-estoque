from conexao import coneatar

def criar_tabela():
    conexao,cursor = coneatar()
    if conexao:
        try:
            cursor.execute("""
            CREATE table produto()
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100)NOT NULL,
            categoria VARCHAR(50),
            preco DECIMAL(10,2),
            quantidade INT
             )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

            




