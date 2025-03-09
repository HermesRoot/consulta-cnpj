from flask import Flask, request, jsonify
import requests
import re
from flask_cors import CORS  # Importa o CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Função para validar o formato do CNPJ (apenas números e 14 dígitos)
def validar_cnpj(cnpj):
    return bool(re.match(r"^\d{14}$", cnpj))  # Verifica se o CNPJ tem 14 dígitos numéricos

# Rota para consultar o CNPJ
@app.route("/consulta-cnpj", methods=["GET"])
def consulta_cnpj():
    cnpj = request.args.get("cnpj")
    
    if not cnpj:
        return jsonify({"erro": "O parâmetro 'cnpj' é obrigatório."}), 400
    
    if not validar_cnpj(cnpj):
        return jsonify({"erro": "CNPJ inválido. O CNPJ deve ter 14 dígitos."}), 400

    try:
        response = requests.get(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")
        response.raise_for_status()  # Lança um erro se a resposta for ruim (não 2xx)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": "Erro ao consultar o CNPJ.", "detalhes": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
