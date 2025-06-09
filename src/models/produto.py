# src/models/produto.py

class Produto:
    def __init__(self, nome: str, preco: float, descricao: str = "", categoria: str = ""):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.categoria = categoria

    def exibir_preco(self):
        return self.preco

    def mudar_preco(self, novo_preco: float):
        if novo_preco >= 0:
            self.preco = novo_preco
            print(f"Preço do produto '{self.nome}' atualizado para {self.preco:.2f}.")
        else:
            print("Erro: O novo preço não pode ser negativo.")

    def alterar_categoria(self, nova_categoria: str):
        self.categoria = nova_categoria
        print(f"Categoria do produto '{self.nome}' alterada para '{self.categoria}'.")

    def __str__(self):
        return f"Produto(nome='{self.nome}', preco={self.preco:.2f})"