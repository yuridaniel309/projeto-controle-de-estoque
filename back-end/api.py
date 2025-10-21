from fastapi import FastAPI
from funcao import listar_produtos, deletar_produto, criar_tabela, inserir_produtos, atualizar_produto, buscar_quantidade

# Rodar o fastapi:
# python -m uvicorn api:app --reload

# /docs > Documentação Swagger
# /redoc > Documentação redoc

app = FastAPI(title="Estoque de produtos")

#GET = Pegar / listar
#POST = Criar / Enviar
#PUT = Atualizar
#DELETE = deletar

# 127.0.0.1:8000
@app.get("/")
def home():
    return{"mensagem": "Bem-vindo ao Estoque de produtos"}

@app.post("/Produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    inserir_produtos(nome, categoria, preco, quantidade)
    return { "mensagem": "Produto adicionado com sucesso!"}

@app.get("/Produtos")
def visualizar_produtos():
    produtos = listar_produtos()
    lista = []
    for produto in produtos:
        lista.append({ 
            "id": produto[0], 
            "nome": produto[1], 
            "categoria": produto[2], 
            "preco": produto[3], 
            "quantidade": produto[4]})
    return {"produtos": lista}
