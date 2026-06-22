# Projeto de Teoria dos Grafos - semestre 2026.1 - Engenharia de Computação/UFAL

Repositório destinado ao armazenamento da solução do projeto da AV2 da disciplina de Teoria dos Grafos.
A atividade aborda dois problemas clássicos aplicados a redes de computadores:

- **Parte 1:** caminho de menor custo em uma rede de backbone (grafo direcionado e ponderado, podendo ter arestas negativas).
- **Parte 2:** coloração de grafos para alocação de canais Wi-Fi (grafo não-direcionado e sem pesos), buscando o número cromático exato χ(G).

## **Alunos:**
  Giovanna Alves Barbosa de Oliveira \
  Marta Mirely Nascimento dos Santos \
  Walysson Maciel Melo \
  Vitória Maria Santana Bigi

## **Professor:**
Glauber Leite

## **Estrutura do repositório**

```
graph_theory_project/
├── README.md
├── grafo_rede_p.txt          # entrada da Parte 1 (grafo pequeno)
├── grafo_rede_m.txt          # entrada da Parte 1 (grafo médio, com pesos negativos)
├── grafo_wifi_p.txt          # entrada da Parte 2 (grafo pequeno)
├── grafo_wifi_m.txt          # entrada da Parte 2 (grafo médio)
├── parte1/
│   ├── main_part1.py         # ponto de entrada: lê o grafo, escolhe o algoritmo e gera a saída
│   ├── dijkstra.py           # implementação do Dijkstra (usado quando não há pesos negativos)
│   ├── bellman_ford.py       # implementação do Bellman-Ford (usado quando há pesos negativos)
│   ├── write_read_io.py      # leitura da entrada e escrita da saída no formato exigido
│   ├── saida_parte1_p.txt    # saída gerada para grafo_rede_p.txt
│   └── saida_parte1_m.txt    # saída gerada para grafo_rede_m.txt
└── parte2/
    ├── main_part2.py         # ponto de entrada: lê o grafo, executa o backtracking e gera a saída
    ├── backtracking.py       # implementação do backtracking que encontra o número cromático exato
    ├── write_read_io.py      # leitura da entrada e escrita da saída no formato exigido
    ├── saida_parte2_p.txt    # saída gerada para grafo_wifi_p.txt
    └── saida_parte2_m.txt    # saída gerada para grafo_wifi_m.txt
```

## **Como testar?**

1 - Clone o repositório do projeto:
```bash
git clone https://github.com/martanascimento1/graph_theory_project.git
```

2 - Abra o terminal na raiz do projeto:
```bash
cd graph_theory_project
```

### Parte 1 — Roteamento na rede de backbone

3 - Para gerar a saída do grafo pequeno (`grafo_rede_p.txt`):
```bash
python3 parte1/main_part1.py grafo_rede_p.txt parte1/saida_parte1_p.txt
```

4 - Para gerar a saída do grafo médio (`grafo_rede_m.txt`, com pesos negativos):
```bash
python3 parte1/main_part1.py grafo_rede_m.txt parte1/saida_parte1_m.txt
```

5 - As saídas `.txt` serão geradas na pasta `parte1`; para verificá-las:
```bash
cat parte1/saida_parte1_p.txt
cat parte1/saida_parte1_m.txt
```

### Parte 2 — Alocação de canais Wi-Fi

6 - Para gerar a saída do grafo pequeno (`grafo_wifi_p.txt`):
```bash
python3 parte2/main_part2.py grafo_wifi_p.txt parte2/saida_parte2_p.txt
```

7 - Para gerar a saída do grafo médio (`grafo_wifi_m.txt`):
```bash
python3 parte2/main_part2.py grafo_wifi_m.txt parte2/saida_parte2_m.txt
```

8 - As saídas `.txt` serão geradas na pasta `parte2`; para verificá-las:
```bash
cat parte2/saida_parte2_p.txt
cat parte2/saida_parte2_m.txt
```

> Não é necessário instalar nenhuma dependência externa — o projeto usa apenas a biblioteca padrão do Python 3 (testado com Python 3.12).

---

## **Comparativo e justificativa dos algoritmos**

### Parte 1 — Dijkstra vs. Bellman-Ford

O programa decide automaticamente qual algoritmo usar, verificando se existe alguma aresta com peso negativo:

| Grafo | Tem peso negativo? | Algoritmo escolhido | Por quê |
|---|---|---|---|
| `grafo_rede_p.txt` | Não | **Dijkstra** | Com todos os pesos ≥ 0, Dijkstra é o mais eficiente: O((V+E) log V) usando fila de prioridade, contra O(V·E) do Bellman-Ford. |
| `grafo_rede_m.txt` | Sim (acordos de SLA) | **Bellman-Ford** | Dijkstra falha na presença de pesos negativos, pois fixa a distância de um vértice ao removê-lo da fila — uma aresta negativa descoberta depois poderia invalidar essa distância. Bellman-Ford relaxa todas as arestas em V-1 rodadas e ainda detecta ciclos negativos, garantindo corretude. |

O Floyd-Warshall não foi usado em nenhum dos casos: ele resolve todos os pares de vértices (O(V³)), o que é desnecessário e mais custoso quando só precisamos do caminho de um único par (S, T).

### Parte 2 — Backtracking vs. heurísticas (Guloso/DSatur)

Foi escolhido **backtracking exaustivo** (testando k = 1, 2, 3, ... até achar a menor coloração válida) em vez de heurísticas como Guloso ou DSatur.

- **Vantagem:** garante o número cromático **exato** (χ(G)), e não apenas uma aproximação — algoritmos gulosos podem usar mais cores do que o necessário, dependendo da ordem dos vértices.
- **Custo:** backtracking é exponencial no pior caso, mas para o tamanho dos grafos desta atividade (5 e 8 vértices) a execução é praticamente instantânea, então a garantia de otimalidade compensa a simplicidade da implementação frente ao DSatur.
- Para grafos muito maiores, DSatur seria preferível por escalar melhor, abrindo mão da garantia de exatidão.

Ambos os grafos Wi-Fi (`grafo_wifi_p.txt` e `grafo_wifi_m.txt`) contêm triângulos, então χ(G) ≥ 3 em ambos; o backtracking confirma que 3 cores também são suficientes, ou seja, **χ(G) = 3** nos dois casos.
