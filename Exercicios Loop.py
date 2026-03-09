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
