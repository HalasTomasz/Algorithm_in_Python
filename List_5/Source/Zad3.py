import Kolejka
from sys import exit, argv
import networkx as nx
from decimal import Decimal
from collections import namedtuple

Counter = 0
GraphEdge = namedtuple('GraphEdge', ['first', 'second', 'weight'])

def find(tmp,sets):
        node = tmp
        while node != sets[node]:
            node = sets[node]
        return node
    
def Finder(first, second,sets):
        tmp1 = find(first,sets)
        tmp2 = find(second,sets)
        sets[tmp2] = tmp1
        return sets
    
def Kruskal(graph):
 
    global Counter
    sets = [i for i in range(0, Counter)]
    result = []
    edges = sorted(graph.edges(), key=lambda a: graph.get_edge_data(a[0],a[1])['weight'])
    for edge in edges:
        first, second = edge[0], edge[1]
        if find(first,sets) != find(second,sets):
            result.append(edge)
            sets = Finder(first, second,sets)

    return result


def Prim(graph):
   
    global Counter
    costing = [float('inf') for i in range(Counter)]
    moves = [None for i in range(Counter)]

    starter = 0
    costing[starter] = 0
    moves[starter] = starter

    costN = [Kolejka.NodeList(key=i, priority=costing[i]) for i in range(0, Counter)]
    Kopiec = Kolejka.Kolejka(MyData=costN)

    been = []
    while not Kopiec.is_empty():
        first = Kopiec.pop().key
        for edge in graph.edges(first):
            if (first,edge[1]) in been or (edge[1],first) in been:
                continue
            been.append((first,edge[1]))
            been.append((edge[1],first))
            second = edge[1]
            weight = graph.get_edge_data(edge[0],edge[1])['weight']
            if costing[second] > weight:
                 costing[second] = weight
                 moves[second] = first
                 Kopiec.priority(second, costing[second])
        
    result = []
    for node in range(0, Counter):
        if node == starter:
            continue
        result.append(GraphEdge( moves[node], node, 0 if  moves[node] == node else graph.get_edge_data( moves[node],node)['weight']))

    return result

def readGraph():
    global Counter
    Graph = nx.Graph()
    nodes_count = int(input())
    Counter = nodes_count

    edges_count = int(input())

    for _ in range(edges_count):
        edge = input().split()
        first, second, weight =  int(edge[0]), int(edge[1]), Decimal(edge[2])
        Graph.add_edge(first, second, weight=weight)

    return Graph

if __name__ == "__main__":

    give = argv[1]
    graph = readGraph()
    
    if give == '-k':
        spanning_tree_edges = Kruskal(graph)
    else:
         spanning_tree_edges = Prim(graph)

    for edge in spanning_tree_edges:
        first, second = sorted([edge[0], edge[1]])
        weight = graph.get_edge_data(edge[0],edge[1])['weight']
        print(first, second, weight)
   
    print(sum(map(lambda x: graph.get_edge_data(x[0],x[1])['weight'], spanning_tree_edges)))