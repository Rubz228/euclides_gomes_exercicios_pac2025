import re 

with open('dados.json','r') as f:
    conteudo = f.read()



padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email_teste = "exemplo@domin"

if re.fullmatch(padrao_email, email_teste):
    print("Email válido!")
else:
    print("Email inválido.")