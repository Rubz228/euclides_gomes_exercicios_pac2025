#---------Exercicio1----------------
segundos = int(input("\nIndica a quantidade de segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
resto_segundos = resto % 60


print(f"\n{horas} hora(s), {minutos} minuto(s) e {resto_segundos} segundo(s)")

#---------Exercicio2----------------

num1 = int(input("\nEscreve o primeiro número: "))
num2 = int(input("Escreve o segundo número: "))
num3 = int(input("Escreve o terceiro número: "))


if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3


if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"\nMaior: {maior}")
print(f"Menor: {menor}")

#---------Exercicio3----------------

num1 = int(input("\nEscolhe o primeiro número: "))
num2 = int(input("Escolhe o segundo número: "))

if num1 < num2:
    print(f"\nCrescente: {num1}, {num2}")
    print(f"Decrescente: {num2}, {num1}")
else:
    print(f"\nCrescente: {num2}, {num1}")
    print(f"Decrescente: {num1}, {num2}")

#---------Exercicio5----------------

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3


if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3


if (num1 != maior and num1 != menor):
    meio = num1
elif (num2 != maior and num2 != menor):
    meio = num2
else:
    meio = num3

print(f"\nCrescente: {menor}, {meio}, {maior}")
print(f"Decrescente: {maior}, {meio}, {menor}")


#---------Exercicio7----------------

nota1 = float(input("\nDigite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"\nMédia: {media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
