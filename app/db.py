import psycopg2
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

# Carregar variáveis do .env

load_dotenv()

# Obter a URL de conexão do banco

DATABASE_URL = os.getenv("DATABASE_URL")

# Função para conectar ao banco

def conectar():
    try:
        # Parse da URL de conexão
        
        result = urlparse(DATABASE_URL)
        conn = psycopg2.connect(
            dbname=result.path[1:],  
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port
        )
        return conn
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return None

# Função para retornar o conteudo da mensagem e o campo remote de acordo com o id da sessão

def show_content(session_id):
    conn = conectar()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT 
                m.id AS message_id,
                m.content AS message_content,
                m.created_at AS message_created_at,
                m.remote AS message_remote,  -- Adicionando o campo remote
                s.id AS session_id
            FROM 
                message m
            JOIN 
                session s ON m.session_id = s.id
            WHERE 
                s.id = %s;
        """, (session_id,)) 
        dados = cur.fetchall()
        cur.close()
        conn.close()
        
        # Retorna o conteúdo da mensagem e o campo remote
        return [{"message_content": linha[1], "message_remote": linha[3]} for linha in dados]

# Função para retornar dados da tabela session

def obter_ids_session():
    conn = conectar()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT id, created_at FROM session;")  # Busca id e created_at
        resultados = [{"id": linha[0], "created_at": linha[1]} for linha in cur.fetchall()]
        cur.close()
        conn.close()
        return resultados  # Retorna uma lista de dicionários contendo id e created_at
    else:
        print("Não foi possível conectar ao banco de dados.")
        return []  # Retorna uma lista vazia em caso de falha



# Função para inserir dados na tabela analysis

def inserir_analysis(session_id, satisfaction, summary, improvement):
    conn = conectar()
    if conn:
        try:
            cur = conn.cursor()
            # Inserir dados na tabela analysis
            cur.execute("""
                INSERT INTO analysis (session_id, satisfaction, summary, improvement, created_at)
                VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP);
            """, (session_id, satisfaction, summary, improvement))
            conn.commit()  # Confirma a transação
            print("Dados inseridos com sucesso na tabela analysis.")
            cur.close()
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

