"""
Conjuntos em qualquer linguagem de programacao estamos fzendo referencia
a teoria dos conjuntos da matematica

Aqui no python os conjuntos sao chamos de sets

Dito isto da mesma forma uque na matematica

Sets(Conjuntos) nao Possuem valores duplicados
Sets(Conjuntos) nao possuem valores ordenados
Elementos nao sao acessados via indice ou seja conjuntos nao sao indexados

Conjuntos sao bon para se utilizar quandoprecisamos armazenar elementos
mas nao nos importamos com a ordenacao deles quando nao precisamos se preocupar com chaves, valores e itens duplicados
Os conuntos (sets) sao referenciados em Python com chaves {}

Diferenca entre conjuntos (Set) e mapas (dicionario) em python
    Um dicionario tem chave/valor
    Um conjuntos tem apenas valor

    #Definindo conjuntos

#Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})

print(s)
print(type(s))

#OBS: Ao criar um conjjunto caso seja adicionado um valor ja existente, o mesmo
#sera ignorado sem gerar error e nao fara parte do conjunto

#Forma 2 - Mais Comum
s= set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))

# Importante lembrar que alem de nao termos valores duplciados nao temos ordem
#listas aceitam valores duplicados
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

#Tuplas aceitam valores duplicados
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'tupla: {tupla} com {len(tupla)} elementos')

#Dicionarios nao aceitam chaves duplicadas
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')

#Conjuntos nao aceitam valore duplicados / recebe um ordenacao propria na hora de mostrar os dados
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

#Assim com todo outro conjunto Python podemos colocar tipos de dados misturados em Sets
#Podemos iterar em um set normalmente (utilizar FOR)

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

#Podemos iterar em um set normalmente

for valor in s:
    print(valor)


#Usos interessantes com sets
#Imagine que fizemos um formulario de um cadastro de cisitantes em uma feira
#ou muse e os visitantes informam manualmente a cidade de onde vieram.

#Nos adicionamos cada cidade em uma lista Python ja que em uma
#lista podemos adicionar novos elementos e ter repeticoes

cidades = ['Belo Horizonete', 'Sao Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'Sao Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

#Agora precisamos saber quantas cidades distintas ou seja unicas temos

#Podemos utilizar o set para fazer isso

print(len(set(cidades)))

#Adicionando elementos em um conjunto

s = {1, 2, 3}

s.add(4)
s.add(4) #Duplicidade nao gera erro, simplemsnte eh ignorado e nao eh adicionado
print(s)

#Remover elementos de um conjunto

s = {1, 2, 3}
print(s)

#Forma 1

s.remove(3) #nao eh indice, informamos o valor a ser removido

print(s)

#OBS. caso o valor nao seja encontrado sera gerado o erro KeyError

#Forma 2

s.discard(2)
print(s)

#OBS. se o valor nao for encontrado nenhum erro eh gerado

#Copiando um conjunto para outro

#Forma 1 - Deep Copy

novo = s.copy()

novo.add(4)

print(novo)
print(s)

#Forma 2 - Shallow Copy

novo = s
novo.add(4)

print(novo)
print(s)

#Podemos removes todos os ietns de um conjunto

s.clear()
print(s)
"""


