from flask import Flask, jsonify, request
from groq import Groq
from dotenv import load_dotenv
import os
from flask_cors import CORS
import smtplib
from email.message import EmailMessage


import re
meu_email = os.getenv("EMAIL")
minha_senha = os.getenv("SENHA_APP")
email_destino = os.getenv("EMAIL")

print(meu_email if meu_email else "não consigo me conectar ao email")
print(minha_senha if minha_senha else "senha  inexistente")
def enviar_notificacao_lead(nome_cliente, contacto_cliente, interesse_cliente):
    msg = EmailMessage()
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
    msg.set_content(corpo)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as server:
            server.starttls()
            server.login(meu_email, minha_senha)
            server.send_message(msg)
            print("email enviado")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


load_dotenv()
Dados = {
    "Empresa":"evvaall",
    "Contacto":[
        "+244957847477",
        "evaall283@gmail.com"
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

def orientacao(dicionario:dict) -> str:
    contexto =""
    for pergunta, resposta in list(dicionario["faq"].items()) + list(dicionario["Roteiro_vendas"].items()) + list(dicionario["respostas_automaticas"].items()):
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
    - Não dê respostas mutio grandes.
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
        model="openai/gpt-oss-120b",
        messages=historico,
        temperature=0.4,
    )
    resposta = completion.choices[0].message.content
    historico.append({
        "role": "assistant",
        "content": resposta
    })
    return resposta

sessoes= {}
app = Flask(__name__)

CORS(app)
@app.route("/ask", methods=["POST"])
def home():
    data = request.get_json()
    if not data or "mensagem" not in data:
        return jsonify({
            "erro":"envie {'mensagem':'texto aqui'}"
            }), 400
    
    mensagem = data["mensagem"].strip()
    session_id = data.get("session_id", "default")
    
    print(mensagem)
    padrao_tel = r"\s?9\d{2}\s?\d{3}\s?\d{3}"
    tell = re.search(padrao_tel, mensagem)
    padrao_email = r"[\w\.-]+@[\w\.-]+\.\w+"
    email = re.search(padrao_email, mensagem)    
    if tell or email:
        contacto = tell if tell else email
        enviar_notificacao_lead("Cliente do Site evvaall", contacto, "Interesse detetado via Chat")

    
    
    if session_id not in sessoes:
        sessoes[session_id] = [
            {"role": "system", "content": f"Você é um assistente útil. {orientacao(Dados)}"}
        ]
    
    historico = sessoes[session_id]
    if len(historico) > 10:
        sessoes[session_id] = [historico[0]] + historico[-6:]
    try:
        resposta = enviar_mensagem(mensagem, sessoes[session_id])
    except Exception as e:
        resposta = "Desculpa, teve um pequeno problema técnico. podes ligar para 957 847 477."
    return jsonify({"resposta":resposta})
    
if __name__ == "__main__":
    app.run()

