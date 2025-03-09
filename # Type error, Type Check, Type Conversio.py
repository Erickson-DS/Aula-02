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
num1 = float(input("Digite o primeiro número flutuante: "))
num2 = float(input("Digite o segundo número flutuante: "))
media = (num1 + num2) / 2
print("A média é:", media)

#8
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

#13
frase = input("Insira  uma frase :")
print(frase.strip())

#14
data_usuario = input("Insira uam data no formato dd/mm/aaaa :")
data_separada = data_usuario.split("/")

print(f"A data completa foi {data_separada}")
print(f"O Dia é {data_separada[0]}")
print(f"O Mês é {data_separada[1]}")
print(f"O Ano é {data_separada[2]}")

#### outra opção
data = "01/01/2024"  # Exemplo de entrada
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

#15
nome = input("Insira seu nome :")
sobrenome = input("Insira seu sobrenome :")
print(nome + sobrenome)

Booleanos

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas."
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)


# 17. 
# Exemplo de entrada
valor1 = True
valor2 = False
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18. 
# Exemplo de entrada
valor1 = False
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. 

# Exemplo de entrada
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20. 
num1 = 5
num2 = 5
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)

# #### try-except e if 
# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")

# 22: 
entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: 
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")


# 24: 


try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")


# 25: Conversão de Tipo com Validação

# Exemplos que causa TypeError

try:
    resultado = len(8)  #len funciona apenas com String
    print(resultado)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro (quando há erro)
else:
    print("Printa se a condição Try der certo")
finally:
    print("Printa independente do resultado")

#outro exemplo de Try except
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")

# Exemplo que causa TypeCheck

numero = 10
if isinstance(numero, int):   # isinstance verifica o tipo de uma variável  
    print("A variável é um inteiro.")   
else:
    print("A variável não é um inteiro.")

#Type Conversion  #converte o tipo
numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5

Exemplo de IF, Elif e Else

idade = 20
if idade < 18:    #Se algo ocorrer e for True o bloco identado será rodado
    print("Menor de idade")
elif idade == 18: #senão se, Se o primeiro blobo não atende ao critério, avaliará esse bloco.
    print("Exatamente 18 anos")
else:             #Senão, se nenhum bloco atender os critério, o que está identado neste bloco será rodado
    print("Maior de idade")
"""


entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")


