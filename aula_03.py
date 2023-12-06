# ESTRUTURAS DE CONTROLE

numero = 10

""" if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero") """


""" while numero < 20:
    numero += 1
    print("Número", numero) """

soma = 0

for x in range(1, 11):
    soma += x

""" print(f"A soma dos números de 1 a 10 é: {soma}")
print("A soma dos números de 1 a 10 é:",soma) """


# Estruturas de Controle de Fluxo Iterativo (while, for)

# break - Interrupção do Loop:

contador = 0

while True:  # Loop infinito
    # print('exemplo 1: ', contador)
    contador += 1

    if contador >= 5:
        break  # Interrompe o loop quando contador atinge 5

# continue - Continuação para a Próxima Iteração:

contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        continue  # Pula para a próxima iteração quando contador é igual a 3

    # print('exemplo 2: ', contador)

# Iteração com Listas:

frutas = ['maçã', 'banana', 'laranja']

""" for fruta in frutas:
    print(fruta) """

# Função range() para Geração de Sequências Numéricas:

""" for i in range(5):
    print(i) """