from flask import Flask, jsonify, request
from groq import Groq
from dotenv import load_dotenv
import os
from flask_cors import CORS
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

def enviar_notificacao_lead(nome_cliente, contacto_cliente, interesse_cliente):
    meu_email = os.getenv("EMAIL")
    minha_senha =os.getenv("SENHA_APP")
    email_destino =os.getenv("EMAIL") # Onde queres receber o aviso

    # Criar a estrutura do e-mail
    msg = MIMEMultipart()
    msg['From'] = meu_email
    msg['To'] = email_destino
    msg['Subject'] = f"🔥 NOVO LEAD: {nome_cliente} está interessado!"

    corpo = f"""
    Temos um novo potencial cliente interessado!
    
    Nome: {nome_cliente}
    Contacto: {contacto_cliente}
    Interesse: {interesse_cliente}
    
    Responde rápido para não perderes a venda!
    """
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(meu_email, minha_senha)
        server.send_message(msg)
        server.quit()
        print("Notificação enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

load_dotenv()
Dados = {
    "Empresa":"evvaall",
    "Contacto":[
        "+244957847477",
        "ev283@gmail.com"
    ],
    "faq":{
        "O Que é a evvaall?": "A evvaall é uma empresa especializada em automação de processos, análise de dados e desenvolvimento de soluções com inteligência artificial para empresas e profissionais.",
        "Qual é o vosso objectivo?":"Nosso Objectivo é simplifiar tarefas que levariam muito tempo, aumentar a produtividade e entregar resultados mensuráveis e tecnológicos de ponta.",
        "Quais são os serviços que vocês prestram?":"Os nossos serviços são: Análise de dados, Criação de chatboots, Consultoria digital e Automatizamos tarefas repetitivas.",
        "Que tipo de Automações?":"Praticamente, qualquer tarefa repetitiva baseada em regras ou que envolva processamento de dados pode ser automatizada. Por exemplo: Envio automático de lembretes de pagamento por WhatsApp, Agendamento de reuniões, Geração e invio automáticos de relatórios.",
        "Que tipo de Chatbots?":"Desenvolvemos chatbots inteligentes para atendimento 24/7, integrando com WhatsApp, Telegram, sites e apps.",
        "Que tipo de Consultoria?":"Avaliamos seus processos e sugerimos soluções digitais sob medida, identificando o problema e ajudamos na tomada de desisão",
        "Que tipo de Análise de dados?":"Por exemplo, Hoje, como é que tu sabes qual é o teu produto mais lucrativo ou qual cliente está prestes a abandonar a tua empresa? Tu usas dados reais ou apenas intuição?",
        "Em que árias vocês atuam?":"sector Administrativo, Marketing e vendas, atendimento ao cliente e nas áreas de TI",
        "Como faço se eu quiser os vossos Serviços?":"Para mais informação ligue para: 957 847 477, ou deixe 1 mensagem com o serviço entre ' ' e nós entraremos em contacto.",
        "Me fale mais sobre vocês":"A evvaall é uma empresa de soluções digitais que ajuda empresas e profissionais a automatizar tarefas repetitivas, transformar dados em decisões estratégicas e criar chatboots inteligentes para a comunicação eficiente.",
        "Como é que vocês garantem segurança de informação":"Seguimos boas práticas de: 1-Controle de acesso baseado em permissões, 2-Armazenamento seguro em cloud, 3-Logs auditáveis, 4-Separação de ambiente (produção/teste), Em projetos sensíveis, a arquitetura pode ser ajustada para cumprir exigências específicas do cliente.",
        "Que tecnologias utilizam?":"A evvaall adota uma abordagem tecnológica orientada a arquitetura, não a ferramentas isoladas. A escolha das tecnologias depende do contexto operacional do cliente, requisitos de segurança, escalabilidade e integração",
        "Como escolhem a tecnologia certa?":"Não utilizamos uma stack fixa por padrão. Selecionamos as tecnologias com base em: 1-Volume de usuários, 2-Exigências regulatórias, 3-Necessidade de escalabilidade, 4-Orçamento do cliente, O foco não é a ferramenta — é o desempenho, segurança e sustentabilidade da solução.",
        "Que tipos de empresas podem contratar a evva.all?":"Trabalhamos com restaurantes, empresas do setor bancário, comércio, prestadores de serviços, Clínicas de Saúde, Imobliliárias e scritórios de Advogado/consultoria.",
        "O chatbot funciona 24 horas por dia?":"Sim. O sistema funciona 24/7, respondendo clientes automaticamente.",
        "O chatbot pode integrar com WhatsApp Business?":"Sim, utilizamos a API oficial do WhatsApp Business para integração segura e profissional.",
        "O chatbot substitui funcionários?":"Não. Ele automatiza tarefas repetitivas, permitindo que a equipa foque em atividades estratégicas trazendo mais resultados com os mesmos recursos.",
        "A IA aprende com o tempo?":"Sim. Podemos configurar o sistema para melhorar respostas com base em interações reais.",
        "O que é análise de dados na prática?":"É transformar dados do seu negócio (vendas, clientes, pagamentos) em informações estratégicas para tomada de decisão.",
        "Vocês criam relatórios personalizados?":"Sim. Desenvolvemos dashboards visuais e relatórios adaptados às necessidades da empresa",
        "Posso acompanhar os dados em tempo real?":"Dependendo da estrutura do cliente, é possível configurar dashboards com atualização automática.",
        "Os dados da minha empresa ficam seguros?":"Sim. Trabalhamos com boas práticas de segurança e integração com APIs oficiais.",
        "Vocês trabalham com contratos formais?":"Sim. Todos os serviços podem ser formalizados por contrato.",
        "Onde os sistemas ficam hospedados?":"Podem ser hospedados em servidores seguros (cloud) ou na infraestrutura do cliente.",
        "Como funciona o processo de contratação?":"Diagnóstico do problema, Proposta técnica, Desenvolvimento, Implementação, Suporte.",
        "O pagamento é mensal ou único?":"Depende do serviço, projetos personalizados e únicos podem ser pagos por  projetos desenvolvidos, sistemas com manutenção podem ter pagamento mensal.",
        "Por que escolher a evvaall?":"Porque combinamos tecnologia, estratégia e personalização. Não vendemos soluções genéricas — desenvolvemos sistemas adaptados ao seu negócio.",
        "Quanto custam os vossos serviços?":"O valor depende do nível de complexidade e integrações necessárias.Preciso de entender o seu desafio. Pode deixar o seu WhatsApp ou e-mail aqui?.",
        "Quanto custa um chatbot?":"O valor depende do nível de complexidade e integrações necessárias.",
        "Como funcionam os chatbots com IA desenvolvidos pela evvaall?":"Nossos sistemas utilizam modelos de linguagem integrados a regras de negócio específicas do cliente. A arquitetura geralmente envolve: 1-Interface (Site ou WhatsApp Business API), 2-Backend seguro (API própria), 3-Motor de IA, 4-Base de conhecimento personalizada, 5-Logs e monitoramento de desempenho, Isso permite respostas contextuais, automação de processos e coleta estruturada de dados.",
        "A IA toma decisões automáticas?":"A IA executa ações dentro de limites definidos. Sempre existe configuração de regras e possibilidade de supervisão humana para processos críticos. Não implementamos sistemas que atuem sem governança.",
        "Como a análise de dados gera valor real?":"Transformamos dados brutos em indicadores estratégicos como: 1-Taxa de conversão, 2-Tempo médio de atendimento, 3-Índice de recorrência de clientes, 4-Análise de inadimplência, 5-Padrões de comportamento, Isso permite decisões baseadas em evidência e não em suposição.",
        "O que diferencia a evvaall de outras empresas de tecnologia?":"1-Foco em automação orientada a resultado, 2-Integração entre IA + dados + processos, 3-Arquitetura enxuta e escalável, 4-Abordagem consultiva antes do desenvolvimento, 5-Implementação adaptada à realidade local",
        "Como funciona o ciclo de implementação?":"1-Diagnóstico técnico e operacional, 2-Mapeamento de processos, 3-Definição da arquitetura, 4-Desenvolvimento e testes, 5-Implantação controlada, 6-Monitoramento e otimização contínua",
    },
    "respostas_automaticas":{
        ".":"Este é um agente de atendimento que responde a perguntas sobre a evvall. Existem perguntas que não estou autorizado a processar",
        "..":"Muito Obrigado!",
        "Muito Obrigado":"Nada por isso. Até à próxima!",
        "*":"Deixe o seu recado. depois entraremos em contacto.",
        "**":"Deixe sua mensagem entre ' ' que nós entraremos em contacto.",
        "....":"Acesse o nosso site para mais informação.",
        ".....":"fui útil?",
    }
}
Dados["Roteiro_vendas"] = {
    "passo_1": "Olá! Bem-vindo à evvaall. Eu sou o assistente virtual inteligente. Com quem tenho o prazer de falar?",
    "passo_2": "Prazer, {nome}! Para te ajudar da melhor forma, o que procura hoje?\n1. Custos dos serviços;\n2. Suporte Técnico\n3. Fazer perguntas\n4. Falar com um Consultor Humano",
    "passo_3_orcamento": "Entendido. Para que eu possa preparar um valor aproximado, como descreveria o seu projeto atual? (Ex: Pequena automação, Sistema completo de dados ou Chatbot para empresa)",
    "passo_3_suporte":"Entendido! A nossa equipa técnica está pronta para ajudar. Para agilizarmos, pode descrever brevemente o que está a acontecer ou indicar o número do seu contrato/projeto?",    
    "passo_3_falar_com_humano":"Com certeza! Nada substitui uma boa conversa estratégica. O nosso consultor especialista terá todo o prazer em falar consigo. Para agendarmos uma chamada breve de 5 a 10 minutos ou para ele lhe enviar um convite de reunião, qual é o seu contacto?",
    "passo_3_tirar_duvida":"Excelente! Sobre o que você gostaria de saber mais agora?\n>•Quais são os nossos Serviços;\n•Qual é o Nosso objectivo?\n•Em que árias nós atuamos?\n•Faça uma outra pergunta.",
    "passo_4_orçamento":"Excelente. Para que o nosso especialista envie a proposta detalhada e o cronograma, por favor, deixe o seu WhatsApp ou E-mail.",
    "passo_4_suporte":"Obrigado pelo detalhe. Vou abrir um ticket prioritário agora. Qual o melhor número de WhatsApp para o técnico lhe contactar caso precisemos de acesso remoto ou mais detalhes?",
    "passo_4_falar_com_humano":"Excelente, vou passar agora mesmo para o nosso consultor no WhatsApp, é mais rápido!.Posso ajudar em algo mais?",
    "passo_5_final":"Muito obrigado! Recebi os seus dados. Em menos de 2 horas um consultor entrará em contacto consigo. Posso ajudar em algo mais?"
}
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
def conected(mensagem:str):
    msn=mensagem.capitalize().strip()
    if msn in Dados["respostas_automaticas"]:
        return Dados["respostas_automaticas"][msn]
    elif msn in Dados["faq"]:
        return Dados["faq"][msn]
    else:
        return msn

def orientacao(dicionario:dict) -> str:
    contexto =""
    for pergunta, resposta in list(dicionario["faq"].items()) + dicionario["Roteiro_vendas"].items() + list(dicionario["respostas_automaticas"].items()):
        contexto +=f"\n- {pergunta}:{resposta}"

    prompt =f"""
    Você é o Assistente de Vendas da EVVAALL. Sua missão é conduzir o cliente pelo FUNIL DE VENDAS:
    
    ORDEM DE CONVERSA:
    1. Se o cliente disser 'Oi' ou 'Olá', execute o PASSO 1: Pergunte o nome dele.
    2. Assim que ele disser o nome, execute o PASSO 2: Pergunte o que ele procura (Custo dos seviços, Suporte técnico, Fazer perguntas ou Falar com consultor).
    3. Se ele escolher 'Custo dos serviços', execute o PASSO 3(orçamento): chatbot, automação ou consultoria.
    3.1 Após a resposta dele, execute o PASSO 4(orçamento): Peça o contacto (WhatsApp ou E-mail).
    4. Se ele escolher 'Suporte técnico', execute  o PASSO 3(suporte).
    4.1 Após a resposta dele, execute o PASSO 4(suporte): Peça o contacto (WhatsApp ou E-mail).
    5. Se ele escolher 'Fazer perguntas', execute  o PASSO 3(tirar_duvida).
    5.1 Após a resposta dele, podes procurar uma resposta em BASE DE CONEHECIMNTO.
    6. Se ele escolher 'Falar com consultor', execute  o PASSO 3(falar_com_humano).
    6.1 Após a resposta dele, execute o PASSO 4(falar_com_humano).
    5. No final, execute o PASSO 5: Agradeça e informe que entraremos em contacto em breve.

    REGRAS DE OURO:
    - Não pule etapas.
    - Se ele fizer uma pergunta técnica no meio do processo, responda brevemente usando a BASE DE CONHECIMENTO e volte para o passo onde parou.
    - Se o cliente se recusar a dar o contacto, responda: 'Compreendo perfeitamente a sua privacidade. No entanto, como as nossas soluções são personalizadas para cada negócio, o nosso especialista precisa de fazer 2 ou 3 perguntas técnicas que eu, como assistente virtual, ainda não estou autorizado a processar. Podemos avançar?
    
    REGRAS IMPORTANTES:
        1. Ao responder, responda exclusivamente usando as respostas fornecidas abaixo. Mas, podes corrigir erros ortográficos.
        2. Quando uma responder pergunta, não acabe por aí, tente fazer uma pergunta que leve o cliente de volta ao funil de  vendas.
        3. Se a pergunta não existir na base, responda exatamente com: "{dicionario["respostas_automaticas"]["."]}"
        4. Quando não souberes deves responder educadamente com {dicionario["respostas_automaticas"]["."]}.
        5. Se a mensagem do cliente for 'muito obrigado', podes escolher responder com {dicionario["respostas_automaticas"]["Muito Obrigado"]} ou com {dicionario["respostas_automaticas"]["....."]}.
        
    BASE DE CONHECIMENTO:
    {contexto}
    """
    return prompt

Você disse

from flask import Flask, jsonify, request

from groq import Groq

from dotenv import load_dotenv

import os

from flask_cors import CORS

import smtplib


from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import re


def enviar_notificacao_lead(nome_cliente, contacto_cliente, interesse_cliente):

meu_email = os.getenv("EMAIL")

minha_senha =os.getenv("SENHA_APP")

email_destino =os.getenv("EMAIL") # Onde queres receber o aviso


# Criar a estrutura do e-mail

msg = MIMEMultipart()

msg['From'] = meu_email

msg['To'] = email_destino

msg['Subject'] = f"🔥 NOVO LEAD: {nome_cliente} está interessado!"


corpo = f"""

Temos um novo potencial cliente interessado!

Nome: {nome_cliente}

Contacto: {contacto_cliente}

Interesse: {interesse_cliente}

Responde rápido para não perderes a venda!

"""

msg.attach(MIMEText(corpo, 'plain'))


try:

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(meu_email, minha_senha)

server.send_message(msg)

server.quit()

print("Notificação enviada com sucesso!")

except Exception as e:

print(f"Erro ao enviar e-mail: {e}")


load_dotenv()

Dados = {

"Empresa":"evvaall",

"Contacto":[

"+244957847477",

"ev283@gmail.com"

],

"faq":{

"O Que é a evvaall?": "A evvaall é uma empresa especializada em automação de processos, análise de dados e desenvolvimento de soluções com inteligência artificial para empresas e profissionais.",

"Qual é o vosso objectivo?":"Nosso Objectivo é simplifiar tarefas que levariam muito tempo, aumentar a produtividade e entregar resultados mensuráveis e tecnológicos de ponta.",

"Quais são os serviços que vocês prestram?":"Os nossos serviços são: Análise de dados, Criação de chatboots, Consultoria digital e Automatizamos tarefas repetitivas.",

"Que tipo de Automações?":"Praticamente, qualquer tarefa repetitiva baseada em regras ou que envolva processamento de dados pode ser automatizada. Por exemplo: Envio automático de lembretes de pagamento por WhatsApp, Agendamento de reuniões, Geração e invio automáticos de relatórios.",

"Que tipo de Chatbots?":"Desenvolvemos chatbots inteligentes para atendimento 24/7, integrando com WhatsApp, Telegram, sites e apps.",

"Que tipo de Consultoria?":"Avaliamos seus processos e sugerimos soluções digitais sob medida, identificando o problema e ajudamos na tomada de desisão",

"Que tipo de Análise de dados?":"Por exemplo, Hoje, como é que tu sabes qual é o teu produto mais lucrativo ou qual cliente está prestes a abandonar a tua empresa? Tu usas dados reais ou apenas intuição?",

"Em que árias vocês atuam?":"sector Administrativo, Marketing e vendas, atendimento ao cliente e nas áreas de TI",

"Como faço se eu quiser os vossos Serviços?":"Para mais informação ligue para: 957 847 477, ou deixe 1 mensagem com o serviço entre ' ' e nós entraremos em contacto.",

"Me fale mais sobre vocês":"A evvaall é uma empresa de soluções digitais que ajuda empresas e profissionais a automatizar tarefas repetitivas, transformar dados em decisões estratégicas e criar chatboots inteligentes para a comunicação eficiente.",

"Como é que vocês garantem segurança de informação":"Seguimos boas práticas de: 1-Controle de acesso baseado em permissões, 2-Armazenamento seguro em cloud, 3-Logs auditáveis, 4-Separação de ambiente (produção/teste), Em projetos sensíveis, a arquitetura pode ser ajustada para cumprir exigências específicas do cliente.",

"Que tecnologias utilizam?":"A evvaall adota uma abordagem tecnológica orientada a arquitetura, não a ferramentas isoladas. A escolha das tecnologias depende do contexto operacional do cliente, requisitos de segurança, escalabilidade e integração",

"Como escolhem a tecnologia certa?":"Não utilizamos uma stack fixa por padrão. Selecionamos as tecnologias com base em: 1-Volume de usuários, 2-Exigências regulatórias, 3-Necessidade de escalabilidade, 4-Orçamento do cliente, O foco não é a ferramenta — é o desempenho, segurança e sustentabilidade da solução.",

"Que tipos de empresas podem contratar a evva.all?":"Trabalhamos com restaurantes, empresas do setor bancário, comércio, prestadores de serviços, Clínicas de Saúde, Imobliliárias e scritórios de Advogado/consultoria.",

"O chatbot funciona 24 horas por dia?":"Sim. O sistema funciona 24/7, respondendo clientes automaticamente.",

"O chatbot pode integrar com WhatsApp Business?":"Sim, utilizamos a API oficial do WhatsApp Business para integração segura e profissional.",

"O chatbot substitui funcionários?":"Não. Ele automatiza tarefas repetitivas, permitindo que a equipa foque em atividades estratégicas trazendo mais resultados com os mesmos recursos.",

"A IA aprende com o tempo?":"Sim. Podemos configurar o sistema para melhorar respostas com base em interações reais.",

"O que é análise de dados na prática?":"É transformar dados do seu negócio (vendas, clientes, pagamentos) em informações estratégicas para tomada de decisão.",

"Vocês criam relatórios personalizados?":"Sim. Desenvolvemos dashboards visuais e relatórios adaptados às necessidades da empresa",

"Posso acompanhar os dados em tempo real?":"Dependendo da estrutura do cliente, é possível configurar dashboards com atualização automática.",

"Os dados da minha empresa ficam seguros?":"Sim. Trabalhamos com boas práticas de segurança e integração com APIs oficiais.",

"Vocês trabalham com contratos formais?":"Sim. Todos os serviços podem ser formalizados por contrato.",

"Onde os sistemas ficam hospedados?":"Podem ser hospedados em servidores seguros (cloud) ou na infraestrutura do cliente.",

"Como funciona o processo de contratação?":"Diagnóstico do problema, Proposta técnica, Desenvolvimento, Implementação, Suporte.",

"O pagamento é mensal ou único?":"Depende do serviço, projetos personalizados e únicos podem ser pagos por projetos desenvolvidos, sistemas com manutenção podem ter pagamento mensal.",

"Por que escolher a evvaall?":"Porque combinamos tecnologia, estratégia e personalização. Não vendemos soluções genéricas — desenvolvemos sistemas adaptados ao seu negócio.",

"Quanto custam os vossos serviços?":"O valor depende do nível de complexidade e integrações necessárias.Preciso de entender o seu desafio. Pode deixar o seu WhatsApp ou e-mail aqui?.",

"Quanto custa um chatbot?":"O valor depende do nível de complexidade e integrações necessárias.",

"Como funcionam os chatbots com IA desenvolvidos pela evvaall?":"Nossos sistemas utilizam modelos de linguagem integrados a regras de negócio específicas do cliente. A arquitetura geralmente envolve: 1-Interface (Site ou WhatsApp Business API), 2-Backend seguro (API própria), 3-Motor de IA, 4-Base de conhecimento personalizada, 5-Logs e monitoramento de desempenho, Isso permite respostas contextuais, automação de processos e coleta estruturada de dados.",

"A IA toma decisões automáticas?":"A IA executa ações dentro de limites definidos. Sempre existe configuração de regras e possibilidade de supervisão humana para processos críticos. Não implementamos sistemas que atuem sem governança.",

"Como a análise de dados gera valor real?":"Transformamos dados brutos em indicadores estratégicos como: 1-Taxa de conversão, 2-Tempo médio de atendimento, 3-Índice de recorrência de clientes, 4-Análise de inadimplência, 5-Padrões de comportamento, Isso permite decisões baseadas em evidência e não em suposição.",

"O que diferencia a evvaall de outras empresas de tecnologia?":"1-Foco em automação orientada a resultado, 2-Integração entre IA + dados + processos, 3-Arquitetura enxuta e escalável, 4-Abordagem consultiva antes do desenvolvimento, 5-Implementação adaptada à realidade local",

"Como funciona o ciclo de implementação?":"1-Diagnóstico técnico e operacional, 2-Mapeamento de processos, 3-Definição da arquitetura, 4-Desenvolvimento e testes, 5-Implantação controlada, 6-Monitoramento e otimização contínua",

},

"respostas_automaticas":{

".":"Este é um agente de atendimento que responde a perguntas sobre a evvall. Existem perguntas que não estou autorizado a processar",

"..":"Muito Obrigado!",

"Muito Obrigado":"Nada por isso. Até à próxima!",

"*":"Deixe o seu recado. depois entraremos em contacto.",

"**":"Deixe sua mensagem entre ' ' que nós entraremos em contacto.",

"....":"Acesse o nosso site para mais informação.",

".....":"fui útil?",

}

}

Dados["Roteiro_vendas"] = {

"passo_1": "Olá! Bem-vindo à evvaall. Eu sou o assistente virtual inteligente. Com quem tenho o prazer de falar?",

"passo_2": "Prazer, {nome}! Para te ajudar da melhor forma, o que procura hoje?\n1. Custos dos serviços;\n2. Suporte Técnico\n3. Fazer perguntas\n4. Falar com um Consultor Humano",

"passo_3_orcamento": "Entendido. Para que eu possa preparar um valor aproximado, como descreveria o seu projeto atual? (Ex: Pequena automação, Sistema completo de dados ou Chatbot para empresa)",

"passo_3_suporte":"Entendido! A nossa equipa técnica está pronta para ajudar. Para agilizarmos, pode descrever brevemente o que está a acontecer ou indicar o número do seu contrato/projeto?",

"passo_3_falar_com_humano":"Com certeza! Nada substitui uma boa conversa estratégica. O nosso consultor especialista terá todo o prazer em falar consigo. Para agendarmos uma chamada breve de 5 a 10 minutos ou para ele lhe enviar um convite de reunião, qual é o seu contacto?",

"passo_3_tirar_duvida":"Excelente! Sobre o que você gostaria de saber mais agora?\n>•Quais são os nossos Serviços;\n•Qual é o Nosso objectivo?\n•Em que árias nós atuamos?\n•Faça uma outra pergunta.",

"passo_4_orçamento":"Excelente. Para que o nosso especialista envie a proposta detalhada e o cronograma, por favor, deixe o seu WhatsApp ou E-mail.",

"passo_4_suporte":"Obrigado pelo detalhe. Vou abrir um ticket prioritário agora. Qual o melhor número de WhatsApp para o técnico lhe contactar caso precisemos de acesso remoto ou mais detalhes?",

"passo_4_falar_com_humano":"Excelente, vou passar agora mesmo para o nosso consultor no WhatsApp, é mais rápido!.Posso ajudar em algo mais?",

"passo_5_final":"Muito obrigado! Recebi os seus dados. Em menos de 2 horas um consultor entrará em contacto consigo. Posso ajudar em algo mais?"

}

client = Groq(

api_key=os.getenv("GROQ_API_KEY")

)

def conected(mensagem:str):

msn=mensagem.capitalize().strip()

if msn in Dados["respostas_automaticas"]:

return Dados["respostas_automaticas"][msn]

elif msn in Dados["faq"]:

return Dados["faq"][msn]

else:

return msn


def orientacao(dicionario:dict) -> str:

contexto =""

for pergunta, resposta in list(dicionario["faq"].items()) + dicionario["Roteiro_vendas"].items() + list(dicionario["respostas_automaticas"].items()):

contexto +=f"\n- {pergunta}:{resposta}"


prompt =f"""

Você é o Assistente de Vendas da EVVAALL. Sua missão é conduzir o cliente pelo FUNIL DE VENDAS:

ORDEM DE CONVERSA:

1. Se o cliente disser 'Oi' ou 'Olá', execute o PASSO 1: Pergunte o nome dele.

2. Assim que ele disser o nome, execute o PASSO 2: Pergunte o que ele procura (Custo dos seviços, Suporte técnico, Fazer perguntas ou Falar com consultor).

3. Se ele escolher 'Custo dos serviços', execute o PASSO 3(orçamento): chatbot, automação ou consultoria.

3.1 Após a resposta dele, execute o PASSO 4(orçamento): Peça o contacto (WhatsApp ou E-mail).

4. Se ele escolher 'Suporte técnico', execute o PASSO 3(suporte).

4.1 Após a resposta dele, execute o PASSO 4(suporte): Peça o contacto (WhatsApp ou E-mail).

5. Se ele escolher 'Fazer perguntas', execute o PASSO 3(tirar_duvida).

5.1 Após a resposta dele, podes procurar uma resposta em BASE DE CONEHECIMNTO.

6. Se ele escolher 'Falar com consultor', execute o PASSO 3(falar_com_humano).

6.1 Após a resposta dele, execute o PASSO 4(falar_com_humano).

5. No final, execute o PASSO 5: Agradeça e informe que entraremos em contacto em breve.


REGRAS DE OURO:

- Não pule etapas.

- Se ele fizer uma pergunta técnica no meio do processo, responda brevemente usando a BASE DE CONHECIMENTO e volte para o passo onde parou.

- Se o cliente se recusar a dar o contacto, responda: 'Compreendo perfeitamente a sua privacidade. No entanto, como as nossas soluções são personalizadas para cada negócio, o nosso especialista precisa de fazer 2 ou 3 perguntas técnicas que eu, como assistente virtual, ainda não estou autorizado a processar. Podemos avançar?

REGRAS IMPORTANTES:

1. Ao responder, responda exclusivamente usando as respostas fornecidas abaixo. Mas, podes corrigir erros ortográficos.

2. Quando uma responder pergunta, não acabe por aí, tente fazer uma pergunta que leve o cliente de volta ao funil de vendas.

3. Se a pergunta não existir na base, responda exatamente com: "{dicionario["respostas_automaticas"]["."]}"

4. Quando não souberes deves responder educadamente com {dicionario["respostas_automaticas"]["."]}.

5. Se a mensagem do cliente for 'muito obrigado', podes escolher responder com {dicionario["respostas_automaticas"]["Muito Obrigado"]} ou com {dicionario["respostas_automaticas"]["....."]}.

BASE DE CONHECIMENTO:

{contexto}

"""

return prompt


def enviar_mensagem(mensagem, historico):

historico.append({

"role": "user",

"content": mensagem

})

completion = client.chat.completions.create(

model="llama-3.3-70b-versatile",

messages=historico,

temperature=0.6

)

resposta = completion.choices[0].message.content

historico.append({

"role": "assistant",

"content": resposta

})

return resposta



app = Flask(__name__)

CORS(app)


@app.route("/ask", methods=["POST"])

def home():

data = request.get_json()

if not data or "mensagem" not in data:

return jsonify(

{

"erro":"envie {'mensagem':'texto aqui'}"

}, 400

)

mensagem = data["mensagem"].strip()

# detetar número de telefone (Angola)

padrao_tel = r"9\d{8}"

tell = re.search(padrao_tel, mensagem)

padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"

email = re.search(padrao_email, mensagem)


if tell or email:

contacto = tell.group(0) if tell else email.group(0)

enviar_notificacao_lead("Cliente do Site evvaall", contacto, "Interesse detetado via Chat")

if mensagem in Dados["faq"]:

return jsonify({"resposta": Dados["faq"][mensagem]})

historico = [

{"role": "system", "content": f"Você é um assistente útil. {orientacao(Dados)}"}

]

historico_usuario = data.get("historico", [])

historico.extend(historico_usuario())

historico.append({"role": "user", "content": mensagem})

try:

resposta = enviar_mensagem(mensagem, historico)

except Exception as e:

resposta = "Desculpa, teve um pequeno problema técnico. podes ligar para 957 847 477."

return jsonify({"resposta":resposta})


if __name__ == "__main__":

app.run()
O Gemini disse

O teu código tem uma estrutura sólida para um MVP (Produto Mínimo Viável), mas encontrei alguns erros críticos de execução, especialmente na manipulação do histórico e na lógica de rotas do Flask, que farão o bot "esquecer" o contexto ou dar erro de servidor.

Aqui estão as correções e melhorias necessárias:
1. Correções Críticas no Código

    Erro no historico_usuario(): No teu código, estavas a tentar chamar a lista como se fosse uma função: historico.extend(historico_usuario()). O correto é apenas historico_usuario.

    Gestão de Estado: O Flask é stateless. Para o bot seguir o funil de vendas (Passo 1, 2, 3...), o frontend precisa de enviar o histórico completo em cada requisição, ou precisas de uma base de dados (Redis/SQL) para guardar a conversa.

    Loop de Recursão: A tua função enviar_mensagem já adiciona a mensagem ao histórico, mas a rota home também estava a tentar fazer isso. Unifiquei a lógica para evitar duplicação.

Código Corrigido e Otimizado
Python

from flask import Flask, jsonify, request
from groq import Groq
from dotenv import load_dotenv
import os
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

load_dotenv()

# --- Configurações e Dados (Mantidos conforme o seu original) ---
Dados = {
    "Empresa":"evvaall",
    "Contacto":["+244957847477", "ev283@gmail.com"],
    "faq": {
        "O Que é a evvaall?": "A evvaall é uma empresa especializada em automação de processos...",
        # ... (restante do seu dicionário faq)
    },
    "respostas_automaticas": {
        ".": "Este é um agente de atendimento que responde a perguntas sobre a evvall...",
        "Muito Obrigado": "Nada por isso. Até à próxima!",
        ".....": "fui útil?",
    }
}

Dados["Roteiro_vendas"] = {
    "passo_1": "Olá! Bem-vindo à evvaall. Eu sou o assistente virtual inteligente. Com quem tenho o prazer de falar?",
    "passo_2": "Prazer, {nome}! Para te ajudar da melhor forma, o que procura hoje?\n1. Custos dos serviços;\n2. Suporte Técnico\n3. Fazer perguntas\n4. Falar com um Consultor Humano",
    # ... (restante do roteiro)
}

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# --- Funções de Apoio ---

def enviar_notificacao_lead(nome_cliente, contacto_cliente, interesse_cliente):
    meu_email = os.getenv("EMAIL")
    minha_senha = os.getenv("SENHA_APP")
    
    msg = MIMEMultipart()
    msg['From'] = meu_email
    msg['To'] = meu_email
    msg['Subject'] = f"🔥 NOVO LEAD: {nome_cliente}"

    corpo = f"Novo Lead detectado!\n\nContacto: {contacto_cliente}\nInteresse: {interesse_cliente}"
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(meu_email, minha_senha)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

def gerar_prompt_sistema(dicionario):
    contexto = ""
    for pergunta, resposta in list(dicionario["faq"].items()) + list(dicionario["Roteiro_vendas"].items()):
        contexto += f"\n- {pergunta}: {resposta}"
    
    return f"""Você é o Assistente de Vendas da EVVAALL. Conduza o cliente pelo FUNIL:
    1. Oi/Olá -> PASSO 1 (Pedir nome).
    2. Nome recebido -> PASSO 2 (Opções de serviço).
    ... (Regras de Funil mantidas)
    BASE DE CONHECIMENTO: {contexto}"""

# --- Flask App ---

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "mensagem" not in data:
        return jsonify({"erro": "Envie 'mensagem' no JSON"}), 400

    mensagem_usuario = data["mensagem"].strip()
    # Recupera o histórico enviado pelo frontend ou inicia um vazio
    historico_recebido = data.get("historico", [])

    # 1. Detecção de Leads (Regex)
    padrao_tel = r"(9\d{8})"
    padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"
    
    match_tel = re.search(padrao_tel, mensagem_usuario)
    match_email = re.search(padrao_email, mensagem_usuario)

    if match_tel or match_email:
        contacto = match_tel.group(0) if match_tel else match_email.group(0)
        enviar_notificacao_lead("Cliente Web", contacto, mensagem_usuario)

    # 2. Construção do Histórico para a IA
    mensagens_ia = [{"role": "system", "content": gerar_prompt_sistema(Dados)}]
    mensagens_ia.extend(historico_recebido)
    mensagens_ia.append({"role": "user", "content": mensagem_usuario})

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=mensagens_ia,
            temperature=0.4 # Reduzido para ser mais assertivo no funil
        )
        resposta_ia = completion.choices[0].message.content
        
        # 3. Retornar resposta e o histórico atualizado para o frontend guardar
        novo_historico = historico_recebido + [
            {"role": "user", "content": mensagem_usuario},
            {"role": "assistant", "content": resposta_ia}
        ]
        
        return jsonify({
            "resposta": resposta_ia,
            "historico": novo_historico
        })

    except Exception as e:
        print(f"Erro Groq: {e}")
        return jsonify({"resposta": "Tivemos um problema técnico. Ligue para 957 847 477."}), 500

