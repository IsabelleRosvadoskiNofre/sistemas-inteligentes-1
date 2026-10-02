def busca_retrocesso(g, inicial):
    le = [inicial] #lista de estados (caminho que eu vou mostrar se der certo)
    lne = [inicial] #lista de novos estados
    bss = [] #beco sem saida

    ec = inicial #estado corrente


    while lne != []:
        if ec == 'I':
            return le
        
        if not g[ec]: #se o estado corrente tiver o vetor dele vazio (ou seja não tem filhos)
            while le and ec == le[0]:
                bss.append(ec)
                le.pop(0)
                lne.pop(0)
                ec = lne[0]
            le = [ec] + le
        else:
            filhos = g[ec]

            for filho in reversed(filhos):
                if filho not in bss and filho not in le and filho not in lne:
                    lne = [filho] + lne
            ec = lne[0]
            le = [ec] + le
    return []

def main():
    dicionario = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': [],
        'D': [],
        'E': ['H', 'I'],
        'F': [],
        'H': [],
        'I': []
    }

    return dicionario


if __name__ == '__main__':
    g = main()          
    le = busca_retrocesso(g, 'A')
    print(le)