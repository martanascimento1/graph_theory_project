
# verifica se nenhum vizinho de v tem a mesma cor c  
def eh_valido(v, c, grafo, cor):
    # percorre os vizinhos de v
    for u in grafo[v]:
        # se algum vizinho de v tem a mesma cor c, entao a coloracao nao e valida
        if cor[u] == c:
            return False
    # se nenhum vizinho de v tem a mesma cor c, entao a coloracao e valida
    return True

# tenta colorir todos os vertices a partir da posicao atual na ordem, usando no maximo k cores 
def backtrack(posicao, ordem, k, grafo, cor):
    # caso base
    # se ja coloriu todos os vertices, entao a coloracao e valida
    if posicao == len(ordem):
        return True

    # tenta colorir o vertice atual com cada cor de 1 a k
    v = ordem[posicao]
    for c in range(1, k + 1):
        # verifica se a cor c é valida para o vertice v, caso seja, segue para o proximo vertice
        if eh_valido(v, c, grafo, cor):
            cor[v] = c
            if backtrack(posicao + 1, ordem, k, grafo, cor):
                return True
            # caso não encontre uma coloraação valida, desfaz a escolha e tenta a próxima cor
            cor[v] = -1 
    # se nenhuma cor de 1 a k funcionou para v, entao nao existe coloracao valida com k cores        
    return False

# encontra o numero cromatico do grafo e uma coloracao valida
def numero_cromatico(grafo):
    # numero de vertices do grafo
    n = len(grafo)

    # ordena os vertices em grau decrescente
    # (o backtracking vai clorir primeiro os vertices com maior grau)
    ordem = sorted(range(n), key=lambda v: len(grafo[v]), reverse=True)

    # estado inicial (nenhum vertice colorido)
    cor = [-1] * n

    # tenta colorir o  grafo com k cores (k de 1 até n)
    for k in range(1, n + 1):
        if backtrack(0, ordem, k, grafo, cor):
            return k, cor
    # se não existir uma coloração válida com n cores, o numero cromatico é n (grafo completo)
    return n, cor