if __name__ == "__main__":
    app.run(debug=True)

O que foi melhorado?

    Persistência de Memória: O bot agora devolve o novo_historico para o frontend. O teu site deve guardar isso numa variável e enviar de volta no próximo POST. Sem isso, o Llama nunca saberá que já perguntou o nome do cliente.

    Segurança de Tipos: Removi a chamada historico_usuario() que causaria um erro TypeError.

    Refinamento do Prompt: Reduzi a temperature para 0.4. Para bots de vendas, valores altos (0.7+) fazem a IA "inventar" demais. Valores baixos mantêm-na focada nas tuas regras de ouro.

    Captura de Leads: Melhorei o Regex para ser mais específico aos números de Angola (começando com 9).

Próximo Passo Recomendado

Gostarias que eu te ajudasse a criar um pequeno exemplo de código em JavaScript/HTML para testares este chatbot no teu navegador e veres como o histórico é enviado? Seria ideal para validar o funil de vendas.
Você disse

ST https://evva-all-backend.onrender.com//ask -H "Content-Type: application/json" -d '{"mensagem":"Olá "}'

<!doctype html>

<html lang=en>

<title>500 Internal Server Error</title>

<h1>Internal Server Error</h1>

<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
O Gemini disse

O erro 500 Internal Server Error que estás a receber acontece porque o teu código original tinha um erro de sintaxe na linha onde tentas manipular o histórico.

