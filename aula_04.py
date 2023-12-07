# Iteração com Listas:

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_frutas = ['maçã', 'banana', 'laranja']

# Função para listar somente números pares:
""" for numero in lista_numeros:
    resto = numero % 2
    if (resto == 0):
        print(numero) """
# Acesso por Índices:

primeiro_elemento = lista_numeros[0]  # Resultado: 1
ultimo_elemento = lista_numeros[-2]  # Resultado: 5[]

# print(primeiro_elemento)
# print(ultimo_elemento)

primeira_fruta = lista_frutas[0]
ultima_fruta = lista_frutas[-2]

# print(primeira_fruta)
# print(ultima_fruta)


# Adicionando um elemento

# lista_frutas[0] = 'pêra'
# print(lista_frutas)

# lista_frutas.append('uva')
# print(lista_frutas)


# Removendo um elemento

# lista_frutas.remove('banana')
# lista_frutas.insert(2, 'morango')
# lista_frutas.pop(1)
# print(lista_frutas)


# Fatiamento de lista (slice)

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_frutas = ['maçã', 'banana', 'laranja']

sublista_numeros = lista_numeros[1:5] # [1, 2, 3, 4]
sublista_frutas = lista_frutas[1:2] # ['banana']

# print(sublista_numeros)
# print(sublista_frutas)


# Tamanho da lista e outras funções com listas

tamanho_lista = len(lista_numeros)
lista_numeros.sort()
lista_numeros.reverse()


# Tuplas
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
# tupla_numeros[0] = 100
# print(tupla_numeros)

# Set
conjunto1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
conjunto2 = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

uniao = conjunto1 | conjunto2
intersecao = conjunto1 & conjunto2
diferenca = conjunto1 - conjunto2

# print(uniao)
# print(intersecao)
# print(diferenca)

# Removendo duplicatas de uma lista
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
conjunto_sem_duplicatas = set(lista_com_duplicatas)
print(conjunto_sem_duplicatas)