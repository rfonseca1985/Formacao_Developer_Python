"""
Este código cria uma API usando o FastAPI, um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6+ baseado nos padrões para APIs HTTP.

A API tem uma única rota, a rota raiz (“/”), que é acessada através do método GET. Quando um cliente faz uma solicitação GET para a rota raiz, a função read_root é chamada.

A função read_root faz o seguinte:

Carrega uma planilha Excel em um DataFrame do pandas. O pandas é uma biblioteca de manipulação e análise de dados em Python.
Converte o DataFrame em JSON usando o método to_json do pandas. O parâmetro orient='records' significa que o JSON resultante será uma lista de registros, onde cada registro é um dicionário
com pares de chave-valor correspondendo a cada coluna e valor da linha na planilha.
Retorna o JSON resultante como resposta à solicitação GET. O código também usa o ngrok para expor a API ao público. O ngrok é uma ferramenta que cria um túnel seguro para o localhost,
permitindo que você exponha seu servidor local à internet. Isso é útil para testar a API em um ambiente de produção simulado.
A função run faz o seguinte:
Conecta-se ao ngrok na porta 8000. Imprime o URL público do túnel ngrok. Inicia o servidor FastAPI na porta 8000.
Portanto, a funcionalidade principal desta API é ler uma planilha Excel, convertê-la em JSON e retornar o JSON quando a rota raiz é acessada via GET.
A API é exposta ao público através do ngrok.

"""

from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import pandas as pd


ngrok.set_auth_token("<SEU TOKEN AQUI>")

app = FastAPI()



@app.get("/")
def read_root():
    # Carrega a planilha em um DataFrame do pandas
    df = pd.read_excel('/home/rf0n53c485/Projetos/Dio/FormacaoPython/Criando uma API com Flask no Ambiente COLAB/Planilha.xlsx')

    # Converte o DataFrame em JSON
    result = df.to_json(orient="records")

    return result

def run():
    ngrok_tunnel = ngrok.connect(8000)
    print('URL Pública:', ngrok_tunnel.public_url)
    nest_asyncio.apply()
    uvicorn.run(app, host='127.0.0.1', port=8000)

run()
