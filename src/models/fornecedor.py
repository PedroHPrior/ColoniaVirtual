# src/models/fornecedor.py

from typing import List
from .produto import Produto # Import relativo

class Fornecedor:
    def __init__(self, nome: str, email: str, telefone: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.media_avaliacoes = 0.0
        self.produtos: List[Produto] = [] # Lista de objetos Produto

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado ao fornecedor '{self.nome}'.")

    def remover_produto(self, produto_nome: str):
        self.produtos = [p for p in self.produtos if p.nome != produto_nome]
        print(f"Produto '{produto_nome}' removido do fornecedor '{self.nome}'.")

    def exibir_produtos(self, categoria: str = None) -> List[Produto]:
        if categoria:
            return [p for p in self.produtos if p.categoria == categoria]
        return self.produtos

    def atualizar_media_avaliacoes(self, nova_media: float):
        self.media_avaliacoes = nova_media
        print(f"Média de avaliações do fornecedor '{self.nome}' atualizada para {self.media_avaliacoes:.2f}.")

    def __str__(self):
        return f"Fornecedor(nome='{self.nome}', email='{self.email}')"