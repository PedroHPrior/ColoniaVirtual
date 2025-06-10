# src/main.py

from src.facade.sistema_venda_facade import SistemaVendaFacade
from src.strategy.calcula_taxa_fixa import CalculaTaxaFixa
from src.strategy.calcula_taxa_express import CalculaTaxaExpress
from src.strategy.calcula_taxa_premium import CalculaTaxaPremium
from datetime import datetime, timedelta

def exibir_menu():
    print("\n--- Sistema de Vendas de Produtos Coloniais ---")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Fornecedor")
    print("3. Adicionar Produto")
    print("4. Criar Pedido")
    print("5. Adicionar Item a Pedido")
    print("6. Finalizar Pedido")
    print("7. Agendar Entrega")
    print("8. Atualizar Status de Entrega")
    print("9. Avaliar Pedido")
    print("10. Responder Avaliação de Pedido")
    print("11. Criar Tutorial")
    print("12. Adicionar Tag a Tutorial")
    print("13. Listar Todos os Pedidos")
    print("14. Listar Produtos de Fornecedor")
    print("0. Sair")
    print("---------------------------------------------")

def main():
    facade = SistemaVendaFacade()

    # Dados iniciais para facilitar os testes (opcional, pode ser removido)
    cliente1 = facade.cadastrar_cliente("Ana Silva", "ana.silva@comprador.com", "11987654321", "Rua das Rosas, 123, Bairro Jardim, São Paulo")
    fornecedor1 = facade.cadastrar_fornecedor("Sítio do Vovô Chico", "contato@sitiodovovochico.com", "554933221100")
    facade.adicionar_produto(fornecedor1.nome, "Queijo Colonial Artesanal (500g)", 35.00, "Queijo curado de leite de vaca, feito artesanalmente.", "Laticínios")
    facade.adicionar_produto(fornecedor1.nome, "Salame Colonial (350g)", 28.50, "Salame defumado, com tempero caseiro.", "Embutidos")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("Telefone do cliente: ")
            endereco = input("Endereço do cliente: ")
            facade.cadastrar_cliente(nome, email, telefone, endereco)
        elif opcao == '2':
            nome = input("Nome do fornecedor: ")
            email = input("Email do fornecedor: ")
            telefone = input("Telefone do fornecedor: ")
            facade.cadastrar_fornecedor(nome, email, telefone)
        elif opcao == '3':
            fornecedor_nome = input("Nome do fornecedor: ")
            nome_produto = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            descricao = input("Descrição do produto (opcional): ")
            categoria = input("Categoria do produto (opcional): ")
            facade.adicionar_produto(fornecedor_nome, nome_produto, preco, descricao, categoria)
        elif opcao == '4':
            cliente_email = input("Email do cliente para o pedido: ")
            pedido = facade.criar_pedido(cliente_email)
            if pedido:
                print(f"Pedido com ID {pedido.cliente_id} criado para {cliente_email}.")
            else:
                print("Não foi possível criar o pedido.")
        elif opcao == '5':
            pedido_id = int(input("ID do pedido: "))
            produto_nome = input("Nome do produto a adicionar: ")
            quantidade = int(input("Quantidade: "))
            facade.adicionar_item_a_pedido(pedido_id, produto_nome, quantidade)
        elif opcao == '6':
            pedido_id = int(input("ID do pedido a finalizar: "))
            metodo_pagamento = input("Método de pagamento (Cartão de Crédito, Pix, Boleto): ")
            print("Escolha a estratégia de taxa:")
            print("1. Taxa Fixa")
            print("2. Taxa Express (porcentagem)")
            print("3. Taxa Premium (fixa + adicional)")
            escolha_taxa = input("Opção de taxa: ")

            metodo_taxa = None
            if escolha_taxa == '1':
                valor_fixo = float(input("Valor da taxa fixa: "))
                metodo_taxa = CalculaTaxaFixa(valor_fixo)
            elif escolha_taxa == '2':
                percentual = float(input("Percentual da taxa express (ex: 0.05 para 5%): "))
                metodo_taxa = CalculaTaxaExpress(percentual)
            elif escolha_taxa == '3':
                taxa_minima = float(input("Taxa mínima Premium: "))
                valor_por_cem = float(input("Valor adicional por cada R$100 de compra: "))
                metodo_taxa = CalculaTaxaPremium(taxa_minima, valor_por_cem)
            else:
                print("Opção de taxa inválida. Nenhuma taxa será aplicada.")

            finalizado = facade.finalizar_pedido(pedido_id, metodo_pagamento, metodo_taxa)
            if finalizado:
                print(f"Pedido {pedido_id} finalizado.")
            else:
                print(f"Não foi possível finalizar o pedido {pedido_id}.")

        elif opcao == '7':
            pedido_id = int(input("ID do pedido para agendar entrega: "))
            endereco = input("Endereço de entrega: ")
            dias_para_entrega = int(input("Dias para a entrega (ex: 2 para daqui a 2 dias): "))
            data_prevista = datetime.now() + timedelta(days=dias_para_entrega)
            facade.agendar_entrega(pedido_id, endereco, data_prevista)
        elif opcao == '8':
            entrega_id = int(input("ID da entrega para atualizar: "))
            novo_status = input("Novo status (Pendente, Em Trânsito, Entregue, Cancelado): ")
            facade.atualizar_status_entrega(entrega_id, novo_status)
        elif opcao == '9':
            pedido_id = int(input("ID do pedido a avaliar: "))
            nota = int(input("Nota (1-5): "))
            comentario_texto = input("Comentário: ")
            autor = input("Seu nome (autor da avaliação): ")
            facade.avaliar_pedido(pedido_id, nota, comentario_texto, autor)
        elif opcao == '10':
            pedido_id = int(input("ID do pedido da avaliação a responder: "))
            texto_resposta = input("Texto da resposta: ")
            autor_resposta = input("Autor da resposta: ")
            tipo_resposta = input("Tipo de resposta (fornecedor ou entrega): ")
            facade.responder_avaliacao_pedido(pedido_id, texto_resposta, autor_resposta, tipo_resposta)
        elif opcao == '11':
            titulo = input("Título do tutorial: ")
            conteudo = input("Conteúdo do tutorial: ")
            autor = input("Autor do tutorial: ")
            facade.criar_tutorial(titulo, conteudo, autor)
        elif opcao == '12':
            titulo_tutorial = input("Título do tutorial para adicionar tag: ")
            tag = input("Tag a adicionar: ")
            facade.adicionar_tag_a_tutorial(titulo_tutorial, tag)
        elif opcao == '13':
            pedidos = facade.listar_todos_pedidos()
            if pedidos:
                print("\n--- Todos os Pedidos ---")
                for p in pedidos:
                    print(p.gerar_detalhes_pedido())
                    print("-" * 30)
            else:
                print("Nenhum pedido cadastrado.")
        elif opcao == '14':
            fornecedor_nome = input("Nome do fornecedor para listar produtos: ")
            produtos = facade.listar_produtos_do_fornecedor(fornecedor_nome)
            if produtos:
                print(f"\n--- Produtos do {fornecedor_nome} ---")
                for prod in produtos:
                    print(f"- {prod.nome} (R${prod.preco:.2f})")
            else:
                print(f"Nenhum produto encontrado para o fornecedor '{fornecedor_nome}' ou fornecedor não existe.")
        elif opcao == '0':
            print("Saindo do sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()