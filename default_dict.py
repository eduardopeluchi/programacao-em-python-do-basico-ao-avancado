"""
Modulo Collections - Default Dict

#Recap Dicionarios
dicionario = {'curso': 'Programacao em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])

Default Dict -> Ao criar um dicionario utilizando-o, nos informamos um valor default
podendo utilizar um lambda para isto, Este valor sera utilizado sempre que nao houver
um valor definido, Caso tentemos acessar uma chave que nao existe, essa chave sera
criada e o valor default sera atribuido.

OBS. Lambdas sao funcoes sem nome que podem ou nao receber parametro de entrada e retornar valores
"""

#Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programacao em Python: Essencial'

print(dicionario)
print(dicionario['outro'])
print(dicionario)



