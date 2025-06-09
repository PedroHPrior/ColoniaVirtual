🛠️ Backend – Conexão Colono-Comprador
Este repositório contém o backend da aplicação Conexão Colono-Comprador, que tem como objetivo conectar colonos (produtores rurais de produtos coloniais) diretamente com compradores interessados. O sistema gerencia dados de usuários, produtos, pedidos, entregas, avaliações, fornecedores e tutoriais, utilizando padrões de projeto como Facade e Strategy para garantir uma arquitetura modular e extensível.

🚀 Funcionalidades Principais
Gerenciamento de Usuários
Cadastro e atualização de perfis de Clientes e Fornecedores (Colonos).

Catálogo de Produtos
Adição, edição e listagem de produtos coloniais oferecidos pelos fornecedores.

Sistema de Pedidos
Criação de pedidos, adição de itens, seleção de método de pagamento e cálculo dinâmico de taxas de entrega.

Gestão de Entregas
Agendamento, atualização de status e rastreamento de entregas.

Sistema de Avaliações e Comentários
Compradores podem avaliar pedidos, fornecedores e entregas. Respostas também são suportadas.

Base de Conhecimento
Criação e gerenciamento de tutoriais, como:
“Como embalar produtos”, “Dicas de vendas”, entre outros.

Padrões de Projeto Utilizados

Facade – SistemaVendaFacade: Interface simplificada para orquestração de operações de vendas.

Strategy – Estratégias flexíveis para o cálculo de taxas de entrega:

CalculaTaxaFixa

CalculaTaxaExpress

CalculaTaxaPremium

⚙️ Estrutura do Projeto
seu_projeto_backend/
├── src/
│   ├── models/         # Entidades de negócio (Cliente, Produto, Pedido etc.)
│   ├── strategy/       # Estratégias de cálculo de taxa
│   ├── facade/         # Facade para simplificação das operações
│   ├── services/       # (Opcional) Lógica de negócio complexa
│   ├── utils/          # Funções auxiliares
│   └── main.py         # Ponto de entrada do projeto
├── tests/              # Testes unitários (a serem implementados)
├── .env                # Variáveis de ambiente
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
🧪 Tecnologias Utilizadas
Python 3.x

Módulos padrão do Python: datetime, abc, typing, entre outros.

🖥️ Como Executar o Projeto Localmente
1. Clonar o Repositório
git clone <https://github.com/PedroHPrior/projeto_engenharia.git>
cd projeto_engenharia

2. Criar e Ativar um Ambiente Virtual
python -m venv venv
Ativando o ambiente virtual:

Windows:

.\venv\Scripts\activate
macOS/Linux:

source venv/bin/activate
3. Instalar as Dependências
bash
Copiar
Editar
pip install -r requirements.txt
O arquivo requirements.txt pode estar vazio neste momento, mas esse passo é importante para futuras bibliotecas.

▶️ Executando o Projeto
Com o ambiente virtual ativado:

python src/main.py
Esse comando executa o exemplo de uso contido no main.py, demonstrando o funcionamento dos modelos, estratégias e fachada.

✅ Testes
Ainda não implementado

Quando disponíveis, execute os testes com:

# Instale o pytest, se necessário
pip install pytest

# Rode os testes
pytest tests/
🤝 Contribuindo
Contribuições são muito bem-vindas!

Faça um fork deste repositório

Crie uma branch: git checkout -b feature/nova-funcionalidade

Faça suas alterações e commite: git commit -m "feat: adiciona nova funcionalidade X"

Faça push para a branch: git push origin feature/nova-funcionalidade

Abra um Pull Request


✉️ Contato
Para dúvidas, sugestões ou contribuições, entre em contato:

Nome: [Pedro Henrique Prior Kraemer]

Email: [pedrohpk17@gmail.com]

GitHub: [https://github.com/PedroHPrior]

LinkedIn: [https://www.linkedin.com/in/pedro-henrique-prior-kraemer/]
