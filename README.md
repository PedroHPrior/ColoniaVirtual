# 🛠️ Backend – Conexão Colono-Comprador

Este repositório contém o **backend** da aplicação **Conexão Colono-Comprador**, que conecta colonos (produtores rurais de produtos coloniais) diretamente com compradores interessados. O sistema gerencia dados de usuários, produtos, pedidos, entregas, avaliações, fornecedores e tutoriais, utilizando os padrões de projeto **Facade** e **Strategy** para garantir uma arquitetura modular e extensível.

---

## 🚀 Funcionalidades Principais

- **Gerenciamento de Usuários**  
  Cadastro e atualização de perfis de **Clientes** e **Fornecedores (Colonos)**.

- **Catálogo de Produtos**  
  Adição, edição e listagem de produtos coloniais oferecidos pelos fornecedores.

- **Sistema de Pedidos**  
  Criação de pedidos, adição de itens, seleção de método de pagamento e cálculo dinâmico de taxas de entrega.

- **Gestão de Entregas**  
  Agendamento, atualização de status e rastreamento de entregas.

- **Sistema de Avaliações e Comentários**  
  Compradores podem avaliar pedidos, fornecedores e entregas. Respostas também são suportadas.

- **Base de Conhecimento**  
  Criação e gerenciamento de tutoriais como:  
  _“Como embalar produtos”_, _“Dicas de vendas”_, entre outros.

- **Padrões de Projeto Utilizados**
  - **Facade**: `SistemaVendaFacade` – Interface simplificada para orquestração das operações de vendas.
  - **Strategy**: Estratégias flexíveis para o cálculo de taxas de entrega:
    - `CalculaTaxaFixa`
    - `CalculaTaxaExpress`
    - `CalculaTaxaPremium`

---

## ⚙️ Estrutura do Projeto

```
projeto_engenharia/
├── src/
│   ├── models/         # Entidades de negócio (Cliente, Produto, Pedido etc.)
│   ├── strategy/       # Estratégias para cálculo de taxa
│   ├── facade/         # Interface unificada para o sistema de vendas
│   ├── utils/          # Funções auxiliares
│   └── main.py         # Exemplo de uso do sistema
├── tests/              # Testes unitários (a serem implementados)
├── .env                # Variáveis de ambiente
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```



---

## 🧪 Tecnologias Utilizadas

- **Python 3.x https://www.python.org/downloads/** 
- **Módulos padrão do Python**: `datetime`, `abc`, `typing`, entre outros

---

## 🖥️ Como Executar o Projeto Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/PedroHPrior/projeto_engenharia.git
cd projeto_engenharia
```
### 2. Instalar as Dependências
```bash
pip install -r requirements.txt
```
Mesmo que o requirements.txt esteja vazio, este passo é importante para futuras dependências.

## ▶️ Executando o Projeto

Lembrando que existem duas branches, na branch main estão mockados os valores, e ao rodar o comando abaixo é possível ver onde estão implementados os padrões facade e strategy. Já na branch homolog é possível encontrar a interface interativa do sistema.

```bash
python -m src.main
```
Esse comando executa o exemplo de uso contido em main.py, demonstrando o funcionamento dos modelos, estratégias e fachada.

## ✅ Testes

Ainda não implementado
Quando disponíveis, execute os testes com:
```bash
# Instale o pytest, se necessário
pip install pytest

# Execute os testes
pytest tests/
```
## ✉️ Contato

Autor: Pedro Henrique Prior Kraemer

GitHub: https://github.com/PedroHPrior

LinkedIn: https://www.linkedin.com/in/pedro-henrique-prior-kraemer/ 



