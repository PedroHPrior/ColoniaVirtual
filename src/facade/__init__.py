# src/main.py

from src.facade.sistema_venda_facade import SistemaVendaFacade
from src.strategy.calcula_taxa_fixa import CalculaTaxaFixa
from src.strategy.calcula_taxa_express import CalculaTaxaExpress
from src.strategy.calcula_taxa_premium import CalculaTaxaPremium
from datetime import datetime, timedelta

def main():
    print("Iniciando o Sistema de Vendas...")
    facade = SistemaVendaFacade()

    # --- 1. Cadastrar Clientes e Fornecedores ---
    print("\n--- 1. Cadastrando Clientes e Fornecedores ---")
    cliente1 = facade.cadastrar_cliente("Ana Silva", "ana.silva@email.com", "11987654321", "Rua A, 123")
    cliente2 = facade.cadastrar_cliente("Bruno Costa", "bruno.costa@email.com", "21912345678", "Av. B, 456")

    fornecedor1 = facade.cadastrar_fornecedor("Eletronicos SA", "contato@eletronicos.com", "551130001000")
    fornecedor2 = facade.cadastrar_fornecedor("Móveis Express", "vendas@moveisexpress.com", "552140002000")

    # --- 2. Adicionar Produtos ---
    print("\n--- 2. Adicionando Produtos ---")
    produto1 = facade.adicionar_produto(fornecedor1.nome, "Smartphone X", 1500.00, "Celular de última geração", "Eletrônicos")
    produto2 = facade.adicionar_produto(fornecedor1.nome, "Smart TV 50", 2500.00, "TV 4K com Android TV", "Eletrônicos")
    produto3 = facade.adicionar_produto(fornecedor2.nome, "Cadeira Gamer", 800.00, "Cadeira ergonômica para jogos", "Móveis")

    # --- 3. Criar e Montar Pedidos ---
    print("\n--- 3. Criando e Montando Pedidos ---")
    pedido1 = facade.criar_pedido(cliente1.email)
    if pedido1:
        facade.adicionar_item_a_pedido(pedido1.cliente_id, "Smartphone X", 1)
        facade.adicionar_item_a_pedido(pedido1.cliente_id, "Smart TV 50", 1)

    pedido2 = facade.criar_pedido(cliente2.email)
    if pedido2:
        facade.adicionar_item_a_pedido(pedido2.cliente_id, "Cadeira Gamer", 2)
        facade.adicionar_item_a_pedido(pedido2.cliente_id, "Smartphone X", 1) # Bruno comprando um smartphone também

    # --- 4. Finalizar Pedidos com Diferentes Estratégias de Taxa ---
    print("\n--- 4. Finalizando Pedidos com Diferentes Estratégias de Taxa ---")

    # Pedido 1 com taxa fixa
    print(f"\nDetalhes do Pedido 1 antes da finalização: {pedido1.gerar_detalhes_pedido()}")
    taxa_fixa = CalculaTaxaFixa(20.00)
    finalizado_pedido1 = facade.finalizar_pedido(pedido1.cliente_id, "Cartão de Crédito", taxa_fixa)
    if finalizado_pedido1:
        print(f"Pedido 1 finalizado. Valor total com taxa: {finalizado_pedido1.valor_total:.2f}")

    # Pedido 2 com taxa express
    print(f"\nDetalhes do Pedido 2 antes da finalização: {pedido2.gerar_detalhes_pedido()}")
    taxa_express = CalculaTaxaExpress(0.03) # 3%
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

    # --- 6. Avaliar Pedidos ---
    print("\n--- 6. Avaliando Pedidos ---")
    facade.avaliar_pedido(pedido1.cliente_id, 5, "Produto excelente e entrega rápida!")
    facade.avaliar_pedido(pedido2.cliente_id, 2, "A cadeira chegou com atraso e um pequeno arranhão.")

    # --- 7. Respostas às Avaliações ---
    print("\n--- 7. Respondendo Avaliações ---")
    facade.responder_avaliacao_pedido(pedido1.cliente_id, "Agradecemos o feedback positivo!", "Gerente Eletronicos", "fornecedor")
    facade.responder_avaliacao_pedido(pedido2.cliente_id, "Lamentamos o ocorrido. Entraremos em contato para resolver.", "Suporte Móveis Express", "entrega")

    # --- 8. Gerenciar Tutoriais ---
    print("\n--- 8. Gerenciando Tutoriais ---")
    tutorial1 = facade.criar_tutorial("Guia de Configuração Smart TV", "Passos para configurar sua nova TV...", "Suporte Eletronicos")
    facade.adicionar_tag_a_tutorial(tutorial1.titulo, "Smart TV")
    facade.adicionar_tag_a_tutorial(tutorial1.titulo, "Configuração")

    # --- 9. Listar Informações ---
    print("\n--- 9. Listando Informações ---")
    print("\nTodos os pedidos:")
    for p in facade.listar_todos_pedidos():
        print(p.gerar_detalhes_pedido())
        print("-" * 30)

    print("\nProdutos do Fornecedor Eletronicos SA:")
    for prod in facade.listar_produtos_do_fornecedor("Eletronicos SA"):
        print(f"- {prod.nome} ({prod.preco:.2f})")

if __name__ == "__main__":
    main()