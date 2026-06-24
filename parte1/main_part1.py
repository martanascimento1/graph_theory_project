# -*- coding: utf-8 -*-
"""
O grafo é inspecionado em busca de arestas com peso negativo (que
representam enlaces com acordo de SLA, reduzindo o custo do trajeto):

  - Se nenhuma aresta tiver peso negativo  --> usa Dijkstra
  - Se houver ao menos uma aresta negativa -> usa Bellman-Ford
"""

import sys
from write_read_io import ler_grafo, escrever_saida
from dijkstra import dijkstra
from bellman_ford import bellman_ford


def existe_peso_negativo(arestas):
    # Retorna True se alguma aresta (u, v, peso) tiver peso < 0
    return any(peso < 0 for _, _, peso in arestas)


def reconstruir_rota(predecessor, origem, destino):
    if origem == destino:
        return [origem]

    if predecessor[destino] is None:
        return None  # destino nunca foi alcancado

    rota = []
    atual = destino
    while atual is not None:
        rota.append(atual)
        if atual == origem:
            break
        atual = predecessor[atual]

    rota.reverse()

    # Se o primeiro vertice da rota reconstruida nao for a origem, significa que o destino esta em um componente desconexo da origem
    if rota[0] != origem:
        return None

    return rota


def resolver_roteamento(caminho_entrada, caminho_saida):

    # lê o grafo, escolhe e executa o algoritmo mais adequado, reconstroi a rota e escreve o arquivo de saida
    (num_vertices, num_arestas, origem, destino,
     lista_adjacencia, arestas) = ler_grafo(caminho_entrada)

    negativo = existe_peso_negativo(arestas)

    if not negativo:
        algoritmo = "Dijkstra"
        justificativa = (
            "Todos os pesos das arestas sao nao-negativos, portanto "
            "Dijkstra é aplicavel e mais eficiente (O((V+E) log V)) do "
            "que Bellman-Ford para um unico par (S,T)."
        )
        dist, predecessor = dijkstra(num_vertices, lista_adjacencia, origem, destino)
        ciclo_negativo = False

    else:
        algoritmo = "Bellman-Ford"
        justificativa = (
            "O grafo contem arestas com peso negativo (acordos SLA), o "
            "que invalida Dijkstra (ele fixa a distancia de um vertice "
            "ao remove-lo da fila). Bellman-Ford suporta pesos "
            "negativos e detecta ciclos negativos."
        )
        dist, predecessor, ciclo_negativo = bellman_ford(num_vertices, arestas, origem, destino)

    if ciclo_negativo:
        escrever_saida(
            caminho_saida,
            algoritmo,
            justificativa + " ATENCAO: foi detectado um ciclo de peso "
            "negativo alcancavel a partir de S; o caminho minimo nao "
            "esta definido.",
            rota=None,
            custo="CICLO NEGATIVO DETECTADO - CAMINHO MINIMO INDEFINIDO",
        )
        return

    rota = reconstruir_rota(predecessor, origem, destino)
    custo = dist[destino]

    if rota is None or custo == float("inf"):
        escrever_saida(
            caminho_saida,
            algoritmo,
            justificativa,
            rota=None,
            custo=f"NAO HA CAMINHO DE {origem} ATE {destino}",
        )
    else:
        escrever_saida(caminho_saida, algoritmo, justificativa, rota, custo)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 parte1_roteamento.py <entrada.txt> <saida.txt>")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    resolver_roteamento(arquivo_entrada, arquivo_saida)
    print(f"Arquivo de saida gerado: {arquivo_saida}")