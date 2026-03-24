import json
import re

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def validar_nif(nif):
    padrao = r'^[123568]\d{8}$'
    return re.match(padrao, nif) is not None

def validar_telemovel(telemovel):
    apenas_digitos = re.sub(r'\D', '', telemovel)
    return len(apenas_digitos) == 9

registos_validos = []

registos_validos = [
    p for p in dados 
    if validar_email(p['email']) and validar_nif(p['nif']) and validar_telemovel(p['telemovel'])
]

with open('validos.json', 'w', encoding='utf-8') as f:
    json.dump(registos_validos, f, indent=4, ensure_ascii=False)

# Exercício 6: Criar o ficheiro .txt
with open('contactos.txt', 'w', encoding='utf-8') as f:
    for p in dados:
        f.write(f"{p['nome']}: {p['email']}\n")