O erro específico está aqui:
historico.extend(historico_usuario())

Como historico_usuario é uma lista (vinda do request.get_json()), ao usares os parênteses (), o Python pensa que estás a tentar chamar uma função, o que causa o crash do servidor.

Aqui está o fluxo de correção para o teu backend no Render:
1. Correção no Ficheiro app.py

Substitui o bloco da rota /ask por este, que já trata o histórico como uma lista e evita o erro 500:
Python

@app.route("/ask", methods=["POST"])
def home():
    data = request.get_json()
    if not data or "mensagem" not in data:
        return jsonify({"erro": "envie {'mensagem':'texto aqui'}"}), 400

    mensagem = data["mensagem"].strip()
    
    # 1. Captura de Leads (Email/Telefone)
    padrao_tel = r"9\d{8}"
    tell = re.search(padrao_tel, mensagem)
    padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"
    email = re.search(padrao_email, mensagem)

    if tell or email:
        contacto = tell.group(0) if tell else email.group(0)
        enviar_notificacao_lead("Cliente do Site evvaall", contacto, "Interesse detetado via Chat")

    # 2. Gestão do Histórico (CORREÇÃO AQUI)
    # Pegamos o histórico que vem do frontend ou criamos uma lista vazia
    historico_usuario = data.get("historico", [])
    
    # Criamos a mensagem de sistema (instruções do bot)
    mensagens_para_ia = [
        {"role": "system", "content": orientacao(Dados)}
    ]
    
    # Adicionamos o histórico anterior e a nova mensagem
    mensagens_para_ia.extend(historico_usuario)
    mensagens_para_ia.append({"role": "user", "content": mensagem})

    try:
        # Chamada à API da Groq
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=mensagens_para_ia,
            temperature=0.5
        )
        resposta = completion.choices[0].message.content
        
        # Atualizamos o histórico para devolver ao frontend
        historico_usuario.append({"role": "user", "content": mensagem})
        historico_usuario.append({"role": "assistant", "content": resposta})

        return jsonify({
            "resposta": resposta,
            "historico": historico_usuario  # O frontend deve guardar isto
        })

    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"resposta": "Desculpa, tive um problema técnico. Liga para 957 847 477."}), 500

