"""
Modulo Collections - Deque

Podemos dizer que o deque eh uma lista de alta performance.
"""

from collections import deque

deq = deque('eduardo')

print(deq)

#adicionando elementos no deque no final
deq.append('p') #adiciona no final
print(deq)

deq.appendleft('A')#adiciona no comeco
print(deq)

print(deq.pop()) #remove no final
print(deq)

print(deq.popleft())#remove no comeco
print(deq)
