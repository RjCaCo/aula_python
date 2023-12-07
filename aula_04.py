# Iteração com Listas:

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_frutas = ['maçã', 'banana', 'laranja']

# Função para listar somente números pares:

for numero in lista_numeros:
    resto = numero % 2
    if (resto == 0):
        print(numero)


# Acesso por Índices:

primeiro_elemento = lista_numeros[0]  # Resultado: 1
ultimo_elemento = lista_numeros[-1]  # Resultado: 5

segunda_fruta = lista_frutas[1]
# print(segunda_fruta)  # Saída: banana


# Adicionando um elemento

lista_frutas[0] = 'pêra'
# print(lista_frutas)  # Saída: ['pêra', 'banana', 'laranja']

lista_frutas.append('uva')
# print(lista_frutas)  # Saída: ['pêra', 'banana', 'laranja', 'uva']


# Removendo um elemento

lista_frutas.remove('banana')
# print(lista_frutas)  # Saída: ['pêra', 'morango', 'laranja', 'uva']


# Fatiamento de lista

sublista_numeros = lista_numeros[1:4]  # Resultado: [2, 3, 4]
sublista_frutas = lista_frutas[1:4]  # Resultado: [2, 3, 4]


# Tamanho da lista e outras funções com listas

tamanho_lista = len(lista_numeros)
lista_numeros.sort()
lista_numeros.reverse()

# print(tamanho_lista)      # Saída: 10
# print(lista_numeros)      # Saída: [9, 6, 5, 5, 4, 3, 3, 2, 1, 1]