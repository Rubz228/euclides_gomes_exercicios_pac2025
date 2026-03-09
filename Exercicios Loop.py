#--------------Exercicio 1-----------------

def par_impar():
    for i in range(31):
        if i % 2 == 0:
        
            print(f"{i}:par", end="  ")
        else:
            print(f"{i}:impar", end="  ")

par_impar()

#--------------Exercicio 2-----------------

def par_impar():
    for i in range(10):
        num = int(input("\nDigite um número: "))
        
        if num % 2 == 0:
            print(num, "é par")
        else:
            print(num, "é impar")

par_impar()

#--------------Exercicio 3-----------------

def media():
    soma = 0  
    
    for i in range(1, 11):
        
        nota = float(input(f"Digite a nota do aluno {i}: "))
        soma = soma + nota 
        
    media = soma / 10  
    
    print("A média da turma é:", media)

media()

#--------------Exercicio 4-----------------

def primo():
    num = int(input("Digite um número inteiro: "))
    
    if num <= 1:
        print(num, "não é primo")
    else:
        e_primo = True  
        
        for i in range(2, num):
            if num % i == 0:
                e_primo = False 
                break 
        
        if e_primo:
            print(num, "é um número primo")
        else:
            print(num, "não é um número primo")

primo() 

#--------------Exercicio 5-----------------

def Imprimir():
    for i in range(1, 10001):
        print(i, end=" ")

Imprimir()

#--------------Exercicio 6-----------------

def mostrar_primos():
    lista_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    for p in lista_primos:
        print(p, end=" ")

mostrar_primos()
