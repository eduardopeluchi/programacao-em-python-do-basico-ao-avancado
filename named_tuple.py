"""
Modulo Collections - Named Tuple
#Recap Tupla

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple ->  Sao tuplas diferenciadas onde especificamos um nome para a mesma e parametros
"""

from collections import namedtuple

#Precisamos definir o nome e parametro
#Forma 1 - Declaracao Named Tuple
gato = namedtuple('gato', 'idade raca nome')

#Forma 2 - Declaracao Named Tuple
gato = namedtuple('gato', 'idade, raca, nome')

#Forma 3 - Declaracao Named Tuple
gato = namedtuple('gato', ['idade', 'raca', 'nome'])

#Usando

camila = gato(idade=2, raca='gato', nome='Camila')

print(camila)
print(camila[0])
print(camila.idade)