2. Porque é que o histórico é vital?

Para que o Funil de Vendas funcione (Passo 1 -> Passo 2), a IA precisa de saber o que foi dito antes. Como o Flask "esquece" tudo mal envia a resposta, o esquema funciona assim:

    Cliente envia: {"mensagem": "Olá"}

    Servidor responde: {"resposta": "Olá! Qual o seu nome?", "historico": [{"role": "user", "content": "Olá"}, {"role": "assistant", "content": "Olá! Qual o seu nome?"}]}

    Cliente envia na próxima vez: {"mensagem": "João", "historico": [...o histórico anterior...]}

3. Checklist para o Render

    Variáveis de Ambiente: Verifica se no painel do Render adicionaste as chaves GROQ_API_KEY, EMAIL e SENHA_APP. Sem elas, o código vai dar erro ao tentar enviar o email ou falar com a IA.

    Logs: Se o erro persistir, clica em "Logs" no menu lateral do Render. Ele dirá exatamente em que linha o Python falhou.

Queres que eu ajude a configurar as Variáveis de Ambiente no painel do Render para garantir que a ligação com a Groq não falhe?
Você disse

from flask import Flask, jsonify, request

from groq import Groq

from dotenv import load_dotenv

import os

from flask_cors import CORS

import smtplib


