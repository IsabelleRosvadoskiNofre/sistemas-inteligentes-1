def busca_retrocesso(g, inicial, objetivo):
    le = [inicial]          # caminho atual
    lne = [inicial]         # estados que ainda podem ser avaliados
    bss = []                # becos sem saída

    lne_custo = [0]         # custo acumulado associado a cada estado de LNE
    le_custo = [0]          # custo acumulado associado a cada estado de LE

    ec = inicial
    custo_atual = 0

    while lne != []:

        # encontrou o objetivo
        if ec == objetivo:
            caminho = list(reversed(le))
            return caminho, custo_atual

        # procura filhos que realmente podem ser explorados
        filhos_validos = []

        for filho, peso in g[ec]:
            if (
                filho not in bss
                and filho not in le
                and filho not in lne
            ):
                filhos_validos.append((filho, peso))

        # se não existem filhos válidos, chegou em um beco sem saída
        if not filhos_validos:

            while le and ec == le[0]:

                bss.append(ec)

                le.pop(0)
                le_custo.pop(0)

                lne.pop(0)
                lne_custo.pop(0)

                # não existe mais nenhum estado para explorar
                if not lne:
                    return [], None

                ec = lne[0]
                custo_atual = lne_custo[0]

            # encontrou uma alternativa
            le = [ec] + le
            le_custo = [custo_atual] + le_custo

        else:

            # colocamos em ordem reversa porque estamos
            # inserindo cada elemento no início da lista
            for filho, peso in reversed(filhos_validos):

                novo_custo = custo_atual + peso

                lne = [filho] + lne
                lne_custo = [novo_custo] + lne_custo

            ec = lne[0]
            custo_atual = lne_custo[0]

            le = [ec] + le
            le_custo = [custo_atual] + le_custo

    return [], None


def main():
    grafo = {
        'A': [('B', 100), ('C', 125), ('D', 100), ('E', 75)],

        'B': [('A', 100), ('C', 50), ('D', 75), ('E', 125)],

        'C': [('A', 125), ('B', 50), ('D', 100), ('E', 125)],

        'D': [('A', 100), ('B', 75), ('C', 100), ('E', 50)],

        'E': [('A', 75), ('B', 125), ('C', 125), ('D', 50)]
    }

    return grafo


if __name__ == '__main__':
    g = main()

    caminho, custo = busca_retrocesso(g, 'A', 'C')

    if caminho:
        print("Caminho:", caminho)
        print("Custo:", custo)
    else:
        print("FALHA")