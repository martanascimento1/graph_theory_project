# -*- coding: utf-8 -*-
"""
Implementação do algoritmo de Bellman Ford 

Motivação da escolha --> suporta pesos negativos (desde que nao haja
ciclo negativo alcancavel a partir da origem).

Como é feita a detecção do ciclo negativo --> Se, apos as V-1 rodadas de relaxamento, ainda for possivel relaxar
alguma aresta (ou seja, encontrar uma distancia menor), entao existe um
ciclo de peso negativo alcancavel a partir da origem. Nesse caso o
conceito de "caminho minimo" deixa de fazer sentido (o custo poderia
ser reduzido indefinidamente percorrendo o ciclo repetidas vezes), e o
algoritmo deve reportar essa condicao em vez de um valor numerico.

num_vertices : Quantidade de vertices do grafo (numerados de 0 a num_vertices-1).
arestas : Lista plana de todas as arestas do grafo, no formato (u, v, peso).
origem :  Vertice de partida (S).
destino : Vertice de chegada (T). 

Saída: 
dist : Menor custo conhecido da origem ate cada vertice
predecessor :Vertice anterior de cada vertice no caminho minimo encontrado.
ciclo_negativo : bool
    True se foi detectado um ciclo de peso negativo alcancavel a
    partir da origem (nesse caso, dist/predecessor nao sao confiaveis
    para os vertices afetados pelo ciclo).
"""
def bellman_ford(num_vertices, arestas, origem, destino):

    INFINITO = float("inf")

    dist = {v: INFINITO for v in range(num_vertices)}
    predecessor = {v: None for v in range(num_vertices)}
    dist[origem] = 0

    # Fase 1: relaxa todas as arestas, V-1 vezes
    for _ in range(num_vertices - 1):
        houve_atualizacao = False
        for u, v, peso in arestas:
            if dist[u] != INFINITO and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                predecessor[v] = u
                houve_atualizacao = True

        # se uma rodada inteira nao alterou nada,no algoritmo já convergiu
        if not houve_atualizacao:
            break

    # deteccao de ciclo negativo
    ciclo_negativo = False
    for u, v, peso in arestas:
        if dist[u] != INFINITO and dist[u] + peso < dist[v]:
            ciclo_negativo = True
            break

    return dist, predecessor, ciclo_negativo