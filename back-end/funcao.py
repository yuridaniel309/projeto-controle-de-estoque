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
            preço DECIMAL(10,2),
            quantidade INT
             )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

criar_tabela()

def inserir_produtos(nome,categoria,preço,quantidade):
    conexao,cursor = coneatar()
    if conexao:
        try:
            cursor.execute(
            "INSERT INTO produtos(nome,categoria,preço,quantidade) VALUES (%s,%s,%s,%s)",
            (nome,categoria,preço,quantidade)
            )
            conexao.connit()
        except Exception as erro:
            print(f"erro ao inserir produtos")
        finally:
            cursor.close()
            conexao.close()
        
                 

            




