"""
Modulo Collections - Counter (contador)

Collections -> High-performance Container Datetypes

Counter -> Rece um iteravel como parametro e cria um objeto do tipo collections counter
que eh parecido com um dicionario, contendo como chave um elemento da lista passada por paramentro
e como valor a quantidade de ocorrencias desse eleemento


lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

#Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

#Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias

#Exemplo 2
print(Counter('Eduardo'))
"""

#Utilizando o counter

from collections import Counter

#Exemplo 3

texto = """
Aprenda Python 3.8.5 com Expressões Lambdas, 
Iteradores, Geradores, Orientação a Objetos e muito mais!
"""

palavras = texto.split()

res = Counter(palavras)

print(res)

#Encontrando as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))