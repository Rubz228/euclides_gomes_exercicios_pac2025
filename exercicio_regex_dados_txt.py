import re

with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()


print(conteudo)


emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', conteudo)
print(emails)


telemoveis = re.findall(r'\d{3}[-\s]?\d{3}[-\s]?\d{3}', conteudo)
print(telemoveis)


nomes = re.findall(r'Nome:\s*(.*?),', conteudo)
print(nomes)


with open('extraidos.txt', 'w', encoding='utf-8') as f:
    for n, e, t in zip(nomes, emails, telemoveis):
        f.write(f"{n} | {e} | {t}\n")


emails_pt = [e for e in emails if e.endswith('.pt')]
print(emails_pt)