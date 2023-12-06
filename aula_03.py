# ESTRUTURAS DE CONTROLE

# Estruturas de Controle de Fluxo Condicional (if, else, elif)

numero = 10

""" if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero") """


# Estruturas de Controle de Fluxo Iterativo (while, for)

# While:

while numero < 20:
    numero += 1
    # print("Número", numero)

# Interrupção do Loop:

contador = 0

while True:  # Loop infinito
    # print('exemplo 1: ', contador)
    contador += 1
    if contador >= 20:
        # print('exemplo 1: ', contador)
        break  # Interrompe o loop quando contador atinge 5


# Continuação para a Próxima Iteração:

contador = 0

while contador < 10:
    contador += 1

    if contador == 3:
        continue  # Pula para a próxima iteração quando contador é igual a 3

    #print('exemplo 2: ', contador)


# For



""" for i in range(5, 10):
    print(i) """

#soma = 0

# for x in range(1, 11):
#     soma += x

# print(f"A soma dos números de 1 a 10 é: {soma}")
# print("A soma dos números de 1 a 10 é:",soma)
