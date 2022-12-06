import math

import networkx as nx
from networkx import NetworkXUnbounded

G = nx.DiGraph()

def build_digraph_logarithm(mat):
    for i in range(len(mat)):
        G.add_node(i)

    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j or mat[i][j] == 0:
                continue
            logarithm_number = math.log(mat[i][j],2)
            G.add_weighted_edges_from([(i,j,logarithm_number)])
            #print((i,j,logarithm_number))
    return G


def find_cycle(digraph, start):
    try:
        path = nx.single_source_bellman_ford_path(digraph, start)
        print(path)
    except NetworkXUnbounded:
        cycles = nx.find_negative_cycle(digraph,0)
        print(cycles)


#def logarithm_of_edge(G):


