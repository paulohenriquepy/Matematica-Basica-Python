# Função para calcular o número de combinações entre dois números

def pedir_numeros():
    print("Essa calculadora funciona apenas com números inteiros positivos.")
    print("Você precisa inserir dois números para os quais você deseja saber o número de combinações possíveis")

    numero_1 = int(input("Insira o primeiro número ---->"))
    numero_2 = int(input("Insira o segundo número ---->"))

    # Verificar se um número é positivo
    while not numero_1 and numero_2 > 0:
        print("Sinto muito. Você não inseriu um número inteiro positivo")
        numero_1 = int(input("Insira o primeiro número ---->"))
        numero_2 = int(input("Insira o segundo número ---->"))
    else:
        print("Você inseriu os dois números corretamente.\n Vamos calcular o número de combinações possíveis.")

    lista_de_numeros = [numero_1, numero_2]

    return lista_de_numeros

lista_de_numeros = pedir_numeros()

def fatorial(lista_de_numeros):

    lista_de_numeros = lista_de_numeros
    terceiro_numero = lista_de_numeros[0] - lista_de_numeros[1]
    lista_de_numeros.append(terceiro_numero)
    lista_fatoriais = []

    for numero in lista_de_numeros:
        fatorial = []

        # Adiciona os números de 1 até o número inserido pelo usuário na lista fatorial
        for elemento in range(1, numero + 1):
            fatorial.append(elemento)

        # Inicializa resultado antes do loop
        resultado = 1

        # Calculando o fatorial
        for valor in fatorial:
            resultado = resultado * valor

        # Obtendo o valor final do fatorial
        produtos = []
        produtos.append(resultado)

        # Obtendo o último valor da lista produtos
        valor_final = produtos[-1]
        lista_fatoriais.append(valor_final)

    print(lista_fatoriais)

    return lista_fatoriais

lista_fatoriais = fatorial(lista_de_numeros)

def combinacoes(lista_fatoriais):

    lista_fatoriais = lista_fatoriais
    n = lista_fatoriais[0]
    k = lista_fatoriais[1]
    n_menos_k = lista_fatoriais[2]
    print(n)

    combinacao = n / (k * n_menos_k)

    print(f"O número de combinações possíveis é {combinacao}.")

    return combinacao

combinacoes(lista_fatoriais)