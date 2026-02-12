from flask import Flask, jsonify, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
Dados = {
    "Empresa":"Evaall",
    "Contacto":[
        "+244957847477",
        "ev283@gmail.com"
    ],
    "faq":{
        "O Que é a evaall?": "A evva.all é uma empresa especializada em automação de processos, análise de dados e desenvolvimento de soluções com inteligência artificial para empresas e profissionais.",
        "Qual é o vosso objectivo?":"Nosso Objectivo é simplifiar tarefas que levariam muito tempo, aumentar a produtividade e entregar resultados mensuráveis e tecnológicos de ponta.",
        "Quais são os serviços que vocês prestram?":"Os nossos serviços são: Análise de dados, Criação de chatboots, Consultoria digital e Automatizamos tarefas repetitivas.",
        "Que tipo de Automações?":"Praticamente qualquer tarefa repetitiva, baseada em regras ou que envolva processamento de dados pode ser automatizada. por exemplo: nas árias de marketing  vendas, análise e dados, atendimento ao cliente e no  sector administrativo.",
        "Que tipo de Chatboots?":"Desenvolvemos chatbots inteligentes para atendimento 24/7, integrando WhatsApp, Telegram, sites e apps.",
        "Que tipo de Consultoria?":"Avaliamos seus processos e sugerimos soluções digitais sob medida, identificando o problema e ajudamos na tomada de desisão",
        "Que tipo de Análise de dados?":"por exemplo, uma empresa pode analisar dados históricos para prever vendas, demanda, comportamento do cliente ou até riscos; uma loja pode analisar quais produtos vendem mais e ajustar o estoque ou promoções.",
        "Em que árias vocês atuam?":"sector Administrativo, Marketing e vendas, atendimento ao cliente e nas áreas de TI",
        "Como faço para se eu quiser os vossos Serviços?":"Para mais informação ligue para: 957 847 477, ou deixe 1 mensagem com o serviço entre ' ' e nós entraremos em contacto.",
        "Me fale mais sobre vocês":"A evva.all é uma empresa de soluções digitais que ajuda empresas e profissionais a automatizar tarefas repetitivas, transformar dados em decisões estratégicas e criar chatboots inteligentes para a comunicação eficiente.",
        "Como é que vocês garantem segurança de informação":"Seguimos boas práticas de: 1-Controle de acesso baseado em permissões, 2-Armazenamento seguro em cloud, 3-Logs auditáveis, 4-Separação de ambiente (produção/teste), Em projetos sensíveis, a arquitetura pode ser ajustada para cumprir exigências específicas do cliente.",
        "Que tecnologias utilizam?":"A evvaall adota uma abordagem tecnológica orientada a arquitetura, não a ferramentas isoladas. A escolha das tecnologias depende do contexto operacional do cliente, requisitos de segurança, escalabilidade e integração",
        "Como escolhem a tecnologia certa?":"Não utilizamos uma stack fixa por padrão. Selecionamos as tecnologias com base em: 1-Volume de usuários, 2-Exigências regulatórias, 3-Necessidade de escalabilidade, 4-Orçamento do cliente, O foco não é a ferramenta — é o desempenho, segurança e sustentabilidade da solução.",
        "Que tipos de empresas podem contratar a evva.all?":"Trabalhamos com restaurantes, empresas do setor bancário, comércio, prestadores de serviços e qualquer negócio que queira automatizar processos ou usar dados de forma estratégica ou criar chatboot para atendimnto automático.",
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
        "Quanto custa um serviço de análise de dados?":"O valor depende do nível de complexidade e integrações necessárias.",
        "Quanto custa um ....?":"O valor depende do nível de complexidade e integrações necessárias.",
        "Quanto custa um chatbot?":"O valor depende do nível de complexidade e integrações necessárias.",
        "Como funcionam os chatbots com IA desenvolvidos pela evvaall?":"Nossos sistemas utilizam modelos de linguagem integrados a regras de negócio específicas do cliente. A arquitetura geralmente envolve: 1-Interface (Site ou WhatsApp Business API), 2-Backend seguro (API própria), 3-Motor de IA, 4-Base de conhecimento personalizada, 5-Logs e monitoramento de desempenho, Isso permite respostas contextuais, automação de processos e coleta estruturada de dados.",
        "A IA toma decisões automáticas?":"A IA executa ações dentro de limites definidos. Sempre existe configuração de regras e possibilidade de supervisão humana para processos críticos. Não implementamos sistemas que atuem sem governança.",
        "Como a análise de dados gera valor real?":"Transformamos dados brutos em indicadores estratégicos como: 1-Taxa de conversão, 2-Tempo médio de atendimento, 3-Índice de recorrência de clientes, 4-Análise de inadimplência, 5-Padrões de comportamento, Isso permite decisões baseadas em evidência e não em suposição.",
        "O que diferencia a evvaall de outras empresas de tecnologia?":"1-Foco em automação orientada a resultado, 2-Integração entre IA + dados + processos, 3-Arquitetura enxuta e escalável, 4-Abordagem consultiva antes do desenvolvimento, 5-Implementação adaptada à realidade local",
        "Como funciona o ciclo de implementação?":"1-Diagnóstico técnico e operacional, 2-Mapeamento de processos, 3-Definição da arquitetura, 4-Desenvolvimento e testes, 5-Implantação controlada, 6-Monitoramento e otimização contínua",
    },
    "respostas_automaticas":{
        "Oi":"Oi, Como posso ajudar?",
        "Olá":"Olá, Como posso ajudar?",
        ".":"Este é um agente de atendimento que responde apénas perguntas sobre a Evvall.",
        "..":"Muito Obrigado!",
        "Muito Obrigado":"Nada por isso. Até à próxima!",
        "*":"Deixe o seu recado. depois entraremos em contacto.",
        "**":"Deixe sua mensagem entre ' ' que nós entraremos em contacto.",
        "***":"Deixe uma pergunta entre ' ' que nós entraremos em contacto.",
        "...":"Nada por isso. Oque mais gostou?",
        "....":"Acesse o nosso site para mais informação.",
        ".....":"fui útil?",
    }
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

def orientacao(diconario:dict) -> str:
    contexto =""
    for pergunta, resposta in list(diconario["faq"].items()) + list(diconario["respostas_automaticas"].items()):
        contexto +=f"\n- {pergunta}:{resposta}"

    prompt =f"""
    Você é um agente oficial da empresa Evaall.

    REGRAS IMPORTANTES:
        1. Responda exclusivamente usando as respostas fornecidas abaixo.
        2. Se a pergunta não existir na base, responda exatamente com:
        "{diconario["respostas_automaticas"]["."]}"
        3. Quando não souberes deves responder educadamente com {diconario["respostas_automaticas"]["."]}.
        4. Se a mensagem do cliente for 'muito obrigado', podes escolher responder com {diconario["respostas_automaticas"]["Muito Obrigado"]} ou com {diconario["respostas_automaticas"]["..."]} ou com {diconario["respostas_automaticas"]["....."]}.
        5. Se a pessoa fizer duas perguntas que você desconhece, podes escolher responder com {diconario["respostas_automaticas"]["**"]} ou com {diconario["respostas_automaticas"]["***"]} ou com {diconario["respostas_automaticas"]["...."]}.
    BASE DE CONHCIMNTO:
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
        temperature=0.7
    )
    resposta = completion.choices[0].message.content
    historico.append({
        "role": "assistant",
        "content": resposta
    })
    return resposta


app = Flask(__name__)

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
    historico = [
        {"role": "system", "content": f"Você é um assistente útil. {orientacao(Dados)}"}
    ]
    resposta = enviar_mensagem(mensagem, historico)
    if mensagem in Dados["faq"]:
        return jsonify({"resposta": Dados["faq"][mensagem]})

    if mensagem in Dados["respostas_automaticas"]:
        return jsonify({"resposta": Dados["respostas_automaticas"][mensagem]})
    
    return jsonify({"resposta":resposta})

if __name__ == "__main__":
    app.run(debug=True)
