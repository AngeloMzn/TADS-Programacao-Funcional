import json
from collections import defaultdict
from datetime import datetime
from functools import reduce
import pandas as pd

with open('thefuck-sample-100.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def extrair_mes_ano(registro):
    return datetime.strptime(registro['starred_at'], "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m")

def contar_usuarios_por_mes(usuarios_por_mes, registro):
    mes_ano = extrair_mes_ano(registro)
    usuarios_por_mes[mes_ano]['total'] += 1
    if registro['user']['hireable']:
        usuarios_por_mes[mes_ano]['hireable'] += 1
    if registro['user']['email']:
        usuarios_por_mes[mes_ano]['email'] += 1
    if registro['user']['twitter_username']:
        usuarios_por_mes[mes_ano]['twitter'] += 1
    return usuarios_por_mes

usuarios_por_mes = defaultdict(lambda: {'total': 0, 'hireable': 0, 'email': 0, 'twitter': 0})

usuarios_por_mes = reduce(contar_usuarios_por_mes, data, usuarios_por_mes)

df = pd.DataFrame([
    {"Mês/Ano": mes_ano,
     "Total Usuários": contagens['total'],
     "Hireable": contagens['hireable'],
     "Email": contagens['email'],
     "Twitter": contagens['twitter']}
    for mes_ano, contagens in sorted(usuarios_por_mes.items())
])

df.to_csv('resultado_stargazers.csv', index=False)
print("Arquivo CSV gerado com sucesso: resultado_stargazers.csv")
