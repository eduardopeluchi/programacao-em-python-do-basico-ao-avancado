"""
Modulo Collections - Ordered Dict

#Em um dicionario a ordem de insercao dos elementos nao eh garantida
dicionario = {'a': 1, 'b': 2, 'c':3, 'd': 4, 'c': 5}

print(dicionario)

#Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c':3, 'd': 4, 'c': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""
#Fazendo o import
from collections import OrderedDict

#Entendendo a diferenca entre Dict e Ordered Dict

#Dicionarios Comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)


