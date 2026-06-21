# -*- coding: utf-8 -*-
"""
Esse módulo é responsável por:
  1) Ler o arquivo de entrada no formato definido:

         <num_vertices>\t<num_arestas>
         <S>\t<T>
         <vertice_u>\t<vertice_v>\t<custo>     (repetida por aresta)

  2) Escrever o arquivo de saida no formato exigido:

         ALGORITMO: <nome do algoritmo>
         JUSTIFICATIVA: <texto livre, ate 3 linhas>
         ROTA: <v0> <v1> <v2> ... <vn>
         CUSTO: <valor inteiro ou decimal>

O separador de campos na entrada e TAB ('\t'), conforme especificado.

caminho_arquivo : Caminho do arquivo .txt de entrada.

Saída: 
num_vertices : Quantidade de vertices do grafo (vertices numerados de 0 a num_vertices - 1).
num_arestas : Quantidade de arestas declaradas no cabecalho.
origem : Vertice de origem (S) do caminho minimo a ser calculado.
destino : Vertice de destino (T) do caminho minimo a ser calculado.
lista_adjacencia : Para cada vertice u, lista de pares (v, peso) representando uma aresta direcionada u -> v com o custo "peso".
arestas : Lista plana de todas as arestas (u, v, peso)
"""

def ler_grafo(caminho_arquivo):

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        linhas = [linha.rstrip("\n") for linha in f if linha.strip() != ""]

    # Linha 0: numero de vertices e numero de arestas
    num_vertices, num_arestas = (int(x) for x in linhas[0].split("\t"))

    # Linha 1: vertice de origem (S) e vertice de destino (T)
    origem, destino = (int(x) for x in linhas[1].split("\t"))

    # Inicializa a lista de adjacencia para todos os vertices, mesmo os que nao possuem arestas de saida (evita KeyError mais adiante).
    lista_adjacencia = {v: [] for v in range(num_vertices)}
    arestas = []

    for linha in linhas[2: 2 + num_arestas]:
        u_str, v_str, peso_str = linha.split("\t")
        u, v, peso = int(u_str), int(v_str), int(peso_str)
        lista_adjacencia[u].append((v, peso))
        arestas.append((u, v, peso))

    return num_vertices, num_arestas, origem, destino, lista_adjacencia, arestas


def escrever_saida(caminho_arquivo, algoritmo, justificativa, rota, custo):

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(f"ALGORITMO: {algoritmo}\n")
        f.write(f"JUSTIFICATIVA: {justificativa}\n")

        if rota is None:
            f.write(f"ROTA: {custo}\n")  # mensagem de erro/indefinicao
            f.write("CUSTO: indefinido\n")
            return

        f.write("ROTA: " + " ".join(str(v) for v in rota) + "\n")

        if isinstance(custo, float) and custo.is_integer():
            custo = int(custo)
        f.write(f"CUSTO: {custo}\n")