#!/user/bin/env python3

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


def gera_grafo_visual(dados):
    G = nx.Graph()


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
            aresta = dict(rota=(cidade_origem, destino), peso=peso)
            grafo.adiciona_arestas(aresta)

    valores = [val for val in grafo.arestas]

    #print(list(filter(lambda x: x.key() == ('a', 'b'), grafo.arestas)))
    exit(10)
    return grafo


def origem_destino(df) -> (str, str):
    """
    Seleção de origem e destino do algoritmo
    :param df:
    :type df:
    :return:
    :rtype:
    """
    opcoes_origem = list(map(lambda x: str(x.lower()), df.columns))
    print('Dentre as cidades abaixo, escolha o ponto de partida.')

    # Seleção origem
    while True:
        try:
            print(list(opcoes_origem))
            origem = str(input('=> ')).lower()
            if origem not in opcoes_origem:
                raise Exception('Cidade inválida, tente novamente.')
            break
        except Exception as e:
            print(e)

    opcoes_destino = list(map(lambda x: str(x.lower()), df.columns))
    opcoes_destino.remove(origem)
    print('Escolha o Destino.')
    # Seleção destino
    while True:
        try:
            print(opcoes_destino)
            destino = str(input('=> ')).lower()
            if destino not in list(opcoes_destino):
                raise Exception('Cidade inválida, tente novamente.')
            break
        except Exception as e:
            print(e)

    return origem, destino


def main(df):
    gera_grafo(df)
    origem, destino = origem_destino(df)

    tamanho_matriz = len(df.columns)

    for i in range(tamanho_matriz):
        """
        Itera (n - 1) vezes o processamento do algoritmo, sendo n = quantidade de cidades.
        """
        for j in range(1, tamanho_matriz):
            #           print(f'Cidade {df.iloc[:, j].name}: ')
            for k in range(1, tamanho_matriz + 1):
                #                print(df.iloc[j][k])
                if df.iloc[j][k] != '-':
                    pass


if __name__ == '__main__':
    main(carregar())