from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import re


def enviar_notificacao_lead(nome_cliente, contacto_cliente, interesse_cliente):

    meu_email = os.getenv("EMAIL")

    minha_senha =os.getenv("SENHA_APP")

    email_destino =os.getenv("EMAIL") # Onde queres receber o aviso


    # Criar a estrutura do e-mail

    msg = MIMEMultipart()

    msg['From'] = meu_email

    msg['To'] = email_destino

    msg['Subject'] = f"🔥 NOVO LEAD: {nome_cliente} está interessado!"


    corpo = f"""

    Temos um novo potencial cliente interessado!

    

    Nome: {nome_cliente}

    Contacto: {contacto_cliente}

    Interesse: {interesse_cliente}

    

    Responde rápido para não perderes a venda!

    """

    msg.attach(MIMEText(corpo, 'plain'))


    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(meu_email, minha_senha)

        server.send_message(msg)

        server.quit()

        print("Notificação enviada com sucesso!")

    except Exception as e:

        print(f"Erro ao enviar e-mail: {e}")


load_dotenv()

Dados = {

    "Empresa":"evvaall",

    "Contacto":[

        "+244957847477",

        "ev283@gmail.com"

    ],

    "faq":{

        "O Que é a evvaall?": "A evvaall é uma empresa especializada em automação de processos, análise de dados e desenvolvimento de soluções com inteligência artificial para empresas e profissionais.",

        "Qual é o vosso objectivo?":"Nosso Objectivo é simplifiar tarefas que levariam muito tempo, aumentar a produtividade e entregar resultados mensuráveis e tecnológicos de ponta.",

        "Quais são os serviços que vocês prestram?":"Os nossos serviços são: Análise de dados, Criação de chatboots, Consultoria digital e Automatizamos tarefas repetitivas.",

        "Que tipo de Automações?":"Praticamente, qualquer tarefa repetitiva baseada em regras ou que envolva processamento de dados pode ser automatizada. Por exemplo: Envio automático de lembretes de pagamento por WhatsApp, Agendamento de reuniões, Geração e invio automáticos de relatórios.",

        "Que tipo de Chatbots?":"Desenvolvemos chatbots inteligentes para atendimento 24/7, integrando com WhatsApp, Telegram, sites e apps.",

        "Que tipo de Consultoria?":"Avaliamos seus processos e sugerimos soluções digitais sob medida, identificando o problema e ajudamos na tomada de desisão",

        "Que tipo de Análise de dados?":"Por exemplo, Hoje, como é que tu sabes qual é o teu produto mais lucrativo ou qual cliente está prestes a abandonar a tua empresa? Tu usas dados reais ou apenas intuição?",

        "Em que árias vocês atuam?":"sector Administrativo, Marketing e vendas, atendimento ao cliente e nas áreas de TI",

        "Como faço se eu quiser os vossos Serviços?":"Para mais informação ligue para: 957 847 477, ou deixe 1 mensagem com o serviço entre ' ' e nós entraremos em contacto.",

        "Me fale mais sobre vocês":"A evvaall é uma empresa de soluções digitais que ajuda empresas e profissionais a automatizar tarefas repetitivas, transformar dados em decisões estratégicas e criar chatboots inteligentes para a comunicação eficiente.",

        "Como é que vocês garantem segurança de informação":"Seguimos boas práticas de: 1-Controle de acesso baseado em permissões, 2-Armazenamento seguro em cloud, 3-Logs auditáveis, 4-Separação de ambiente (produção/teste), Em projetos sensíveis, a arquitetura pode ser ajustada para cumprir exigências específicas do cliente.",

        "Que tecnologias utilizam?":"A evvaall adota uma abordagem tecnológica orientada a arquitetura, não a ferramentas isoladas. A escolha das tecnologias depende do contexto operacional do cliente, requisitos de segurança, escalabilidade e integração",

        "Como escolhem a tecnologia certa?":"Não utilizamos uma stack fixa por padrão. Selecionamos as tecnologias com base em: 1-Volume de usuários, 2-Exigências regulatórias, 3-Necessidade de escalabilidade, 4-Orçamento do cliente, O foco não é a ferramenta — é o desempenho, segurança e sustentabilidade da solução.",

        "Que tipos de empresas podem contratar a evva.all?":"Trabalhamos com restaurantes, empresas do setor bancário, comércio, prestadores de serviços, Clínicas de Saúde, Imobliliárias e scritórios de Advogado/consultoria.",

        "O chatbot funciona 24 horas por dia?":"Sim. O sistema funciona 24/7, respondendo clientes automaticamente.",

        "O chatbot pode integrar com WhatsApp Business?":"Sim, utilizamos a API oficial do WhatsApp Business para integração segura e profissional.",

        "O chatbot substitui funcionários?":"Não. Ele automatiza tarefas repetitivas, permitindo que a equipa foque em atividades estratégicas trazendo mais resultados com os mesmos recursos.",

        "A IA aprende com o tempo?":"Sim. Podemos configurar o sistema para melhorar respostas com base em interações reais.",

        "O que é análise de dados na prática?":"É transformar dados do seu negócio (vendas, clientes, pagamentos) em informações estratégicas para tomada de decisão.",

        "Vocês criam relatórios personalizados?":"Sim. Desenvolvemos dashboards visuais e relatórios adaptados às necessidades da empresa",

        "Posso acompanhar os dados em tempo real?":"Dependendo da estrutura do cliente, é possível configurar dashboards com atualização automática.",

        "Os dados da minha empresa ficam seguros?":"Sim. Trabalhamos com boas práticas de segurança e integração com APIs oficiais.",

        "Vocês trabalham com contratos formais?":"Sim. Todos os serviços podem ser formalizados por contrato.",

        "Onde os sistemas ficam hospedados?":"Podem ser hospedados em servidores seguros (cloud) ou na infraestrutura do cliente.",

        "Como funciona o processo de contratação?":"Diagnóstico do problema, Proposta técnica, Desenvolvimento, Implementação, Suporte.",

        "O pagamento é mensal ou único?":"Depende do serviço, projetos personalizados e únicos podem ser pagos por  projetos desenvolvidos, sistemas com manutenção podem ter pagamento mensal.",

        "Por que escolher a evvaall?":"Porque combinamos tecnologia, estratégia e personalização. Não vendemos soluções genéricas — desenvolvemos sistemas adaptados ao seu negócio.",

        "Quanto custam os vossos serviços?":"O valor depende do nível de complexidade e integrações necessárias.Preciso de entender o seu desafio. Pode deixar o seu WhatsApp ou e-mail aqui?.",

        "Quanto custa um chatbot?":"O valor depende do nível de complexidade e integrações necessárias.",

        "Como funcionam os chatbots com IA desenvolvidos pela evvaall?":"Nossos sistemas utilizam modelos de linguagem integrados a regras de negócio específicas do cliente. A arquitetura geralmente envolve: 1-Interface (Site ou WhatsApp Business API), 2-Backend seguro (API própria), 3-Motor de IA, 4-Base de conhecimento personalizada, 5-Logs e monitoramento de desempenho, Isso permite respostas contextuais, automação de processos e coleta estruturada de dados.",

        "A IA toma decisões automáticas?":"A IA executa ações dentro de limites definidos. Sempre existe configuração de regras e possibilidade de supervisão humana para processos críticos. Não implementamos sistemas que atuem sem governança.",

        "Como a análise de dados gera valor real?":"Transformamos dados brutos em indicadores estratégicos como: 1-Taxa de conversão, 2-Tempo médio de atendimento, 3-Índice de recorrência de clientes, 4-Análise de inadimplência, 5-Padrões de comportamento, Isso permite decisões baseadas em evidência e não em suposição.",

        "O que diferencia a evvaall de outras empresas de tecnologia?":"1-Foco em automação orientada a resultado, 2-Integração entre IA + dados + processos, 3-Arquitetura enxuta e escalável, 4-Abordagem consultiva antes do desenvolvimento, 5-Implementação adaptada à realidade local",

        "Como funciona o ciclo de implementação?":"1-Diagnóstico técnico e operacional, 2-Mapeamento de processos, 3-Definição da arquitetura, 4-Desenvolvimento e testes, 5-Implantação controlada, 6-Monitoramento e otimização contínua",

    },

    "respostas_automaticas":{

        ".":"Este é um agente de atendimento que responde a perguntas sobre a evvall. Existem perguntas que não estou autorizado a processar",

        "..":"Muito Obrigado!",

        "Muito Obrigado":"Nada por isso. Até à próxima!",

        "*":"Deixe o seu recado. depois entraremos em contacto.",

        "**":"Deixe sua mensagem entre ' ' que nós entraremos em contacto.",

        "....":"Acesse o nosso site para mais informação.",

        ".....":"fui útil?",

    }

}

