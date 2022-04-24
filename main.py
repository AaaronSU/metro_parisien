from typing import List
from metro_line import Line
from queue import Queue
from graph import Graph
from node import Node
from edge import Edge


def init():
    graph = Graph()
    with open('metro.txt', 'r') as f:
        while 1:
            line = f.readline()
            if line == '':
                break
            line = line[:-1]
            if line[0] == 'V':
                line = line.split(" ", 2)
                vertex, vertex_name = int(line[1]), line[2]
                graph.add_node(vertex, vertex_name)
            if line[0] == 'E':
                line = line.split(" ", 3)
                vertex1, vertex2, weight = [
                    int(element) for element in line[1:]]
                graph.add_edge(vertex1, vertex2, weight)
                graph.add_edge(vertex2, vertex1, weight)
    return graph


def dfs(graph: Graph):
    for vertex in graph:
        vertex.color = "white"
    dico = []
    for vertex in graph:
        stations_ligne = {}
        terminus = []
        if vertex.color == "white":
            stations_ligne, terminus = pp(
                graph, vertex, stations_ligne, terminus)
            dico.append([stations_ligne, terminus])
    return dico


def pp(graph: Graph, vertex: Node, stations_ligne: List[Node], terminus):
    stations_ligne[vertex.name] = vertex
    vertex.color = "black"

    counter = 0
    liste_connected = []
    for vertex_successor in vertex.connectedTo:
        if vertex_successor.name != vertex.name:
            counter += 1
            liste_connected.append(vertex.name)
    if counter == 1:
        terminus.append(liste_connected)
    for vertex_successor in vertex.connectedTo:
        if vertex_successor.color == "white" and vertex_successor.name != vertex.name:
            pp(graph, vertex_successor, stations_ligne, terminus)
    return stations_ligne, terminus


def bfs(graph: Graph, node: Node) -> None:
    if node.get_id() not in graph:
        raise Exception("Node not exist in graph")
    node.set_predecessor(None)
    vertQueue = Queue()
    vertQueue.put(node)
    while (not vertQueue.empty()):
        currentVert = vertQueue.get()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setPred(currentVert)
                vertQueue.put(nbr)
        currentVert.setColor('black')


metro_parisien = init()

lignes = dfs(metro_parisien)
for ligne, terminus in lignes:
    print(terminus)
    print({vertex.id: station for station, vertex in ligne.items()})
    print()
