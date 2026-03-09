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

#--------------Exercicio 7-----------------

def contar_dez_em_dez():
    for i in range(10, 1001,10):
        print(i, end=" ")

contar_dez_em_dez()
#--------------Exercicio 8-----------------

def quinze_dez_em_dez():
    for i in range(15, 1001,10):
        print(i, end=" ")
    
    print("\n-------------------------------\n")

    for x in range(10, 1001, 10):
        print(x ,end=" " )

quinze_dez_em_dez()


#--------------Exercicio 9-----------------

def pedir_numero():
    while True:
        num = int(input("Digite um número entre 1 e 100: "))
        
        if 1 <= num <= 100:
            print("Número válido:", num)
            break
        else:
            print("Número inválido! Tente novamente.")

pedir_numero()

#--------------Exercicio 10-----------------

def contar_divisores():
    num = int(input("Digite um número: "))
    total_divisores = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            total_divisores = total_divisores + 1
            
    print("O número", num, "tem", total_divisores, "divisores.")

contar_divisores()


