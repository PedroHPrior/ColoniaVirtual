# src/main.py

from src.facade.sistema_venda_facade import SistemaVendaFacade
from src.strategy.calcula_taxa_fixa import CalculaTaxaFixa
from src.strategy.calcula_taxa_express import CalculaTaxaExpress
from src.strategy.calcula_taxa_premium import CalculaTaxaPremium
from datetime import datetime, timedelta

def main():
    print("Iniciando o Sistema de Vendas de Produtos Coloniais...")
    facade = SistemaVendaFacade()

    # --- 1. Cadastrar Clientes e Fornecedores (Colonias/Produtores) ---
    print("\n--- 1. Cadastrando Clientes e Fornecedores (Colonos) ---")
    cliente1 = facade.cadastrar_cliente("Ana Silva", "ana.silva@comprador.com", "11987654321", "Rua das Rosas, 123, Bairro Jardim, São Paulo")
    cliente2 = facade.cadastrar_cliente("Bruno Costa", "bruno.costa@comprador.com", "21912345678", "Av. Central, 456, Centro, Rio de Janeiro")

    # Colonos/Produtores com nomes mais apropriados
    fornecedor1 = facade.cadastrar_fornecedor("Sítio do Vovô Chico", "contato@sitiodovovochico.com", "554933221100")
    fornecedor2 = facade.cadastrar_fornecedor("Cantinho da Roça", "vendas@cantinhodaroca.com", "555198765432")

    # --- 2. Adicionar Produtos Coloniais ---
    print("\n--- 2. Adicionando Produtos Coloniais ---")
    # Ajustando nomes e valores para produtos coloniais
    produto1 = facade.adicionar_produto(fornecedor1.nome, "Queijo Colonial Artesanal (500g)", 35.00, "Queijo curado de leite de vaca, feito artesanalmente.", "Laticínios")
    produto2 = facade.adicionar_produto(fornecedor1.nome, "Salame Colonial (350g)", 28.50, "Salame defumado, com tempero caseiro.", "Embutidos")
    produto3 = facade.adicionar_produto(fornecedor2.nome, "Doce de Leite Cremoso (600g)", 22.00, "Doce de leite tradicional, sem conservantes.", "Doces e Geleias")
    produto4 = facade.adicionar_produto(fornecedor2.nome, "Pão Artesanal de Fermentação Natural (800g)", 18.00, "Pão rústico, fermentação longa, casca crocante.", "Panificação")
    produto5 = facade.adicionar_produto(fornecedor1.nome, "Geleia de Morango Caseira (300g)", 15.00, "Geleia feita com frutas frescas da estação.", "Doces e Geleias")


    # --- 3. Criar e Montar Pedidos ---
    print("\n--- 3. Criando e Montando Pedidos ---")
    pedido1 = facade.criar_pedido(cliente1.email) # Pedido da Ana
    if pedido1:
        facade.adicionar_item_a_pedido(pedido1.cliente_id, "Queijo Colonial Artesanal (500g)", 2) # 2x35 = 70
        facade.adicionar_item_a_pedido(pedido1.cliente_id, "Salame Colonial (350g)", 3) # 3x28.50 = 85.50
        facade.adicionar_item_a_pedido(pedido1.cliente_id, "Geleia de Morango Caseira (300g)", 1) # 1x15 = 15
        # Total do pedido 1: 70 + 85.50 + 15 = 170.50

    pedido2 = facade.criar_pedido(cliente2.email) # Pedido do Bruno
    if pedido2:
        facade.adicionar_item_a_pedido(pedido2.cliente_id, "Doce de Leite Cremoso (600g)", 2) # 2x22 = 44
        facade.adicionar_item_a_pedido(pedido2.cliente_id, "Pão Artesanal de Fermentação Natural (800g)", 4) # 4x18 = 72
        facade.adicionar_item_a_pedido(pedido2.cliente_id, "Queijo Colonial Artesanal (500g)", 1) # 1x35 = 35
        # Total do pedido 2: 44 + 72 + 35 = 151.00


    # --- 4. Finalizar Pedidos com Diferentes Estratégias de Taxa ---
    print("\n--- 4. Finalizando Pedidos com Diferentes Estratégias de Taxa ---")

    # Pedido 1 com taxa fixa
    print(f"\nDetalhes do Pedido 1 antes da finalização: {pedido1.gerar_detalhes_pedido()}")
    taxa_fixa = CalculaTaxaFixa(10.00) # Taxa fixa de R$10 para entrega
    finalizado_pedido1 = facade.finalizar_pedido(pedido1.cliente_id, "Cartão de Crédito", taxa_fixa)
    if finalizado_pedido1:
        print(f"Pedido 1 finalizado. Valor total com taxa: {finalizado_pedido1.valor_total:.2f}")

    # Pedido 2 com taxa express
    print(f"\nDetalhes do Pedido 2 antes da finalização: {pedido2.gerar_detalhes_pedido()}")
    taxa_express = CalculaTaxaExpress(0.05) # 5% de taxa de entrega para expressa
    finalizado_pedido2 = facade.finalizar_pedido(pedido2.cliente_id, "Pix", taxa_express)
    if finalizado_pedido2:
        print(f"Pedido 2 finalizado. Valor total com taxa: {finalizado_pedido2.valor_total:.2f}")

    # --- 5. Agendar e Atualizar Entregas ---
    print("\n--- 5. Agendando e Atualizando Entregas ---")
    data_entrega_pedido1 = datetime.now() + timedelta(days=2)
    entrega1 = facade.agendar_entrega(pedido1.cliente_id, cliente1.endereco, data_entrega_pedido1)
    if entrega1:
        facade.atualizar_status_entrega(entrega1.id_entrega, "Em Trânsito")
        facade.atualizar_status_entrega(entrega1.id_entrega, "Entregue")

    data_entrega_pedido2 = datetime.now() + timedelta(days=1) # Entrega mais rápida para o express
    entrega2 = facade.agendar_entrega(pedido2.cliente_id, cliente2.endereco, data_entrega_pedido2)
    if entrega2:
        facade.atualizar_status_entrega(entrega2.id_entrega, "Em Trânsito")
        facade.atualizar_status_entrega(entrega2.id_entrega, "Entregue")

    # --- 6. Avaliar Pedidos ---
    print("\n--- 6. Avaliando Pedidos ---")
    facade.avaliar_pedido(pedido1.cliente_id, 5, "Produtos frescos e de excelente qualidade! Chegou rapidinho.", cliente1.nome)
    facade.avaliar_pedido(pedido2.cliente_id, 3, "O pão estava ótimo, mas o doce de leite demorou um pouco para chegar.", cliente2.nome)

    # --- 7. Respostas às Avaliações ---
    print("\n--- 7. Respondendo Avaliações ---")
    facade.responder_avaliacao_pedido(pedido1.cliente_id, "Ficamos muito felizes que gostou dos nossos produtos!", fornecedor1.nome, "fornecedor")
    facade.responder_avaliacao_pedido(pedido2.cliente_id, "Pedimos desculpas pelo atraso na entrega. Estamos aprimorando nosso serviço.", "Equipe de Entregas", "entrega")

    # --- 8. Gerenciar Tutoriais ---
    print("\n--- 8. Gerenciando Tutoriais ---")
    tutorial1 = facade.criar_tutorial("Como Conservar Queijos Artesanais", "Dicas para manter seu queijo fresco por mais tempo...", fornecedor1.nome)
    facade.adicionar_tag_a_tutorial(tutorial1.titulo, "Queijo")
    facade.adicionar_tag_a_tutorial(tutorial1.titulo, "Conservação")

    tutorial2 = facade.criar_tutorial("Receitas com Doce de Leite Colonial", "Ideias deliciosas para usar seu doce de leite...", fornecedor2.nome)
    facade.adicionar_tag_a_tutorial(tutorial2.titulo, "Receitas")
    facade.adicionar_tag_a_tutorial(tutorial2.titulo, "Doces")


    # --- 9. Listar Informações ---
    print("\n--- 9. Listando Informações ---")
    print("\nTodos os pedidos:")
    for p in facade.listar_todos_pedidos():
        print(p.gerar_detalhes_pedido())
        print("-" * 30)

    print("\nProdutos do Sítio do Vovô Chico:")
    for prod in facade.listar_produtos_do_fornecedor("Sítio do Vovô Chico"):
        print(f"- {prod.nome} (R${prod.preco:.2f})")

    print("\nProdutos do Cantinho da Roça:")
    for prod in facade.listar_produtos_do_fornecedor("Cantinho da Roça"):
        print(f"- {prod.nome} (R${prod.preco:.2f})")

if __name__ == "__main__":
    main()