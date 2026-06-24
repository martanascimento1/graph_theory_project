# -*- coding: utf-8 -*-
import heapq
"""
Implementacao do algoritmo de Dijkstra 
Motivação da escolha --> valido apenas quando TODOS os pesos das
arestas sao >= 0.

num_vertices : Quantidade de vertices do grafo (numerados de 0 a num_vertices-1).
lista_adjacencia : vertice -> lista de (vizinho, peso_da_aresta).
origem : Vertice de partida (S).
destino : Vertice de chegada (T). (Mantido por simetria de interface com
    bellman_ford; o algoritmo pode parar cedo ao alcanca-lo.)

Saída:
dist : Menor custo conhecido da origem ate cada vertice
predecessor:  Vertice anterior de cada vertice no caminho minimo encontrado; usado para reconstruir a rota completa.
"""

def dijkstra(num_vertices, lista_adjacencia, origem, destino):

    INFINITO = float("inf")

    dist = {v: INFINITO for v in range(num_vertices)}
    predecessor = {v: None for v in range(num_vertices)}
    dist[origem] = 0

    # Fila de prioridade de pares (distancia_atual, vertice)
    fila_prioridade = [(0, origem)]
    visitados = set()

    while fila_prioridade:
        distancia_u, u = heapq.heappop(fila_prioridade)

        if u in visitados:
            continue
        visitados.add(u)

        # Só é necessário o caminho ate T
        if u == destino:
            break

        for vizinho, peso in lista_adjacencia[u]:
            if peso < 0:
                raise ValueError(
                    "Dijkstra recebeu uma aresta com peso negativo "
                    f"({u} -> {vizinho}, peso={peso}); use Bellman-Ford."
                )
            nova_distancia = distancia_u + peso
            if nova_distancia < dist[vizinho]:
                dist[vizinho] = nova_distancia
                predecessor[vizinho] = u
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

    return dist, predecessor