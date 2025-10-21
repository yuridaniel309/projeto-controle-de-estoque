from conexao import conectar

def criar_tabela():
    conexao,cursor = conectar()
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
    conexao,cursor = conectar()
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
    conexao,cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM  produto ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"erro ao tentar listar produto")
        finally:
            cursor.closse()
            conexao.closse()

def atualizar_produto(novo_preço, novo_quantidade, id_produtos):
     conexao, cursor = conectar()
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

def deletar_produto(id_produtos):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            "DELETE FROM produto WHERE id = %s", (id_produtos,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao tentar deletar filme")
        finally:
            cursor.close()
            conexao.close()
 


def buscar_quantidade(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT nome, quantidade FROM produtos WHERE id = %s",
                (id_produto,)
            )
            return cursor.fetchone() 
        except Exception as erro:
            print(f"Erro ao buscar produto: {erro}")
            return None
        finally:
            cursor.close()
            conexao.close()
    return None