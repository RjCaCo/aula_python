# ESTRUTURAS DE CONTROLE

# Estruturas de Controle de Fluxo Condicional (if, else, elif)

""" numero_1 = 20
numero_2 = 10

if numero_1 > numero_2:
    print("numero 1 é maior")
elif numero_1 < numero_2:
    print("Número numero 1 é menor")
else:
    print("iguais") """


# Estruturas de Controle de Fluxo Condicional (switch / case)
    
""" número = int(input("Digite um número entre 1 e 7: "))

if número == 1:
    print("Domingo")
elif número == 2:
    print("Segunda-feira")
elif número == 3:
    print("Terça-feira")
elif número == 4:
    print("Quarta-feira")
elif número == 5:
    print("Quinta-feira")
elif número == 6:
    print("Sexta-feira")
else:
    print("Sábado") """


# Estruturas de Controle de Fluxo Iterativo (while, for)

# While:

""" numero = 10

while numero <= 20:
    print("Número", numero)
    numero += 1 """

# Interrupção do Loop:

contador = 0

""" while True:  # Loop infinito
    print('exemplo 1: ', contador)
    contador += 1
    if contador >= 20:
        print('exemplo 1: ', contador)
        break  # Interrompe o loop quando contador atinge 5 """


# Continuação para a Próxima Iteração:

# contador = 0

""" while contador < 10:
    contador += 1

    if contador == 3:
        continue  # Pula para a próxima iteração quando contador é igual a 3

    print('exemplo 2: ', contador) """


# For

""" for i in range(5, 10):
    print(i) """

""" valor = 0
for x in range(10):
    x += 2
    valor += x
    print(f"x é: {x}")
    print(f"A soma dos números de 1 a 4 é: {valor}")


print(f"final: {valor}") """

valor = 0

for i in range(1, 11, 2):  # usa range com passo de 2 para iterar aos ímpares
    print(f"valor: {valor}")  # usa f-string para formatar
    print(f"i: {i}")
    valor += i

print(f"final: {valor}")  # usa f-string para formatar