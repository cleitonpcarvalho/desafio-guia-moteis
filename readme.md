```markdown
# Desafio de Análise de Conversas com OpenAI

Este projeto foi desenvolvido como parte de um desafio técnico para a vaga de Engenheiro(a) de Inteligência Conversacional e Assistentes Virtuais. A aplicação tem como objetivo analisar conversas de atendimento utilizando a API da OpenAI (GPT-4) e armazenar os resultados em um banco de dados PostgreSQL.

## Descrição do Projeto

A aplicação realiza a análise de conversas de atendimento, extraindo três principais informações:

1. **Satisfação do cliente**: Uma nota de 0 a 10 que reflete o nível de satisfação do cliente com o atendimento.
2. **Resumo da conversa**: Um breve resumo da conversa, destacando os pontos principais.
3. **Melhorias sugeridas**: Sugestões de como a conversa poderia ter sido melhorada.

A aplicação utiliza a API da OpenAI para processar as mensagens e armazenar os resultados em um banco de dados PostgreSQL.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
.
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── README.md
└── app
    ├── db.py
    └── gpt.py
```

### Arquivos Principais

- **Dockerfile**: Contém as instruções para construir a imagem Docker da aplicação.
- **docker-compose.yml**: Define os serviços da aplicação e do banco de dados PostgreSQL.
- **main.py**: O ponto de entrada da aplicação, responsável por orquestrar a análise das conversas.
- **requirements.txt**: Lista as dependências do projeto.
- **app/db.py**: Contém as funções para interagir com o banco de dados PostgreSQL.
- **app/gpt.py**: Contém as funções para interagir com a API da OpenAI.

## Configuração do Ambiente

### Pré-requisitos

- Docker
- Docker Compose
- Chave da API da OpenAI

### Passos para Configuração

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Configure as variáveis de ambiente**:

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

   ```plaintext
   POSTGRES_USER=seu_usuario
   POSTGRES_PASSWORD=sua_senha
   POSTGRES_DB=seu_banco_de_dados
   DATABASE_URL=postgresql://seu_usuario:sua_senha@db:5432/seu_banco_de_dados
   OPENAI_API_KEY=sua_chave_da_api_openai
   ```

3. **Construa e execute os contêineres**:

   ```bash
   docker-compose up --build
   ```

   Isso irá construir e iniciar os contêineres da aplicação e do banco de dados.

## Funcionamento da Aplicação

A aplicação funciona da seguinte forma:

1. **Obtenção das Conversas**: A aplicação obtém as conversas do banco de dados, identificando as mensagens enviadas pelo cliente e pelo chatbot.
2. **Análise das Conversas**: As conversas são enviadas para a API da OpenAI, que retorna a nota de satisfação, o resumo da conversa e as sugestões de melhoria.
3. **Armazenamento dos Resultados**: Os resultados da análise são armazenados no banco de dados na tabela `analysis`.

### Exemplo de Uso

Ao executar a aplicação, ela irá automaticamente analisar as conversas disponíveis no banco de dados e armazenar os resultados. Os dados de análise serão exibidos no console para fins de teste.

```plaintext
----------------------------------------------------------
Análise da conversa com id da Sessão - 1:

Satisfaction: 8

Summary: O cliente perguntou sobre disponibilidade de quartos e a assistente respondeu de forma clara e objetiva, concluindo a reserva com sucesso.

Improvement: A assistente poderia ter sugerido opções adicionais, como upgrades de quarto ou serviços extras, para aumentar a satisfação do cliente.

Data de criação: 2023-10-01 12:34:56
```

## Avaliação

Os principais pontos avaliados neste desafio são:

- **Elaboração do Prompt**: A qualidade e precisão dos prompts utilizados para extrair as informações desejadas.
- **Solução de Extração de Dados**: A eficácia da solução para processar as conversas e armazenar os resultados.
- **Execução da Aplicação**: A capacidade da aplicação de ser iniciada e funcionar corretamente ao executar o comando `docker-compose up --build`.

## Considerações Finais

Este projeto demonstra a capacidade de integrar tecnologias avançadas de processamento de linguagem natural (NLP) com bancos de dados e contêineres Docker, criando uma solução robusta e escalável para análise de conversas de atendimento.

Para qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato.

```
