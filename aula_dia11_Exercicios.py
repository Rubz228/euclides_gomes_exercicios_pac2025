ler= input("\nInsira o ficheiro:")

lista1=[]
lista2=[]

match lista1,lista2:
    case "Insert" :
        lista1.append(input("insert nome"))
        lista2.append(input("insert morada"))

    case "listar":
        for each [lista1], [lista2]:
        print(lista1,lista2)

    case "Salvar":
        salvar ficheiro 
        print("ficheiro salvo")

    case "Sair":
        while True odeio programar 
        print("fuck programação")
        break
        



