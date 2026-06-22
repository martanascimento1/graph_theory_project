# -*- coding: utf-8 -*-

import sys
from backtracking import numero_cromatico
from write_read_io import escrever_saida, ler_grafo


def resolver_coloracao(caminho_entrada, caminho_saida):
    num_vertices, num_arestas, lista_adjacencia = ler_grafo(caminho_entrada)

    algoritmo = "Backtracking"
    justificativa = (
        """O problema pede o menor número de cores. O backtracking testa k em ordem crescente
           até encontrar a menor coloração válida, garantindo que a solução seja ótima. Além disso, em compa-
           ração com algoritmos como o DSsatur, o backtracking tem uma implementação mais simples e que funciona para a dimensão do projeto."""
    )

    k, coloracao = numero_cromatico(lista_adjacencia)
    cores_usadas = len(set(coloracao))
    escrever_saida(caminho_saida, algoritmo, justificativa, k, coloracao)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 parte2/main_part2.py <entrada.txt> <saida.txt>")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    resolver_coloracao(arquivo_entrada, arquivo_saida)
    print(f"Arquivo de saida gerado: {arquivo_saida}")