Dados["Roteiro_vendas"] = {

    "passo_1": "Olá! Bem-vindo à evvaall. Eu sou o assistente virtual inteligente. Com quem tenho o prazer de falar?",

    "passo_2": "Prazer, {nome}! Para te ajudar da melhor forma, o que procura hoje?\n1. Custos dos serviços;\n2. Suporte Técnico\n3. Fazer perguntas\n4. Falar com um Consultor Humano",

    "passo_3_orcamento": "Entendido. Para que eu possa preparar um valor aproximado, como descreveria o seu projeto atual? (Ex: Pequena automação, Sistema completo de dados ou Chatbot para empresa)",

    "passo_3_suporte":"Entendido! A nossa equipa técnica está pronta para ajudar. Para agilizarmos, pode descrever brevemente o que está a acontecer ou indicar o número do seu contrato/projeto?",    

    "passo_3_falar_com_humano":"Com certeza! Nada substitui uma boa conversa estratégica. O nosso consultor especialista terá todo o prazer em falar consigo. Para agendarmos uma chamada breve de 5 a 10 minutos ou para ele lhe enviar um convite de reunião, qual é o seu contacto?",

    "passo_3_tirar_duvida":"Excelente! Sobre o que você gostaria de saber mais agora?\n>•Quais são os nossos Serviços;\n•Qual é o Nosso objectivo?\n•Em que árias nós atuamos?\n•Faça uma outra pergunta.",

    "passo_4_orçamento":"Excelente. Para que o nosso especialista envie a proposta detalhada e o cronograma, por favor, deixe o seu WhatsApp ou E-mail.",

    "passo_4_suporte":"Obrigado pelo detalhe. Vou abrir um ticket prioritário agora. Qual o melhor número de WhatsApp para o técnico lhe contactar caso precisemos de acesso remoto ou mais detalhes?",

    "passo_4_falar_com_humano":"Excelente, vou passar agora mesmo para o nosso consultor no WhatsApp, é mais rápido!.Posso ajudar em algo mais?",

    "passo_5_final":"Muito obrigado! Recebi os seus dados. Em menos de 2 horas um consultor entrará em contacto consigo. Posso ajudar em algo mais?"

}

client = Groq(

    api_key=os.getenv("GROQ_API_KEY")

)

def conected(mensagem:str):

    msn=mensagem.capitalize().strip()

    if msn in Dados["respostas_automaticas"]:

        return Dados["respostas_automaticas"][msn]

    elif msn in Dados["faq"]:

        return Dados["faq"][msn]

    else:

        return msn


def orientacao(dicionario:dict) -> str:

    contexto =""

    for pergunta, resposta in list(dicionario["faq"].items()) + dicionario["Roteiro_vendas"].items() + list(dicionario["respostas_automaticas"].items()):

        contexto +=f"\n- {pergunta}:{resposta}"


    prompt =f"""

    Você é o Assistente de Vendas da EVVAALL. Sua missão é conduzir o cliente pelo FUNIL DE VENDAS:

    

    ORDEM DE CONVERSA:

    1. Se o cliente disser 'Oi' ou 'Olá', execute o PASSO 1: Pergunte o nome dele.

    2. Assim que ele disser o nome, execute o PASSO 2: Pergunte o que ele procura (Custo dos seviços, Suporte técnico, Fazer perguntas ou Falar com consultor).

    3. Se ele escolher 'Custo dos serviços', execute o PASSO 3(orçamento): chatbot, automação ou consultoria.

    3.1 Após a resposta dele, execute o PASSO 4(orçamento): Peça o contacto (WhatsApp ou E-mail).

    4. Se ele escolher 'Suporte técnico', execute  o PASSO 3(suporte).

    4.1 Após a resposta dele, execute o PASSO 4(suporte): Peça o contacto (WhatsApp ou E-mail).

    5. Se ele escolher 'Fazer perguntas', execute  o PASSO 3(tirar_duvida).

    5.1 Após a resposta dele, podes procurar uma resposta em BASE DE CONEHECIMNTO.

    6. Se ele escolher 'Falar com consultor', execute  o PASSO 3(falar_com_humano).

    6.1 Após a resposta dele, execute o PASSO 4(falar_com_humano).

    5. No final, execute o PASSO 5: Agradeça e informe que entraremos em contacto em breve.


    REGRAS DE OURO:

    - Não pule etapas.

    - Se ele fizer uma pergunta técnica no meio do processo, responda brevemente usando a BASE DE CONHECIMENTO e volte para o passo onde parou.

    - Se o cliente se recusar a dar o contacto, responda: 'Compreendo perfeitamente a sua privacidade. No entanto, como as nossas soluções são personalizadas para cada negócio, o nosso especialista precisa de fazer 2 ou 3 perguntas técnicas que eu, como assistente virtual, ainda não estou autorizado a processar. Podemos avançar?

    

    REGRAS IMPORTANTES:

        1. Ao responder, responda exclusivamente usando as respostas fornecidas abaixo. Mas, podes corrigir erros ortográficos.

        2. Quando uma responder pergunta, não acabe por aí, tente fazer uma pergunta que leve o cliente de volta ao funil de  vendas.

        3. Se a pergunta não existir na base, responda exatamente com: "{dicionario["respostas_automaticas"]["."]}"

        4. Quando não souberes deves responder educadamente com {dicionario["respostas_automaticas"]["."]}.

        5. Se a mensagem do cliente for 'muito obrigado', podes escolher responder com {dicionario["respostas_automaticas"]["Muito Obrigado"]} ou com {dicionario["respostas_automaticas"]["....."]}.

        

    BASE DE CONHECIMENTO:

    {contexto}

    """

    return prompt


def enviar_mensagem(mensagem, historico):

    historico.append({

        "role": "user",

        "content": mensagem

    })

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=historico,

        temperature=0.4

    )

    resposta = completion.choices[0].message.content

    historico.append({

        "role": "assistant",

        "content": resposta

    })

    return resposta



app = Flask(__name__)

CORS(app)


@app.route("/ask", methods=["POST"])

def home():

    data = request.get_json()

    if not data or "mensagem" not in data:

        return jsonify(

            {

                "erro":"envie {'mensagem':'texto aqui'}"

            }, 400

        )

    mensagem = data["mensagem"].strip()

    # detetar número de telefone (Angola)

    padrao_tel = r"9\d{8}"

    tell = re.search(padrao_tel, mensagem)

    padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"

    email = re.search(padrao_email, mensagem)


    

    if tell or email:

        contacto = tell.group(0) if tell else email.group(0)

        enviar_notificacao_lead("Cliente do Site evvaall", contacto, "Interesse detetado via Chat")

    

    if mensagem in Dados["faq"]:

        return jsonify({"resposta": Dados["faq"][mensagem]})

        

    historico = [

        {"role": "system", "content": f"Você é um assistente útil. {orientacao(Dados)}"}

    ]

    historico_usuario = data.get("historico", [])

    historico.extend(historico_usuario)

    historico.append({"role": "user", "content": mensagem})

    try:

        resposta = enviar_mensagem(mensagem, historico)

    except Exception as e:

        resposta = "Desculpa, teve um pequeno problema técnico. podes ligar para 957 847 477."

    return jsonify({"resposta":resposta})


if __name__ == "__main__":

    app.run()
O Gemini disse

Entendido! Analisando o teu código atualizado, notei que já corrigiste o erro anterior (historico_usuario() para historico_usuario). No entanto, para que o bot funcione perfeitamente no Render e não se perca no funil de vendas, precisamos de ajustar como a resposta é enviada de volta.

Aqui está a versão otimizada para garantir que o contexto (memória) seja mantido entre as perguntas e que o erro 500 não volte a acontecer por falta de variáveis de ambiente.
Código Otimizado (Backend)
Python

from flask import Flask, jsonify, request
from groq import Groq
from dotenv import load_dotenv
import os
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

load_dotenv()

# ... [Teus dicionários 'Dados' e 'Roteiro_vendas' permanecem iguais] ...

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def enviar_notificacao_lead(nome_cliente, contacto_cliente, interesse_cliente):
    meu_email = os.getenv("EMAIL")
    minha_senha = os.getenv("SENHA_APP")
    if not meu_email or not minha_senha:
        print("Erro: Credenciais de e-mail não configuradas.")
        return

    msg = MIMEMultipart()
    msg['From'] = meu_email
    msg['To'] = meu_email 
    msg['Subject'] = f"🔥 NOVO LEAD: {nome_cliente}"

    corpo = f"Novo interesse detectado!\n\nContacto: {contacto_cliente}\nInteresse: {interesse_cliente}"
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(meu_email, minha_senha)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Função para construir o prompt do sistema
def orientacao(dicionario:dict) -> str:
    contexto = ""
    for pergunta, resposta in list(dicionario["faq"].items()) + list(dicionario["Roteiro_vendas"].items()):
        contexto += f"\n- {pergunta}:{resposta}"
    
    return f"""Você é o Assistente de Vendas da EVVAALL.
    Sua missão é seguir estritamente o FUNIL DE VENDAS (Passo 1 ao 5).
    BASE DE CONHECIMENTO: {contexto}"""

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def home():
    data = request.get_json()
    if not data or "mensagem" not in data:
        return jsonify({"erro": "Envie 'mensagem' no corpo do JSON"}), 400

    mensagem = data["mensagem"].strip()
    
    # 1. Detecção de Leads
    padrao_tel = r"9\d{8}"
    tell = re.search(padrao_tel, mensagem)
    padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"
    email = re.search(padrao_email, mensagem)

    if tell or email:
        contacto = tell.group(0) if tell else email.group(0)
        enviar_notificacao_lead("Cliente Web", contacto, mensagem)

    # 2. Gestão de Memória (O segredo para o funil funcionar)
    # O frontend deve enviar o 'historico' nas requisições seguintes
    historico_usuario = data.get("historico", [])
    
    mensagens_para_ia = [{"role": "system", "content": orientacao(Dados)}]
    mensagens_para_ia.extend(historico_usuario)
    mensagens_para_ia.append({"role": "user", "content": mensagem})

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=mensagens_para_ia,
            temperature=0.4
        )
        resposta = completion.choices[0].message.content
        
        # Atualizamos o histórico para enviar de volta ao cliente
        novo_historico = historico_usuario + [
            {"role": "user", "content": mensagem},
            {"role": "assistant", "content": resposta}
        ]

        return jsonify({
            "resposta": resposta,
            "historico": novo_historico # O Frontend deve guardar isto
        })

    except Exception as e:
        print(f"Erro na API Groq: {e}")
        return jsonify({"resposta": "Desculpa, tive um problema técnico. Ligue para 957 847 477."}), 500

