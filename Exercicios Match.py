opc=input("Segunda- dia util , Terça- dia util , Quarta- dia util , Quinta- dia util , Sexta- dia util , Sabado- Fim de semana , Domingo- Fim de semana")

match opc:

    case "Segunda":
        print("dia util")
    case "Terça":
        print("dia util")
    case "Quarta":
        print("dia util")
    case "Quinta":
        print("dia util")
    case "Sexta":
        print("dia util")
    case "Sábado":
        print("Fim de semana")
    case "Domingo":
        print("Fim de semana")
    case _:
        print("Opção não existe")

Nota=input("Excelente- 90 ou > , Bom- 70-89 , Sufciente- 50-69 , Insufciente- <50")

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
    

    