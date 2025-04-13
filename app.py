from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return "test"


@app.route('/chatbot', methods=['GET'])
def chatbot():
    # data = request.json
    # pergunta = data.get('pergunta')
    pergunta = request.args.get('pergunta')
    resposta = gerar_resposta(pergunta)

    #return jsonify({'resposta': resposta})
    return resposta

def gerar_resposta(pergunta):
    prompt = f"""
    Você é um comediante respondendo perguntas do público, com um tom leve, divertido, sarcástico (mas de boa) e muito criativo.
    Sempre inclua:
    - Uma introdução engraçada
    - Uma explicação com analogias bem-humoradas
    - Um final com ar de "boa noite galera!"

    Pergunta do usuário:
    {pergunta}
    Responda com base apenas nas informações acima.
    """

    # url = "https://api.groq.com/openai/v1/chat/completions"
    # headers = {
    #   "Authorization": f"Bearer {GROQ_API_KEY}",
    #   "Content-Type": "application/json"
    # }

    # data = {
    #   "model": "llama3-8b-8192",
    #   "messages": [
    #       {"role": "user", "content": prompt}
    #   ],
    #   "temperature": 0.9,
    #   "max_tokens": 150
    # }

    # response = request.post(url, headers=headers, json=data)
    # resposta = response.json()["choices"][0]["message"]["content"]

    return "Ta aqui sua resposta cuzao"


if __name__ == "__main__":
  app.run(debug=True)