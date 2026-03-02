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
    

    