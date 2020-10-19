#verificar a ordenação da lista 
def verificarOrdenacao(lista_vacas):
    i = 0
    ordenado = True
    while i < len(lista_vacas) - 1:
        if lista_vacas[i+1] < lista_vacas[i]:
            ordenado = False
        i = i + 1
    return ordenado

#efeturar partição da lista - auxiliar ordenação rápida
def particionar(lista_vacas, inicio, fim):
    pivo = lista_vacas[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista_vacas[direita] <= pivo:
            lista_vacas[direita], lista_vacas[esquerda] = lista_vacas[esquerda], lista_vacas[direita]
            esquerda = esquerda + 1
    lista_vacas[esquerda], lista_vacas[fim] = lista_vacas[fim], lista_vacas[esquerda]
    return esquerda

#ordenação rápida - caso a lista não esteja ordenada
def ordenacaoRapida(lista_vacas, inicio, fim):
    if inicio < fim:
        pivo = particionar(lista_vacas, inicio, fim)
        ordenacaoRapida(lista_vacas, inicio, pivo - 1)
        ordenacaoRapida(lista_vacas, pivo + 1, fim)
    return lista_vacas

#efetuar busca binária
def buscarAnimal(lista_vacas, cod_vaca):
    menor = 0
    maior = len(lista_vacas) - 1
    encontrado = False

    while menor <= maior and not encontrado:
        meio = (menor + maior) // 2
        if lista_vacas[meio] == cod_vaca:
            encontrado = True
        else:
            if cod_vaca < lista_vacas[meio]:
                maior = meio - 1
            else:
                menor = meio + 1

    return encontrado

#Programa Principal
lista_vacas = [3,4,5,7,2,6,9,13,53,87,42,76,69]

codigo = int(input("Digite o código do animal: "))

ordenado = verificarOrdenacao(lista_vacas)

if not ordenado:
    ordenacaoRapida(lista_vacas, 0, len(lista_vacas) - 1)

encontrado = buscarAnimal(lista_vacas, codigo)

if encontrado:
    print("O animal de código {} foi encontrado!".format(codigo))
else:
    print("O animal não foi encontrado.")
