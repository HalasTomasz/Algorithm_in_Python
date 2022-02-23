from collections import namedtuple
import Kolejka
from sys import stderr
from time import time
import networkx as nx
from decimal import Decimal

Counter = 0

Result = namedtuple('Result', ['distance', 'moves'])


def Dijkstra_algorithm(graph, start):
    global Counter
    distance = [float('inf') for i in range(Counter)]
    moves = [None for i in range(Counter)]
    distance[start] = 0
    moves[start] = start

    distanceN = [Kolejka.NodeList(key=i, priority=distance[i]) for i in range(0, Counter)]
    Kopiec = Kolejka.Kolejka(MyData=distanceN)
 
    while not Kopiec.is_empty():
        first = Kopiec.pop().key
        for edge in graph.edges(first):
            second = edge[1]
            weight = graph.get_edge_data(edge[0],edge[1])['weight']
            if distance[second] > distance[first] + weight:
                 distance[second] = distance[first] + weight
                 moves[second] = first
                 if second in Kopiec.heap():
                     Kopiec.priority(second, distance[second])
                 else:
                     Kopiec.insert(second,distance[second])
 

    return Result(distance=distance, moves=moves)

def readGraph():
    global Counter
    Graph = nx.DiGraph()
    nodes_count = int(input())
    Counter = nodes_count
    edges_count = int(input())

    for _ in range(edges_count):
        edge = input().split()
        first, second, weight =  int(edge [0]), int(edge[1]), Decimal(edge[2])
        Graph.add_edge(first, second, weight=weight)

    return Graph

if __name__ == "__main__":

  
    graph = readGraph()
    start= int(input())
    begin = time()
    results = Dijkstra_algorithm(graph, start)
    
with open ("res.txt",'w') as test:
       
    end = time()

    for node in range(0, Counter):
    
        print(node, results.distance[node])
       
        mesure = [(node,0 if results.moves[node] == node else graph.get_edge_data(results.moves[node],node)['weight'])]

        curr = mesure[0]
        while curr[0] != start:
            curr = (results.moves[curr[0]], None)
            test.write(str(curr) +" " + str(results.distance[curr[0]]) + " ")
            mesure.insert(0,(curr[0],0 if results.moves[curr[0]] == curr[0] else graph.get_edge_data(results.moves[curr[0]],curr[0])['weight']))
    
        test.write("\n")
    test.close()
    print((end-begin), file=stderr)