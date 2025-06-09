# src/models/pedido.py

from datetime import datetime
from typing import List
from .item_pedido import ItemPedido # Import relativo
# Importar Avaliacao e Comentario quando forem usados como tipos (adição futura ou para clareza)
# from .avaliacao import Avaliacao
# from .comentario import Comentario

class Pedido:
    def __init__(self, cliente_id: int, data: datetime = None, valor_total: float = 0.0):
        self.cliente_id = cliente_id
        self.data = data if data else datetime.now()
        self.valor_total = valor_total
        self.status_pagamento = "Pendente" # Pode ser "Pendente", "Pago", "Cancelado"
        self.itens_pedido: List[ItemPedido] = []
        self.avaliacao_fornecedor = None # Objeto Avaliacao
        self.avaliacao_entrega = None # Objeto Avaliacao
        self.resposta_fornecedor = None # Objeto Comentario
        self.resposta_entrega = None # Objeto Comentario


    def adicionar_item(self, item: ItemPedido):
        self.itens_pedido.append(item)
        self.calcular_valor_total()

    def calcular_valor_total(self) -> float:
        total = sum(item.calcular_subtotal() for item in self.itens_pedido)
        self.valor_total = total
        return total

    def atualizar_status_pagamento(self, novo_status: str):
        self.status_pagamento = novo_status
        print(f"Status de pagamento do pedido atualizado para: {self.status_pagamento}")

    def gerar_detalhes_pedido(self) -> str:
        detalhes = f"Pedido do Cliente ID: {self.cliente_id}\n"
        detalhes += f"Data: {self.data.strftime('%Y-%m-%d %H:%M:%S')}\n"
        detalhes += "Itens:\n"
        for item in self.itens_pedido:
            detalhes += f"- {item.obter_informacoes_produto()} (Subtotal: {item.calcular_subtotal():.2f})\n"
        detalhes += f"Valor Total: {self.valor_total:.2f}\n"
        detalhes += f"Status de Pagamento: {self.status_pagamento}"
        return detalhes

    def __str__(self):
        return f"Pedido(cliente_id={self.cliente_id}, data={self.data.strftime('%Y-%m-%d')}, valor_total={self.valor_total:.2f}, status_pagamento='{self.status_pagamento}')"