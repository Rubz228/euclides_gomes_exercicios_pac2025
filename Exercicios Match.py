#-----------------------------Exercicio1----------------------------    
opc = input("Escolha um dia da semana:\n"
            "Segunda - dia útil\n"
            "Terça - dia útil\n"
            "Quarta - dia útil\n"
            "Quinta - dia útil\n"
            "Sexta - dia útil\n"
            "Sábado - Fim de semana\n"
            "Domingo - Fim de semana\n"
            "Diz o dia da semana: ")
match opc:

    case "Segunda":
        print("dia util\n")
    case "Terça":
        print("dia util\n")
    case "Quarta":
        print("dia util\n")
    case "Quinta":
        print("dia util\n")
    case "Sexta":
        print("dia util\n")
    case "Sábado":
        print("Fim de semana\n")
    case "Domingo":
        print("Fim de semana\n")
    case _:
        print("Opção não existe\n")

#-----------------------------Exercicio2----------------------------   

Nota=input("Excelente- 90 ou >\n"
           "Bom- 70-89\n"
           "Sufciente- 50-69\n"
           "Insufciente- <50\n"
           "Escolha a nota:")

match Nota:

    case "Excelente":
        print("90 ou >")
    case "Bom":
        print("70-89")
    case "Sufciente":
        print("50-69")
    case "Insufciente":
        print("<50")
    case _:
        print("Opção não existe")

#-----------------------------Exercicio3----------------------------   

transaçao = input("\nEscolhe a transação: ")
valor = int(input("\nEscreve o valor: \n"))

pedido = {"tipo": transaçao, "valor": valor}

match pedido["tipo"]:
    case "compra":
        print("Compra de\n", pedido["valor"],)
    case "venda":
        print("Venda de\n", pedido["valor"],)
    case _:
        print("Pedido desconhecido\n")

#-----------------------------Exercicio5----------------------------   

msg = input("Digite uma mensagem:\n"
            "olá - Saudação\n"
            "bom dia - Saudação\n"
            "tchau - Despedida\n"
            "adeus - Despedida\n"
            "És quem? - Pergunta\n"
            "Diz a mensagem: ")

match msg:
    case "ola":
        print("Saudação")
    case "bom dia":
        print("Saudação")
    case "tchau":
        print("Despedida")
    case "adeus":
        print("Despedida")
    case _ if msg.endswith("?"):
        print("Pergunta")
    case _:
        print("Mensagem genérica")
    
#-----------------------------Exercicio6----------------------------  

status = input("Diz o status do servidor (ok ou erro): ")
tempo = int(input("Diz o tempo de resposta (em ms): "))

dados = {"status": status, "tempo_resposta": tempo}

match dados:
    case {"status": "ok", "tempo_resposta": tempo} if tempo > 200:
        print("Servidor lento")
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "erro"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")

#-----------------------------Exercicio7---------------------------- 

categoria = input("Escolhe a categoria do produto (eletronico ou alimento): ")
preco = int(input("Digite o preço do produto: "))

dados = {"categoria": categoria, "preco": preco}

match dados:
    case {"categoria": "eletronico", "preco": preco} if preco > 1000:
        print("Produto de luxo")
    case {"categoria": "eletronico", "preco": preco} if preco <= 1000:
        print("Produto comum")
    case {"categoria": "alimento"}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")

#-----------------------------Exercicio8---------------------------- 

op = input("Digite a operação (soma, subtrai, multiplica, divide): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match op:
    case "soma":
        print(num1 + num2)
    case "subtrai":
        print(num1 - num2)
    case "multiplica":
        print(num1 * num2)
    case "divide":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Erro: divisão por zero!")
    case _:
        print("Operação inválida!")