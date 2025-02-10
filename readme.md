# Documentação da Aplicação de Análise de Conversas com OpenAI

## Introdução

Esta aplicação foi desenvolvida por **Cleiton Carvalho**, Engenheiro de Software, como parte de um desafio técnico para uma vaga de **Engenheiro(a) de Inteligência Conversacional e Assistentes Virtuais**. O objetivo da aplicação é analisar conversas de atendimento ao cliente e extrair informações úteis para melhorar a qualidade do serviço e o desempenho da assistente virtual.

A aplicação usa a API oficial do OpenAI para analisar as conversas, processando-as com o modelo `gpt-4o-mini`. Os resultados da análise são gravados em um banco de dados PostgreSQL, com informações sobre a satisfação do cliente, resumo da conversa e sugestões de melhorias.

---

## Objetivo do Desafio

A aplicação tem como objetivo analisar conversas entre clientes e assistentes virtuais, extraindo as seguintes informações:

- **Satisfaction**: Nota de satisfação do cliente (de 0 a 10)
- **Summary**: Resumo da conversa
- **Improvement**: Como a conversa poderia ter sido melhor

Essas informações são extraídas utilizando a API do OpenAI e gravadas em um banco de dados PostgreSQL.

---

## Estrutura do Projeto

A aplicação está estruturada da seguinte forma:

```
/ (Raiz do projeto)
│
├── app/
│   ├── db.py                # Manipulação do banco de dados
│   ├── gpt.py               # Integração com a API OpenAI
│
├── Dockerfile               # Configuração do Docker para a aplicação
├── docker-compose.yml       # Configuração do Docker Compose
├── main.py                  # Código principal da aplicação
├── requirements.txt         # Dependências do projeto
└── .env                     # Arquivo de variáveis de ambiente
```

---

## Componentes Principais

### 1. **Banco de Dados** (`db.py`)

A comunicação com o banco de dados é realizada através do arquivo `db.py`. Ele contém funções para:

- **Conectar ao banco de dados** (`conectar`)
- **Obter sessões de conversas** (`obter_ids_session`)
- **Mostrar conteúdo da conversa** (`show_content`)
- **Inserir análise de conversas** (`inserir_analysis`)

A conexão é feita com o PostgreSQL, e os dados são extraídos e gravados conforme o fluxo de execução da aplicação.

### 2. **Integração com o OpenAI** (`gpt.py`)

O arquivo `gpt.py` contém funções para interagir com a API do OpenAI:

- **Enviar mensagens para o ChatGPT**: Função `enviar_mensagem` envia uma conversa ou prompt para a API do OpenAI.
- **Funções de análise**:
  - `get_satisfaction`: Obtém a satisfação do cliente com base na conversa.
  - `get_summary`: Retorna um resumo da conversa.
  - `get_improvement`: Sugere melhorias para a conversa.

Essas funções usam a API do OpenAI para processar as mensagens e obter as análises de satisfação, resumo e sugestões de melhorias.

### 3. **Arquivo Principal** (`main.py`)

O arquivo `main.py` é o coração da aplicação. Ele:

- Obtém os IDs das sessões de conversas
- Itera sobre as mensagens e as organiza, diferenciando se foram enviadas pelo cliente ou pelo assistente
- Chama as funções do OpenAI para obter a análise da conversa
- Insere os resultados da análise no banco de dados PostgreSQL
- Exibe os resultados da análise no console

### 4. **Docker e Docker Compose**

#### Dockerfile

O **Dockerfile** configura o ambiente da aplicação, usando a imagem `python:3.10-slim` para instalar as dependências necessárias e executar o script `main.py`.

```dockerfile
FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
```

#### docker-compose.yml

O arquivo `docker-compose.yml` define dois serviços:

- **db**: Serviço de banco de dados PostgreSQL
- **python_app**: Serviço da aplicação Python, que depende do serviço de banco de dados

```yaml
version: '3.8'

services:

  db:
    container_name: teste_guia_db
    image: postgres
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_DB: ${POSTGRES_DB}
    ports:
      - 5432:5432
    volumes:
      - postgres:/var/lib/postgresql/data
      - ./prisma/sql/:/docker-entrypoint-initdb.d/

  python_app:
    container_name: python_app
    build: .
    depends_on:
      - db
    environment:
      DATABASE_URL: "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}"
    volumes:
      - .:/usr/src/app
    ports:
      - "5000:5000"
    command: ["python", "main.py"]

volumes:
  postgres:
```

---

## Como Executar a Aplicação

### 1. **Configuração do Ambiente**

Clone o repositório e configure o arquivo `.env` com as variáveis necessárias:

```dotenv
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
OPENAI_API_KEY=your_openai_api_key
```

### 2. **Build e Execução com Docker Compose**

Para rodar a aplicação, execute os seguintes comandos no diretório raiz do projeto:

```bash
docker-compose up --build
```

Este comando irá construir e iniciar os contêineres definidos no `docker-compose.yml`.

### 3. **Verificação e Testes**

A aplicação irá automaticamente:

1. Analisar as conversas no banco de dados
2. Extrair as informações de satisfação, resumo e sugestões de melhorias
3. Inserir os resultados na tabela `analysis`
4. Imprimir os resultados no console para fins de teste

---

## Considerações Finais

Esta aplicação serve como uma base para análise de conversas e pode ser expandida para incluir mais funcionalidades, como:

- **Envio de mensagens para o WhatsApp** (Integração com a API Oficial)
- **Melhorias na análise do comportamento do cliente**
- **Análises adicionais de dados coletados**

A implementação utiliza **Docker** para garantir que a aplicação seja fácil de configurar e executar em qualquer ambiente.

Se você tiver dúvidas ou sugestões, fique à vontade para entrar em contato!

---

**Cleiton Carvalho**  
Engenheiro de Software  
[LinkedIn](https://www.linkedin.com/in/cleitonpcarvalho/)
