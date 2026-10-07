import json
import os

# DEFINE O CAMINHO DA PASTA E DO ARQUIVO
PASTA_DATA = "data"
CAMINHO_JSON = os.path.join(PASTA_DATA, "transacoes.json")

def salvar_transacao_do_app(lista_completa):
    if not os.path.exists(PASTA_DATA):
        os.makedirs(PASTA_DATA)

    with open(CAMINHO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista_completa, arquivo, ensure_ascii=False, indent=4)
        
def carregar_transacoes():
    if os.path.exists(CAMINHO_JSON):
        with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return [
            {"descricao": "Salário", "valor": 3200.00, "tipo": "receita"},
            {"descricao": "Aluguel", "valor": 1200.00, "tipo": "despesa"},
            {"descricao": "Mercado", "valor": 356.72, "tipo": "despesa"},
            {"descricao": "Freela", "valor": 800.00, "tipo": "receita"},
            {"descricao": "Uber", "valor": 27.90, "tipo": "despesa"}
        ]
