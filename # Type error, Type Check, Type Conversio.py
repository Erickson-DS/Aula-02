"""
Inteiros

#1

#numero1 = int(input("digite o primeiro número: "))
#numero2 = int(input("digite o segundo número: "))

#print( numero1 + numero2)

#2
#numero1 = int(input("digite o primeiro número: "))
#divisao = 5
#print(numero1%divisao)

#3
numero1 = int(input("digite o primeiro número: "))
numero2 = int(input("digite o segundo número: "))
print( numero1 * numero2)

#4 
numero1 = int(input("digite o primeiro número: "))
numero2 = int(input("digite o segundo número: "))

print( numero1 // numero2)


#5
numero1 = int(input("digite o primeiro número: "))
print(numero1 ** 2)


Float

#6
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))

print( numero1 + numero2)

#7
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))

#8
import math
base = int(input("digite a base: "))
potencia = int(input("digite a potencia: "))
print(base**potencia)

#9
cel = float(input("digite a temperatura em celsius: "))
far = cel *1.8 + 32
print(f"{far:.1f}")

#10 Precisa calcular pi
import math
raio_do_circulo = float(input("digite o raio: "))
area_do_circulo = math.pi *raio_do_circulo **2
print(f"{area_do_circulo:.2f}") # Formata a saída da fstring para 2 casa decimais

String

#11
nome = input("Insira seu nome :")
print(nome.upper())

#12
nome = input("Insira seu nome :")
print(nome.lower())

13#
frase = input("Insira  uma frase :")
print(frase.strip())

#14
data_usuario = input("Insira uam data no formato dd/mm/aaaa :")
data_separada = data_usuario.split("/")

print(f"A data completa foi {data_separada}")
print(f"O Dia é {data_separada[0]}")
print(f"O Mês é {data_separada[1]}")
print(f"O Ano é {data_separada[2]}")"""

#15

nome = input("Insira seu nome :")
sobrenome = input("Insira seu sobrenome :")
print(f"{nome} {sobrenome}" )