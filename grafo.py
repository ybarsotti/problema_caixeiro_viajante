class Grafo(object):
    def __init__(self, df):
        self.vertices = self.adiciona_vertices(df)
        self.arestas = []
        self.custo = 0

    def adiciona_custo(self, custo):
        """
        Soma o custo no grafo
        :param custo:
        :type custo:
        :return:
        :rtype:
        """
        self.custo += int(custo) if custo != '-' else 0

    def adiciona_arestas(self, arestas):
        self.arestas.append(arestas)

    def adiciona_vertices(self, df):
        return list(map(lambda x: str(x).lower(), df.columns))