# importando scripts de manipulação do Banco de Dados e do ChatGPT

from app.db import *
from app.gpt import *

# Retornando os ids das sessões

ids = obter_ids_session()

# Iterando sobre o conteúdo da mensagem e passando o id da sessão como parâmetro

for j in ids:
    texto = show_content(j['id'])
    mensagens = ""

    # Verificando se a mensagem foi enviada pelo Bot ou pelo cliente

    for i in texto:
        if i["message_remote"] == True:
            mensagens += f"Cliente: {i['message_content']}\n"  
        else:
            mensagens += f"Chatbot: {i['message_content']}\n"
    
    # Salvando o id da sessão na variável id_s para uso posterior

    id_s = j['id']

    # Retornando o resultado gerado pelo ChatGPT e armazenando nas seguintes variáveis

    sat = get_satisfaction(mensagens)
    sum = get_summary(mensagens)
    imp = get_improvement(mensagens)
    data_criacao = j['created_at']

    # Formatando o tipo do dado retornado antes de serem inseridos no Banco de Dados

    id_session = id_s
    satisfaction = int(sat['content'])
    summary = str(sum['content'])
    improvement = str(imp['content'])

    # Chamando a função e passando os dados para serem gravados no Banco de Dados

    inserir_analysis(id_session,satisfaction,summary,improvement)

    # Imprimindo no console os dados de análise retornados pelo ChatGPT para fins de teste

    print("----------------------------------------------------------")
    print(f"Análise da conversa com id da Sessão - {id_session}:\n")
    print(f"Satisfaction: {satisfaction}\n")
    print(f"Summary:  {summary}\n")
    print(f"Improvement: {improvement}\n")

    # Imprime a data de criação da sessão para fins de teste

    print(f"Data de criação: {data_criacao}\n")





   






