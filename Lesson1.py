numero_decimal = int(input())
"Nb = '{0:08b}'.format(N)"
lista_de_binarios = list(bin(numero_decimal))

print(lista_de_binarios)
print(lista_de_binarios.count('0'))

contador = 2
tamanho_da_lacuna = 0
quantidade_de_zeros = 0
test_lacuna = 0
contador_de_lacunas = 2

while contador < len(lista_de_binarios):
    if lista_de_binarios[contador] == '0':
        quantidade_de_zeros+=1
    else:
        if tamanho_da_lacuna < quantidade_de_zeros:
            tamanho_da_lacuna = quantidade_de_zeros
            quantidade_de_zeros = 0
            test_lacuna+=1
        else:
            if tamanho_da_lacuna > quantidade_de_zeros:
                print(f"Lacuna numero: {contador_de_lacunas} tamanho = ", quantidade_de_zeros)
                contador_de_lacunas += 1
    contador += 1

if test_lacuna == 0 or quantidade_de_zeros == 0:
    print("nao tem lacunas")
else:
    print("Lacuna numero: 1 tamanho =", tamanho_da_lacuna)
