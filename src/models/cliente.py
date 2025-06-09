# src/models/cliente.py

from datetime import datetime

class Cliente:
    def __init__(self, nome: str, email: str, telefone: str, endereco: str):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.configuracoes = {}  # Dicionário para configurações
        self.avaliacoes_recebidas = [] # Lista de avaliações recebidas (serão objetos Avaliacao)
        self.pedidos = []  # Lista de objetos Pedido

    def avaliar_pedido(self, pedido_id: int, nota: int, mensagem: str):
        # Lógica para avaliar um pedido específico (será implementado via fachada)
        print(f"Cliente {self.nome} avaliou o pedido {pedido_id} com nota {nota}: {mensagem}")

    def atualizar_perfil(self, nome: str = None, email: str = None, telefone: str = None, endereco: str = None):
        if nome:
            self.nome = nome
        if email:
            self.email = email
        if telefone:
            self.telefone = telefone
        if endereco:
            self.endereco = endereco
        print(f"Perfil do cliente {self.nome} atualizado.")

    def definir_localizacao_gps(self, latitude: float, longitude: float):
        self.configuracoes['gps_location'] = {'latitude': latitude, 'longitude': longitude}
        print(f"Localização GPS do cliente {self.nome} definida para ({latitude}, {longitude}).")

    def __str__(self):
        return f"Cliente(nome='{self.nome}', email='{self.email}')"