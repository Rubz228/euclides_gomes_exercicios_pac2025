#-----------------------------Exercicio1----------------------------    
alunos = []

aluno1 = {
    "nome": input("Nome: "),
    "idade": int(input("Idade: ")),
    "curso": input("Curso: ")
}
alunos.append(aluno1)

print("\n--- Lista de Alunos ---")
for aluno in alunos:
    print(f"nome: {aluno['nome']}")
    print(f"idade: {aluno['idade']}")
    print(f"curso: {aluno['curso']}")

#-----------------------------Exercicio2----------------------------    

carro = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}

print(carro['modelo'])

#-----------------------------Exercicio3----------------------------    

produto = {}

produto['nome'] = "Telemóvel"
produto['preço'] = 1500
produto['stock'] = 30

del produto['stock']

print(produto)

#-----------------------------Exercicio4----------------------------    

utilizador = {'nome': 'Carlos', 'idade': 28}

if 'email' in utilizador:
    print("Email encontrado.")
else:
    print("Email não encontrado.")

#-----------------------------Exercicio5----------------------------    

palavra = input("Introduza uma palavra: ")
contagem = {}

for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)

#-----------------------------Exercicio6----------------------------    

vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}

total_trimestre = sum(vendas.values())

print(f"O total de vendas do trimestre é: {total_trimestre}")

#-----------------------------Exercicio7----------------------------    

d = {'a': 1, 'b': 2, 'c': 3}
d_invertido = {}

for chave, valor in d.items():
    d_invertido[valor] = chave

print(d_invertido)

#-----------------------------Exercicio8----------------------------    

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d3 = d1.copy()
d3.update(d2)

print(d3)

#-----------------------------Exercicio9----------------------------    

notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

for nome, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{nome}: {media:.1f}")

#-----------------------------Exercicio10----------------------------    

frase = input("Introduza uma frase: ")
palavras = frase.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)