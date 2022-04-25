import sys
from typing import List
from metro_line import Line
from queue import PriorityQueue, Queue
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
    for vertex_successor in vertex:
        if vertex_successor.name != vertex.name:
            counter += 1
            liste_connected.append(vertex.name)
    if counter == 1:
        terminus.append(liste_connected)
    for vertex_successor in vertex:
        if vertex_successor.color == "white" and vertex_successor.name != vertex.name:
            pp(graph, vertex_successor, stations_ligne, terminus)
    return stations_ligne, terminus


def bfs(graph: Graph, node: Node) -> None:
    for vertex in graph:
        vertex.set_color("white")
    if node.get_id() not in graph:
        raise Exception("Node not exist in graph")
    node.set_predecessor(None)
    vertQueue = Queue()
    vertQueue.put(node)
    while (not vertQueue.empty()):
        currentVert = vertQueue.get()
        for nbr in currentVert:
            if (nbr.get_color() == 'white'):
                nbr.set_color('gray')
                nbr.set_predecessor(currentVert)
                vertQueue.put(nbr)
        currentVert.set_color('black')


def is_connexe(graph: Graph):
    bfs(graph, graph.get_node(0))
    for vertex in graph:
        if vertex.color != "black":
            return False
    return True


def dijkstra(graph: Graph, start_node: Node):
    dico = {v: float('inf') for v in graph}
    dico[start_node] = 0

    nodes_visited = []

    pq = PriorityQueue()
    pq.put((0, start_node))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        nodes_visited.append(current_vertex)

        for neighbor in current_vertex:
            distance = Edge.get_weight_of_nodes(current_vertex, neighbor)
            if neighbor not in nodes_visited:
                old_cost = dico[neighbor]
                new_cost = dico[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    dico[neighbor] = new_cost
    return dico


"""metro_parisien = init()
print(is_connexe(metro_parisien))


lignes = dfs(metro_parisien)
for ligne, terminus in lignes:
    print(terminus)
    print({vertex.id: station for station, vertex in ligne.items()})
    print()"""


uvsq = Graph()
uvsq.add_node(1, "source")
uvsq.add_node(2, "s2")
uvsq.add_node(3, "s3")
uvsq.add_node(4, "s4")
uvsq.add_node(5, "s5")
uvsq.add_node(6, "s6")

uvsq.add_edge(1, 2, 4)
uvsq.add_edge(2, 4, 2)
uvsq.add_edge(1, 3, 8)
uvsq.add_edge(2, 3, 3)
uvsq.add_edge(1, 5, 11)
uvsq.add_edge(3, 4, 1)
uvsq.add_edge(4, 3, 2)
uvsq.add_edge(4, 5, 5)
uvsq.add_edge(3, 5, 2)
uvsq.add_edge(5, 6, 3)
uvsq.add_edge(4, 6, 7)

dico = dijkstra(uvsq, uvsq.get_node(1))
print(dico[uvsq.get_node(6)])
