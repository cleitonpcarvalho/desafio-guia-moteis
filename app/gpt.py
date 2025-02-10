
import os
import openai
from dotenv import load_dotenv

# Carregar variáveis de ambiente

load_dotenv()

chave_api = os.getenv("OPENAI_API_KEY")
openai.api_key = chave_api

# Função inicial com configurações e prompt principal

def enviar_mensagem(prompt, lista_mensagens=[]):
    lista_mensagens.append(
            {"role": "system", "content": """Você é um vendedor altamente qualificado, com profundo conhecimento sobre as melhores técnicas
              de vendas do mercado. Devido ao seu reconhecimento e expertise, você se especializou no nicho de motéis, atuando agora como consultor 
              que ajuda empresas desse nicho a aprimorar suas estratégias de vendas por meio do treinamento de assistentes virtuais inteligentes. Seu papel 
              é analisar as interações entre os assistentes virtuais das empresas e seus clientes, identificando pontos fortes e fracos na condução do atendimento 
              por mensagens e, assim, apontando oportunidades de melhoria a serem implementadas.

               Dessa forma, quero que você avalie cuidadosamente a conversa a seguir entre a nossa assistente e um cliente e extraia, 
               com precisão, a seguinte informação:"""}
    )
    lista_mensagens.append(
        {"role": "user", "content": prompt}
    )
    resposta = openai.ChatCompletion.create(
        model="gpt-4o-mini", 
        messages=lista_mensagens 
    )
    return resposta['choices'][0]['message']      


# Função para obter a satisfação do cliente

def get_satisfaction(conversa):
    prompt = f"""Analise todo o texto da conversa abaixo e, com base no seu desenvolvimento, 
    atribua uma nota de 0 a 10 totalmente condizente com a conversa e que reflita de forma 
    realista o nível de satisfação na perspectiva do cliente. Lembre-se de que uma conversa 
    eficaz ocorre quando a assistente compreende claramente as necessidades do usuário, responde 
    de forma precisa e objetiva às suas perguntas, oferece informações relevantes e conduz a 
    interação de maneira fluida e natural. Além disso, para garantir uma experiência satisfatória, 
    a assistente deve ser capaz de esclarecer dúvidas, sugerir opções quando necessário e concluir 
    a reserva de forma eficiente, garantindo que todos os detalhes estejam corretos e confirmados.\n

    Observação: A análise deve retornar somente um número inteiro de 0 a 10, nada de texto, títulos, 
    listas, formatações ou qualquer outra coisa, somente um número inteiro de 0 a 10.\n
    
    A conversa para ser analisada é a seguinte:\n
    
    {conversa}

    """

    return enviar_mensagem(prompt)

# Função para obter o resumo da conversa

def get_summary(conversa):
    prompt = f"""
    
    Faça um breve resumo da conversa abaixo em um texto corrido de no máximo 750 caracteres, 
    contando com os espaços. O resumo deve ser direto ao ponto e fornecer um excelente panorama 
    geral sobre o começo, meio e fim da conversa, sem desperdícios com informações irrelevantes. 
    Assim, deve ter uma estrutura que permita uma leitura rápida e clara do que ocorreu no diálogo. \n

    Observação: Quero somente o RESUMO DA CONVERSA, nada de títulos, listas ou formatações. Quero 
    apenas o TEXTO DO RESUMO, e um detalhe importante: esse texto deve ter no máximo 750 caracteres, 
    incluindo os espaços, nada além disso!\n
    
    
    A conversa para ser analisada é a seguinte:\n
    
    {conversa}
    
    """
    return enviar_mensagem(prompt)

# Função para obter a melhoria sugerida para a conversa

def get_improvement(conversa):
    prompt = f"""
    
    Analise cuidadosamente o texto da conversa abaixo e me entregue um diagnóstico em um texto corrido
    sobre como essa conversa poderia ter sido melhor. Utilize seus melhores conhecimentos sobre técnicas
    de venda, em especial o conhecimento de vendas específico do nicho de motéis. Lembre-se de que uma boa
    conversa é aquela em que a assistente responde adequadamente às perguntas do usuário e finaliza a reserva. 
    Desse modo, me forneça um diagnóstico 100% profissional e baseado em técnicas de vendas avançadas.\n
    
    Observação: Quero somente o texto com a ANÁLISE DA CONVERSA, nada de títulos, listas, tópicos ou formatações. 
    Quero apenas o TEXTO DA ANÁLISE, e um detalhe importante: esse texto deve ter no máximo 750 caracteres, 
    incluindo os espaços, nada mais do que isso!\n

    A conversa para ser analisada é a seguinte:\n
    
    {conversa}
    
    """
    return enviar_mensagem(prompt)
 


