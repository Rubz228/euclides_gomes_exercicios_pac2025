import requests
from bs4 import BeautifulSoup
import time
import json
from urllib.parse import urljoin


def crawler(url_inicial, max_paginas):
    visitados = set()
    fila = [url_inicial]
    dados = []

    headers = {"User-Agent": "MeuCrawler"}

    while fila and len(visitados) < max_paginas:
        url = fila.pop(0)
        print("A visitar:", url)

        if url in visitados:
            continue

        try:
            resposta = requests.get(url, headers=headers)
            soup = BeautifulSoup(resposta.text, "html.parser")

            titulo = soup.title.string if soup.title else "Sem título"

            links = []

            for a in soup.find_all("a", href=True):
                link = urljoin(url, a["href"])
                links.append(link)

                if link not in visitados:
                    fila.append(link)

            dados.append({
                "url": url,
                "titulo": titulo,
                "links": links
            })

            visitados.add(url)

            time.sleep(1)

        except Exception as e:
            print("Erro ao visitar", url)
            print(e)

    with open("dados.json", "w", encoding="utf-8") as ficheiro:
        json.dump(dados, ficheiro, indent=4, ensure_ascii=False)


crawler("https://example.com", 3)