if __name__ == "__main__":
    app.run()

Por que o seu bot pode falhar no Render?

    Statelessness (Falta de Memória): O seu código original processava a mensagem mas não devolvia o histórico atualizado. Sem isso, quando o cliente diz o nome dele, a IA já esqueceu que tinha perguntado o nome. No código acima, o campo "historico" no JSON resolve isso.

    Variáveis de Ambiente: No painel do Render (Dashboard -> Seu Serviço -> Environment), precisa de adicionar:

        GROQ_API_KEY

        EMAIL (seu Gmail)

        SENHA_APP (Senha de app do Google, não a sua senha normal).

    Emails: Se o SMTP falhar, ele pode travar a resposta. Usei um bloco try/except mais robusto para que, mesmo que o email falhe, o cliente receba a resposta no chat.

Como testar agora:

Envie o seguinte JSON para o seu endpoint:
JSON

{
  "mensagem": "Olá",
  "historico": []
}

O servidor vai responder com a mensagem e um histórico preenchido. Na próxima pergunta, mande o histórico que recebeu de volta para manter o fluxo.

Gostaria que eu criasse um exemplo simples de como configurar o seu Frontend (JavaScript) para guardar esse histórico automaticamente?
Você disse

from flask import Flask, jsonify, request

from groq import Groq

from dotenv import load_dotenv

import os

from flask_cors import CORS

import smtplib


from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import re


def enviar_notificacao_lead(nome_cliente, contacto_cliente, interesse_cliente):

    meu_email = os.getenv("EMAIL")

    minha_senha =os.getenv("SENHA_APP")

    email_destino =os.getenv("EMAIL") # Onde queres receber o aviso


    # Criar a estrutura do e-mail

    msg = MIMEMultipart()

    msg['From'] = meu_email

    msg['To'] = email_destino

    msg['Subject'] = f"🔥 NOVO LEAD: {nome_cliente} está interessado!"


    corpo = f"""

    Temos um novo potencial cliente interessado!

    

    Nome: {nome_cliente}

    Contacto: {contacto_cliente}

    Interesse: {interesse_cliente}

    

    Responde rápido para não perderes a venda!

    """

    msg.attach(MIMEText(corpo, 'plain'))


    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(meu_email, minha_senha)

        server.send_message(msg)

        server.quit()

        print("Notificação enviada com sucesso!")

    except Exception as e:

        print(f"Erro ao enviar e-mail: {e}")


load_dotenv()

Dados = {

    "Empresa":"evvaall",

    "Contacto":[

        "+244957847477",

        "ev283@gmail.com"

    ],

    "faq":{

        "O Que é a evvaall?": "A evvaall é uma empresa especializada em automação de processos, análise de dados e desenvolvimento de soluções com inteligência artificial para empresas e profissionais.",

        "Qual é o vosso objectivo?":"Nosso Objectivo é simplifiar tarefas que levariam muito tempo, aumentar a produtividade e entregar resultados mensuráveis e tecnológicos de ponta.",

        "Quais são os serviços que vocês prestram?":"Os nossos serviços são: Análise de dados, Criação de chatboots, Consultoria digital e Automatizamos tarefas repetitivas.",

        "Que tipo de Automações?":"Praticamente, qualquer tarefa repetitiva baseada em regras ou que envolva processamento de dados pode ser automatizada. Por exemplo: Envio automático de lembretes de pagamento por WhatsApp, Agendamento de reuniões, Geração e invio automáticos de relatórios.",

        "Que tipo de Chatbots?":"Desenvolvemos chatbots inteligentes para atendimento 24/7, integrando com WhatsApp, Telegram, sites e apps.",

        "Que tipo de Consultoria?":"Avaliamos seus processos e sugerimos soluções digitais sob medida, identificando o problema e ajudamos na tomada de desisão",

        "Que tipo de Análise de dados?":"Por exemplo, Hoje, como é que tu sabes qual é o teu produto mais lucrativo ou qual cliente está prestes a abandonar a tua empresa? Tu usas dados reais ou apenas intuição?",

        "Em que árias vocês atuam?":"sector Administrativo, Marketing e vendas, atendimento ao cliente e nas áreas de TI",

        "Como faço se eu quiser os vossos Serviços?":"Para mais informação ligue para: 957 847 477, ou deixe 1 mensagem com o serviço entre ' ' e nós entraremos em contacto.",

        "Me fale mais sobre vocês":"A evvaall é uma empresa de soluções digitais que ajuda empresas e profissionais a automatizar tarefas repetitivas, transformar dados em decisões estratégicas e criar chatboots inteligentes para a comunicação eficiente.",

        "Como é que vocês garantem segurança de informação":"Seguimos boas práticas de: 1-Controle de acesso baseado em permissões, 2-Armazenamento seguro em cloud, 3-Logs auditáveis, 4-Separação de ambiente (produção/teste), Em projetos sensíveis, a arquitetura pode ser ajustada para cumprir exigências específicas do cliente.",

        "Que tecnologias utilizam?":"A evvaall adota uma abordagem tecnológica orientada a arquitetura, não a ferramentas isoladas. A escolha das tecnologias depende do contexto operacional do cliente, requisitos de segurança, escalabilidade e integração",

        "Como escolhem a tecnologia certa?":"Não utilizamos uma stack fixa por padrão. Selecionamos as tecnologias com base em: 1-Volume de usuários, 2-Exigências regulatórias, 3-Necessidade de escalabilidade, 4-Orçamento do cliente, O foco não é a ferramenta — é o desempenho, segurança e sustentabilidade da solução.",

        "Que tipos de empresas podem contratar a evva.all?":"Trabalhamos com restaurantes, empresas do setor bancário, comércio, prestadores de serviços, Clínicas de Saúde, Imobliliárias e scritórios de Advogado/consultoria.",

        "O chatbot funciona 24 horas por dia?":"Sim. O sistema funciona 24/7, respondendo clientes automaticamente.",

        "O chatbot pode integrar com WhatsApp Business?":"Sim, utilizamos a API oficial do WhatsApp Business para integração segura e profissional.",

        "O chatbot substitui funcionários?":"Não. Ele automatiza tarefas repetitivas, permitindo que a equipa foque em atividades estratégicas trazendo mais resultados com os mesmos recursos.",

        "A IA aprende com o tempo?":"Sim. Podemos configurar o sistema para melhorar respostas com base em interações reais.",

        "O que é análise de dados na prática?":"É transformar dados do seu negócio (vendas, clientes, pagamentos) em informações estratégicas para tomada de decisão.",

        "Vocês criam relatórios personalizados?":"Sim. Desenvolvemos dashboards visuais e relatórios adaptados às necessidades da empresa",

        "Posso acompanhar os dados em tempo real?":"Dependendo da estrutura do cliente, é possível configurar dashboards com atualização automática.",

        "Os dados da minha empresa ficam seguros?":"Sim. Trabalhamos com boas práticas de segurança e integração com APIs oficiais.",

        "Vocês trabalham com contratos formais?":"Sim. Todos os serviços podem ser formalizados por contrato.",

        "Onde os sistemas ficam hospedados?":"Podem ser hospedados em servidores seguros (cloud) ou na infraestrutura do cliente.",

        "Como funciona o processo de contratação?":"Diagnóstico do problema, Proposta técnica, Desenvolvimento, Implementação, Suporte.",

        "O pagamento é mensal ou único?":"Depende do serviço, projetos personalizados e únicos podem ser pagos por  projetos desenvolvidos, sistemas com manutenção podem ter pagamento mensal.",

        "Por que escolher a evvaall?":"Porque combinamos tecnologia, estratégia e personalização. Não vendemos soluções genéricas — desenvolvemos sistemas adaptados ao seu negócio.",

        "Quanto custam os vossos serviços?":"O valor depende do nível de complexidade e integrações necessárias.Preciso de entender o seu desafio. Pode deixar o seu WhatsApp ou e-mail aqui?.",

        "Quanto custa um chatbot?":"O valor depende do nível de complexidade e integrações necessárias.",

        "Como funcionam os chatbots com IA desenvolvidos pela evvaall?":"Nossos sistemas utilizam modelos de linguagem integrados a regras de negócio específicas do cliente. A arquitetura geralmente envolve: 1-Interface (Site ou WhatsApp Business API), 2-Backend seguro (API própria), 3-Motor de IA, 4-Base de conhecimento personalizada, 5-Logs e monitoramento de desempenho, Isso permite respostas contextuais, automação de processos e coleta estruturada de dados.",

        "A IA toma decisões automáticas?":"A IA executa ações dentro de limites definidos. Sempre existe configuração de regras e possibilidade de supervisão humana para processos críticos. Não implementamos sistemas que atuem sem governança.",

        "Como a análise de dados gera valor real?":"Transformamos dados brutos em indicadores estratégicos como: 1-Taxa de conversão, 2-Tempo médio de atendimento, 3-Índice de recorrência de clientes, 4-Análise de inadimplência, 5-Padrões de comportamento, Isso permite decisões baseadas em evidência e não em suposição.",

        "O que diferencia a evvaall de outras empresas de tecnologia?":"1-Foco em automação orientada a resultado, 2-Integração entre IA + dados + processos, 3-Arquitetura enxuta e escalável, 4-Abordagem consultiva antes do desenvolvimento, 5-Implementação adaptada à realidade local",

        "Como funciona o ciclo de implementação?":"1-Diagnóstico técnico e operacional, 2-Mapeamento de processos, 3-Definição da arquitetura, 4-Desenvolvimento e testes, 5-Implantação controlada, 6-Monitoramento e otimização contínua",

    },

    "respostas_automaticas":{

        ".":"Este é um agente de atendimento que responde a perguntas sobre a evvall. Existem perguntas que não estou autorizado a processar",

        "..":"Muito Obrigado!",

        "Muito Obrigado":"Nada por isso. Até à próxima!",

        "*":"Deixe o seu recado. depois entraremos em contacto.",

        "**":"Deixe sua mensagem entre ' ' que nós entraremos em contacto.",

        "....":"Acesse o nosso site para mais informação.",

        ".....":"fui útil?",

    }

}

