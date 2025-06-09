# src/facade/sistema_venda_facade.py

from datetime import datetime
from typing import List, Optional

# Importando as classes das entidades (models)
# src/facade/sistema_venda_facade.py

# Importando as classes das entidades (models)
from src.models.cliente import Cliente
from src.models.produto import Produto
from src.models.item_pedido import ItemPedido
from src.models.pedido import Pedido
from src.models.entrega import Entrega
from src.models.avaliacao import Avaliacao
from src.models.comentario import Comentario
from src.models.fornecedor import Fornecedor
from src.models.tutorial import Tutorial

# Importando as classes de estratégia
from src.strategy.metodo_calculo_taxa import MetodoCalculoTaxa
from src.strategy.calcula_taxa_fixa import CalculaTaxaFixa
from src.strategy.calcula_taxa_express import CalculaTaxaExpress
from src.strategy.calcula_taxa_premium import CalculaTaxaPremium

class SistemaVendaFacade:
    """
    SistemaVendaFacade: Fornece uma interface simplificada para o subsistema de vendas,
    orquestrando as operações entre as diversas entidades e utilizando padrões como Strategy.
    """
    def __init__(self):
        # Aqui você pode ter "repositórios" ou listas simples para simular um banco de dados
        # Em um sistema real, isso seria a camada de persistência.
        self._clientes: List[Cliente] = []
        self._produtos: List[Produto] = []
        self._pedidos: List[Pedido] = []
        self._entregas: List[Entrega] = []
        self._fornecedores: List[Fornecedor] = []
        self._tutoriais: List[Tutorial] = []
        self._next_pedido_id = 1
        self._next_entrega_id = 1

    # --- Métodos para Gerenciamento de Clientes ---
    def cadastrar_cliente(self, nome: str, email: str, telefone: str, endereco: str) -> Cliente:
        cliente = Cliente(nome, email, telefone, endereco)
        self._clientes.append(cliente)
        print(f"Facade: Cliente {nome} cadastrado com sucesso.")
        return cliente

    def buscar_cliente_por_email(self, email: str) -> Optional[Cliente]:
        for cliente in self._clientes:
            if cliente.email == email:
                return cliente
        print(f"Facade: Cliente com email {email} não encontrado.")
        return None

    def atualizar_perfil_cliente(self, email: str, nome: str = None, telefone: str = None, endereco: str = None):
        cliente = self.buscar_cliente_por_email(email)
        if cliente:
            cliente.atualizar_perfil(nome, email, telefone, endereco)
            print(f"Facade: Perfil do cliente {email} atualizado.")
        else:
            print(f"Facade: Falha ao atualizar perfil. Cliente com email {email} não encontrado.")

    # --- Métodos para Gerenciamento de Produtos ---
    def adicionar_produto(self, fornecedor_nome: str, nome: str, preco: float, descricao: str = "", categoria: str = "") -> Optional[Produto]:
        fornecedor = self.buscar_fornecedor_por_nome(fornecedor_nome)
        if fornecedor:
            produto = Produto(nome, preco, descricao, categoria)
            fornecedor.adicionar_produto(produto)
            self._produtos.append(produto) # Adiciona ao controle geral de produtos
            print(f"Facade: Produto '{nome}' adicionado pelo fornecedor '{fornecedor_nome}'.")
            return produto
        else:
            print(f"Facade: Fornecedor '{fornecedor_nome}' não encontrado para adicionar produto.")
            return None

    def buscar_produto_por_nome(self, nome: str) -> Optional[Produto]:
        for produto in self._produtos:
            if produto.nome == nome:
                return produto
        print(f"Facade: Produto '{nome}' não encontrado.")
        return None

    # --- Métodos para Gerenciamento de Fornecedores ---
    def cadastrar_fornecedor(self, nome: str, email: str, telefone: str) -> Fornecedor:
        fornecedor = Fornecedor(nome, email, telefone)
        self._fornecedores.append(fornecedor)
        print(f"Facade: Fornecedor {nome} cadastrado com sucesso.")
        return fornecedor

    def buscar_fornecedor_por_nome(self, nome: str) -> Optional[Fornecedor]:
        for fornecedor in self._fornecedores:
            if fornecedor.nome == nome:
                return fornecedor
        print(f"Facade: Fornecedor '{nome}' não encontrado.")
        return None

    # --- Métodos para Gerenciamento de Pedidos ---
    def criar_pedido(self, cliente_email: str) -> Optional[Pedido]:
        cliente = self.buscar_cliente_por_email(cliente_email)
        if cliente:
            pedido = Pedido(cliente_id=len(self._pedidos) + 1, data=datetime.now()) # ID simples
            self._pedidos.append(pedido)
            cliente.pedidos.append(pedido)
            print(f"Facade: Pedido {pedido.cliente_id}-{pedido.data.strftime('%H%M%S')} criado para o cliente {cliente.nome}.")
            return pedido
        else:
            print(f"Facade: Cliente com email {cliente_email} não encontrado. Pedido não pode ser criado.")
            return None

    def adicionar_item_a_pedido(self, pedido_id: int, produto_nome: str, quantidade: int):
        pedido = next((p for p in self._pedidos if p.cliente_id == pedido_id), None)
        produto = self.buscar_produto_por_nome(produto_nome)

        if pedido and produto:
            item = ItemPedido(produto, quantidade)
            pedido.adicionar_item(item)
            print(f"Facade: {quantidade}x '{produto_nome}' adicionado ao pedido {pedido_id}.")
        else:
            print(f"Facade: Não foi possível adicionar item. Pedido {pedido_id} ou produto '{produto_nome}' não encontrado.")

    def finalizar_pedido(self, pedido_id: int, metodo_pagamento: str, metodo_taxa: MetodoCalculoTaxa = None) -> Optional[Pedido]:
        pedido = next((p for p in self._pedidos if p.cliente_id == pedido_id), None) # Usando cliente_id como pedido_id por simplicidade
        if pedido:
            # Lógica de pagamento (simulada)
            print(f"Facade: Processando pagamento do pedido {pedido_id} via {metodo_pagamento}...")
            pedido.atualizar_status_pagamento("Pago")

            # Aplicando a estratégia de cálculo de taxa
            if metodo_taxa:
                taxa = metodo_taxa.calcular_taxa(pedido.valor_total)
                pedido.valor_total += taxa
                print(f"Facade: Taxa de {taxa:.2f} aplicada ao pedido {pedido_id}. Novo total: {pedido.valor_total:.2f}")

            print(f"Facade: Pedido {pedido_id} finalizado com sucesso. Status: {pedido.status_pagamento}")
            return pedido
        else:
            print(f"Facade: Pedido {pedido_id} não encontrado para finalização.")
            return None

    # --- Métodos para Gerenciamento de Entregas ---
    def agendar_entrega(self, pedido_id: int, endereco_entrega: str, data_prevista: datetime) -> Optional[Entrega]:
        pedido = next((p for p in self._pedidos if p.cliente_id == pedido_id), None)
        if pedido:
            entrega = Entrega(self._next_entrega_id, endereco_entrega, data_prevista)
            self._entregas.append(entrega)
            # Associar a entrega ao pedido (se a relação for bidirecional)
            # pedido.entrega = entrega # Se Pedido tivesse um atributo de Entrega
            self._next_entrega_id += 1
            print(f"Facade: Entrega {entrega.id_entrega} agendada para o pedido {pedido_id} no endereço '{endereco_entrega}'.")
            return entrega
        else:
            print(f"Facade: Pedido {pedido_id} não encontrado. Entrega não pode ser agendada.")
            return None

    def atualizar_status_entrega(self, entrega_id: int, novo_status: str):
        entrega = next((e for e in self._entregas if e.id_entrega == entrega_id), None)
        if entrega:
            entrega.atualizar_status(novo_status)
            print(f"Facade: Status da entrega {entrega_id} atualizado para '{novo_status}'.")
        else:
            print(f"Facade: Entrega {entrega_id} não encontrada.")

    # --- Métodos para Avaliações e Comentários ---
    def avaliar_pedido(self, pedido_id: int, nota: int, comentario_texto: str, autor: str):
        pedido = next((p for p in self._pedidos if p.cliente_id == pedido_id), None)
        if pedido:
            avaliacao = Avaliacao(nota, comentario_texto)
            # Determinar se a avaliação é para fornecedor ou entrega (exemplo simplificado)
            if nota >= 3: # Supondo que avaliações boas são para o fornecedor
                pedido.avaliacao_fornecedor = avaliacao
            else: # Avaliações piores podem ser para a entrega
                pedido.avaliacao_entrega = avaliacao
            print(f"Facade: Pedido {pedido_id} avaliado com nota {nota}.")
        else:
            print(f"Facade: Pedido {pedido_id} não encontrado para avaliação.")

    def responder_avaliacao_pedido(self, pedido_id: int, texto_resposta: str, autor_resposta: str, tipo_resposta: str):
        pedido = next((p for p in self._pedidos if p.cliente_id == pedido_id), None)
        if pedido:
            resposta = Comentario(texto_resposta, autor_resposta)
            if tipo_resposta == "fornecedor":
                pedido.resposta_fornecedor = resposta
                print(f"Facade: Resposta do fornecedor adicionada ao pedido {pedido_id}.")
            elif tipo_resposta == "entrega":
                pedido.resposta_entrega = resposta
                print(f"Facade: Resposta da entrega adicionada ao pedido {pedido_id}.")
            else:
                print(f"Facade: Tipo de resposta '{tipo_resposta}' inválido para o pedido {pedido_id}.")
        else:
            print(f"Facade: Pedido {pedido_id} não encontrado para responder avaliação.")

    # --- Métodos para Tutoriais ---
    def criar_tutorial(self, titulo: str, conteudo: str, autor: str) -> Tutorial:
        tutorial = Tutorial(titulo, conteudo, autor)
        self._tutoriais.append(tutorial)
        print(f"Facade: Tutorial '{titulo}' criado por {autor}.")
        return tutorial

    def adicionar_tag_a_tutorial(self, titulo_tutorial: str, tag: str):
        tutorial = next((t for t in self._tutoriais if t.titulo == titulo_tutorial), None)
        if tutorial:
            tutorial.adicionar_tag(tag)
            print(f"Facade: Tag '{tag}' adicionada ao tutorial '{titulo_tutorial}'.")
        else:
            print(f"Facade: Tutorial '{titulo_tutorial}' não encontrado para adicionar tag.")

    # --- Métodos para relatórios/listagens (simplificados) ---
    def listar_todos_pedidos(self) -> List[Pedido]:
        return self._pedidos

    def listar_produtos_do_fornecedor(self, fornecedor_nome: str) -> List[Produto]:
        fornecedor = self.buscar_fornecedor_por_nome(fornecedor_nome)
        if fornecedor:
            return fornecedor.exibir_produtos()
        return []