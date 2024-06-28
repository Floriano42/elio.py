lista = []
tamanhoListas = 5
maiorValor=0
menorValor=9999999999999999999999999999999


for i in range (tamanhoListas):
    valor = int(input('Dígite o valor'))
    lista.append(valor)
    if lista[i] > maiorValor:
        maiorValor= lista[i]
    if lista[i]< menorValor:
        menorValor = lista[i]

soma = maiorValor + menorValor
print(soma)