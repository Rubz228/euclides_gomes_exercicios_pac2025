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