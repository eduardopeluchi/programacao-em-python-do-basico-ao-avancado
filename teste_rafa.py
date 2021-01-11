numero = 0
soma = 0

while True:
    numero = int(input("texto"))

    if numero > 100 or numero < -100:
        break
    else:
        soma = soma + numero

print(soma)
