# -*- coding: utf-8 -*-
"""
Leitura e escrita para a Parte 2.

Formato de entrada:
    <num_vertices>\\t<num_arestas>
    <vertice_u>\\t<vertice_v>    (repetida por aresta, sem peso)

Formato de saida:
    ALGORITMO: <nome do algoritmo>
    JUSTIFICATIVA: <texto livre, ate 3 linhas>
    NUM_CORES: <k>
    COLORACAO: <v0>=<cor> <v1>=<cor> ... <vn>=<cor>
"""


def ler_grafo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        linhas = [linha.rstrip("\n") for linha in f if linha.strip() != ""]

    num_vertices, num_arestas = (int(x) for x in linhas[0].split("\t"))

    vizinhos = {v: set() for v in range(num_vertices)}

    for linha in linhas[1: 1 + num_arestas]:
        u_str, v_str = linha.split("\t")
        u, v = int(u_str), int(v_str)
        vizinhos[u].add(v)
        vizinhos[v].add(u)

    lista_adjacencia = {v: list(vizinhos[v]) for v in range(num_vertices)}

    return num_vertices, num_arestas, lista_adjacencia


def escrever_saida(caminho_arquivo, algoritmo, justificativa, num_cores, coloracao):
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(f"ALGORITMO: {algoritmo}\n")
        f.write(f"JUSTIFICATIVA: {justificativa}\n")
        f.write(f"NUM_CORES: {num_cores}\n")

        partes = [f"{v}={coloracao[v]}" for v in range(len(coloracao))]
        f.write("COLORACAO: " + " ".join(partes) + "\n")
