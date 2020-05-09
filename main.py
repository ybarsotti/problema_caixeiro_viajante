#!/user/bin/env python3
import mlrose
import pandas as pd
import networkx as nx
import plotly.graph_objects as go

from grafo import Grafo

# Lista de todos os grafos
grafos = []


def carregar():
    global colunas
    try:
        df = pd.read_csv('cidades.csv', index_col=0)
        colunas = list(map(lambda x: str(x.lower()), df.columns))
        if df.shape[0] != df.shape[1]:
            raise Exception('Número de colunas e linhas são diferentes. ')
        return df
    except Exception as e:
        print('Falha ao carregar arquivo. Msg: {}'.format(e))
        exit()


def gera_grafo_visual():
    G = nx.Graph()

    fig = go.Figure(
        data=[grafo.vertices, ('a', 'a')],
        title='Grafo inicial',
        titlefont_size=16,
        hovermode='closest',

    )
    fig.show()


def gera_grafo(df) -> Grafo:
    global grafo

    grafo = Grafo(df)

    for i in range(len(colunas)):
        # Pega o nome da cidade pelo índice
        cidade_origem = colunas[i]
        for j in range(len(colunas)):
            # Pega o peso e o destino da aresta e adiciona no objeto Grafo
            destino = df.index[j]
            peso = df.iloc[j][cidade_origem]
            #aresta = dict(rota=(cidade_origem, destino), peso=peso)
            if peso != '-':
                aresta = (int(cidade_origem), int(destino), int(peso))
                grafo.adiciona_arestas(aresta)

    fitness = mlrose.TravellingSales(distances=grafo.arestas)
    # Define optimization problem object
    problem_fit = mlrose.TSPOpt(length=8, fitness_fn=fitness, maximize=False)
    best_state, best_fitness = mlrose.genetic_alg(problem_fit, mutation_prob=0.2, max_attempts = 100, random_state = 2)
    print(fitness)
    return grafo



def main(df):
    gera_grafo(df)


if __name__ == '__main__':
    main(carregar())
