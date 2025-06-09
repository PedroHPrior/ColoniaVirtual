# src/models/item_pedido.py

from .produto import Produto # Import relativo dentro do pacote models

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self) -> float:
        return self.produto.preco * self.quantidade

    def obter_informacoes_produto(self) -> str:
        return f"{self.produto.nome} (quantidade: {self.quantidade})"

    def __str__(self):
        return f"ItemPedido(produto='{self.produto.nome}', quantidade={self.quantidade})"