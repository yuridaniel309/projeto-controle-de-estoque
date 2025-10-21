from conexao import coneatar

def criar_tabela():
    conexao,cursor = coneatar()
    if conexao:
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto(
            id SERIAL PRIMARY KEY,
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

def inserir_produtos(nome, categoria, preço, quantidade):
    conexao,cursor = coneatar()
    if conexao:
        try:
            cursor.execute(
            "INSERT INTO produto(nome, categoria, preço, quantidade) VALUES (%s, %s, %s, %s)",
            (nome, categoria, preço, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao inserir produtos {erro}")
        finally:
            cursor.close()
            conexao.close()


def listar_produtos():
    conexao,cursor = coneatar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM  produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"erro ao tentar listar produtos")
        finally:
            cursor.closse()
            conexao.closse()

def atualizar_produto(novo_preço, novo_quantidade, id_produtos):
     conexao, cursor = coneatar()
     if conexao:
        try:
            cursor.execute(
            "UPDATE produto SET preço = %s,quantidade = %s WHERE id = %s", 
            (id_produtos, novo_quantidade, novo_preço)
        )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao tentar atualizar produto")
        finally:
            cursor.close()
            conexao.close()
atualizar_produto( 1, 25, 16)