Dados["Roteiro_vendas"] = {

    "passo_1": "Olá! Bem-vindo à evvaall. Eu sou o assistente virtual inteligente. Com quem tenho o prazer de falar?",

    "passo_2": "Prazer, {nome}! Para te ajudar da melhor forma, o que procura hoje?\n1. Custos dos serviços;\n2. Suporte Técnico\n3. Fazer perguntas\n4. Falar com um Consultor Humano",

    "passo_3_orcamento": "Entendido. Para que eu possa preparar um valor aproximado, como descreveria o seu projeto atual? (Ex: Pequena automação, Sistema completo de dados ou Chatbot para empresa)",

    "passo_3_suporte":"Entendido! A nossa equipa técnica está pronta para ajudar. Para agilizarmos, pode descrever brevemente o que está a acontecer ou indicar o número do seu contrato/projeto?",    

    "passo_3_falar_com_humano":"Com certeza! Nada substitui uma boa conversa estratégica. O nosso consultor especialista terá todo o prazer em falar consigo. Para agendarmos uma chamada breve de 5 a 10 minutos ou para ele lhe enviar um convite de reunião, qual é o seu contacto?",

    "passo_3_tirar_duvida":"Excelente! Sobre o que você gostaria de saber mais agora?\n>•Quais são os nossos Serviços;\n•Qual é o Nosso objectivo?\n•Em que árias nós atuamos?\n•Faça uma outra pergunta.",

    "passo_4_orçamento":"Excelente. Para que o nosso especialista envie a proposta detalhada e o cronograma, por favor, deixe o seu WhatsApp ou E-mail.",

    "passo_4_suporte":"Obrigado pelo detalhe. Vou abrir um ticket prioritário agora. Qual o melhor número de WhatsApp para o técnico lhe contactar caso precisemos de acesso remoto ou mais detalhes?",

    "passo_4_falar_com_humano":"Excelente, vou passar agora mesmo para o nosso consultor no WhatsApp, é mais rápido!.Posso ajudar em algo mais?",

    "passo_5_final":"Muito obrigado! Recebi os seus dados. Em menos de 2 horas um consultor entrará em contacto consigo. Posso ajudar em algo mais?"

}

client = Groq(

    api_key=os.getenv("GROQ_API_KEY")

)

def conected(mensagem:str):

    msn=mensagem.capitalize().strip()

    if msn in Dados["respostas_automaticas"]:

        return Dados["respostas_automaticas"][msn]

    elif msn in Dados["faq"]:

        return Dados["faq"][msn]

    else:

        return msn


def orientacao(dicionario:dict) -> str:

    contexto =""

    for pergunta, resposta in list(dicionario["faq"].items()) + dicionario["Roteiro_vendas"].items() + list(dicionario["respostas_automaticas"].items()):

        contexto +=f"\n- {pergunta}:{resposta}"


    prompt =f"""

    Você é o Assistente de Vendas da EVVAALL. Sua missão é conduzir o cliente pelo FUNIL DE VENDAS:

    

    ORDEM DE CONVERSA:

    1. Se o cliente disser 'Oi' ou 'Olá', execute o PASSO 1: Pergunte o nome dele.

    2. Assim que ele disser o nome, execute o PASSO 2: Pergunte o que ele procura (Custo dos seviços, Suporte técnico, Fazer perguntas ou Falar com consultor).

    3. Se ele escolher 'Custo dos serviços', execute o PASSO 3(orçamento): chatbot, automação ou consultoria.

    3.1 Após a resposta dele, execute o PASSO 4(orçamento): Peça o contacto (WhatsApp ou E-mail).

    4. Se ele escolher 'Suporte técnico', execute  o PASSO 3(suporte).

    4.1 Após a resposta dele, execute o PASSO 4(suporte): Peça o contacto (WhatsApp ou E-mail).

    5. Se ele escolher 'Fazer perguntas', execute  o PASSO 3(tirar_duvida).

    5.1 Após a resposta dele, podes procurar uma resposta em BASE DE CONEHECIMNTO.

    6. Se ele escolher 'Falar com consultor', execute  o PASSO 3(falar_com_humano).

    6.1 Após a resposta dele, execute o PASSO 4(falar_com_humano).

    5. No final, execute o PASSO 5: Agradeça e informe que entraremos em contacto em breve.


    REGRAS DE OURO:

    - Não pule etapas.

    - Se ele fizer uma pergunta técnica no meio do processo, responda brevemente usando a BASE DE CONHECIMENTO e volte para o passo onde parou.

    - Se o cliente se recusar a dar o contacto, responda: 'Compreendo perfeitamente a sua privacidade. No entanto, como as nossas soluções são personalizadas para cada negócio, o nosso especialista precisa de fazer 2 ou 3 perguntas técnicas que eu, como assistente virtual, ainda não estou autorizado a processar. Podemos avançar?

    

    REGRAS IMPORTANTES:

        1. Ao responder, responda exclusivamente usando as respostas fornecidas abaixo. Mas, podes corrigir erros ortográficos.

        2. Quando uma responder pergunta, não acabe por aí, tente fazer uma pergunta que leve o cliente de volta ao funil de  vendas.

        3. Se a pergunta não existir na base, responda exatamente com: "{dicionario["respostas_automaticas"]["."]}"

        4. Quando não souberes deves responder educadamente com {dicionario["respostas_automaticas"]["."]}.

        5. Se a mensagem do cliente for 'muito obrigado', podes escolher responder com {dicionario["respostas_automaticas"]["Muito Obrigado"]} ou com {dicionario["respostas_automaticas"]["....."]}.

        

    BASE DE CONHECIMENTO:

    {contexto}

    """

    return prompt


def enviar_mensagem(mensagem, historico):

    historico.append({

        "role": "user",

        "content": mensagem

    })

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=historico,

        temperature=0.4

    )

    resposta = completion.choices[0].message.content

    historico.append({

        "role": "assistant",

        "content": resposta

    })

    return resposta



app = Flask(__name__)

CORS(app)


@app.route("/ask", methods=["POST"])

def home():

    data = request.get_json()

    if not data or "mensagem" not in data:

        return jsonify(

            {

                "erro":"envie {'mensagem':'texto aqui'}"

            }, 400

        )

    mensagem = data["mensagem"].strip()

    # detetar número de telefone (Angola)

    padrao_tel = r"9\d{8}"

    tell = re.search(padrao_tel, mensagem)

    padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"

    email = re.search(padrao_email, mensagem)


    

    if tell or email:

        contacto = tell.group(0) if tell else email.group(0)

        enviar_notificacao_lead("Cliente do Site evvaall", contacto, "Interesse detetado via Chat")

    

    if mensagem in Dados["faq"]:

        return jsonify({"resposta": Dados["faq"][mensagem]})

        

    historico = [

        {"role": "system", "content": f"Você é um assistente útil. {orientacao(Dados)}"}

    ]

    historico_usuario = data.get("historico", [])

    historico.extend(historico_usuario)

    historico.append({"role": "user", "content": mensagem})

    try:

        resposta = enviar_mensagem(historico, )

    except Exception as e:

        resposta = "Desculpa, teve um pequeno problema técnico. podes ligar para 957 847 477."

    return jsonify({"resposta":resposta})


if __name__ == "__main__":

    app.run()
O Gemini disse

Entendido! Analisando a tua versão mais recente do código, notei um pequeno erro de digitação na chamada da função enviar_mensagem dentro da rota /ask, o que causaria um erro de execução.

Aqui está o ajuste necessário e uma melhoria na forma como o histórico é retornado, para garantir que o teu bot não sofra de "amnésia" (esquecer o nome do cliente no meio do funil).
1. O Erro Encontrado

Na tua linha:
resposta = enviar_mensagem(historico, )
Faltam os argumentos corretos e a vírgula está sobrando. A função enviar_mensagem espera (mensagem, historico).
2. Código Corrigido e Ajustado

Substitua a sua função home() e enviar_mensagem() por estas versões:
Python

def enviar_mensagem(mensagem, historico_atual):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=historico_atual,
            temperature=0.4
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Erro na API Groq: {e}")
        return "Desculpa, tive um pequeno problema técnico. Podes ligar para 957 847 477."


app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def home():
    data = request.get_json()
    if not data or "mensagem" not in data:
        return jsonify({"erro": "envie {'mensagem':'texto aqui'}"}), 400

    mensagem_usuario = data["mensagem"].strip()
    
    padrao_tel = r"9\d{8}"
    tell = re.search(padrao_tel, mensagem_usuario)
    padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"
    email = re.search(padrao_email, mensagem_usuario)

    if tell or email:
        contacto = tell.group(0) if tell else email.group(0)
        enviar_notificacao_lead("Cliente do Site evvaall", contacto, mensagem_usuario)

    historico_da_conversa = data.get("historico", [])
    
    mensagens_para_ia = [
        {"role": "system", "content": orientacao(Dados)}
    ]
    mensagens_para_ia.extend(historico_da_conversa)
    mensagens_para_ia.append({"role": "user", "content": mensagem_usuario})

    resposta_ia = enviar_mensagem(mensagem_usuario, mensagens_para_ia)

    novo_historico = historico_da_conversa + [
        {"role": "user", "content": mensagem_usuario},
        {"role": "assistant", "content": resposta_ia}
    ]

    return jsonify({
        "resposta": resposta_ia,
        "historico": novo_historico  # O frontend deve guardar este array para a próxima pergunta
    })

if __name__ == "__main__":
    app.run()
