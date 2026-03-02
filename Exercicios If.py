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


if (num1 != maior and num1 != menor):
    meio = num1
elif (num2 != maior and num2 != menor):
    meio = num2
else:
    meio = num3

print(f"\nCrescente: {menor}, {meio}, {maior}")
print(f"Decrescente: {maior}, {meio}, {menor}")


#---------Exercicio7----------------

nota1 = float(input("\nEscreve a nota do 1º Teste: "))
nota2 = float(input("Escreve a nota do 2º Teste: "))
nota3 = float(input("Escreve a nota do 3ª Teste: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

print(f"\nMédia: {media:.1f}")

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#---------Exercicio8----------------

n1 = float(input("Digite a nota do aluno 1: "))
n2 = float(input("Digite a nota do aluno 2: "))
n3 = float(input("Digite a nota do aluno 3: "))
n4 = float(input("Digite a nota do aluno 4: "))
n5 = float(input("Digite a nota do aluno 5: "))
n6 = float(input("Digite a nota do aluno 6: "))
n7 = float(input("Digite a nota do aluno 7: "))
n8 = float(input("Digite a nota do aluno 8: "))
n9 = float(input("Digite a nota do aluno 9: "))
n10 = float(input("Digite a nota do aluno 10: "))

soma = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
media = soma / 10

acima_media = 0

if n1 >= media:
    acima = acima_media + 1
if n2 >= media:
    acima = acima_media + 1
if n3 >= media:
    acima = acima_media + 1
if n4 >= media:
    acima = acima_media + 1
if n5 >= media:
    acima = acima_media + 1
if n6 >= media:
    acima = acima_media + 1
if n7 >= media:
    acima = acima_media + 1
if n8 >= media:
    acima = acima_media + 1
if n9 >= media:
    acima = acima_media + 1
if n10 >= media:
    acima = acima_media + 1

print(f"\nMédia: {media:.1f}")
print(f"Alunos com nota acima/igual da média: {acima}")
