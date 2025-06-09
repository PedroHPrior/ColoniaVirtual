# src/models/entrega.py

from datetime import datetime
# Importar Avaliacao quando for usado como tipo
# from .avaliacao import Avaliacao

class Entrega:
    def __init__(self, id_entrega: int, endereco_entrega: str, data_prevista: datetime, status_entrega: str = "Pendente"):
        self.id_entrega = id_entrega
        self.endereco_entrega = endereco_entrega
        self.data_prevista = data_prevista
        self.data_realizacao = None
        self.status_entrega = status_entrega # "Pendente", "Em Trânsito", "Entregue", "Cancelado"
        self.observacoes = ""
        self.avaliacao = None # Objeto Avaliacao

    def atualizar_status(self, novo_status: str):
        self.status_entrega = novo_status
        if novo_status == "Entregue":
            self.data_realizacao = datetime.now()
        print(f"Status da entrega {self.id_entrega} atualizado para: {self.status_entrega}")

    def adicionar_observacao(self, obs: str):
        self.observacoes = obs
        print(f"Observação adicionada à entrega {self.id_entrega}.")

    def calcular_tempo_entrega(self) -> float:
        if self.data_realizacao and self.data_prevista:
            return (self.data_realizacao - self.data_prevista).total_seconds() / 3600 # Tempo em horas
        return 0.0

    def __str__(self):
        return f"Entrega(id={self.id_entrega}, status='{self.status_entrega}', endereco='{self.endereco_entrega}')"