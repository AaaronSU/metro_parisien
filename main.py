from typing import List, Mapping, NoReturn, Optional
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


def get_metro_lines(graph: Graph):
    for vertex in graph:
        vertex.color = "white"
    lines = []
    for vertex in graph:
        stations_ligne = {}
        terminus = {}
        if vertex.color == "white":
            stations_ligne, terminus = pp(
                graph, vertex, stations_ligne, terminus)
            lines.append([stations_ligne, terminus])
    return lines


def pp(graph: Graph, vertex: Node, stations_ligne: Mapping[int, Node], terminus: Mapping[int, Node]):
    stations_ligne[vertex.id] = vertex
    vertex.color = "black"

    counter = 0
    liste_connected = {}
    for vertex_successor in vertex:
        if vertex_successor.name != vertex.name:
            counter += 1
            liste_connected[vertex.id] = vertex
    if counter == 1:
        terminus.update(liste_connected)
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
                    neighbor.set_predecessor(current_vertex)
    return dico


def find_shortest_path(graph: Graph, start_node: int, destination: int) -> Optional[List[int]]:
    dico = dijkstra(graph, graph.get_node(start_node))
    total_second = dico[graph.get_node(destination)]
    liste = [destination]

    while graph.get_node(destination).get_predecessor():
        destination = graph.get_node(destination).get_predecessor().get_id()
        liste = [destination] + liste

    return liste, total_second


def initialize_metro_lines(graph: Graph) -> NoReturn:
    lines_info = [
        ("12", "#007852"),
        ("2", "#003CA6"),
        ("9", "#B6BD00"),
        ("4", "#CF009E"),
        ("3", "#837902"),
        ("1", "#FFCD00"),
        ("11", "#704B1C"),
        ("7", "#FA9ABA"),
        ("10", "#C9910D"),
        ("13", "#6EC4E8"),
        ("5", "#FF7E2E"),
        ("8", "#E19BDF"),
        ("6", "#6ECA97"),
        ("14", "#62259D"),
        ("7b", "#6ECA97"),
        ("3b", "#6EC4E8")
    ]
    metro_lines = get_metro_lines(graph)
    for index in range(len(lines_info)):
        line = Line(*lines_info[index])
        line_stations, terminus_list = metro_lines[index]
        for station in line_stations:
            line.add_node(station, line_stations[station])
        for terminus in terminus_list:
            line.add_terminus(terminus, terminus_list[terminus])
    # à ajouter le terminus pour une ligne de métro
    return Line.get_line_list()


metro_parisien = init()
print(is_connexe(metro_parisien))


lines = initialize_metro_lines(metro_parisien)

counter = 0
q = Queue()
for line in lines:
    for terminus in line.get_terminus_nodes():
        q.put(terminus)
        marked = [terminus]
        while not q.empty():
            station = q.get()
            for successeur in station:
                if successeur.name != station.name and successeur not in marked:
                    q.put(successeur)
                    marked.append(successeur)
                    edge = Edge.get_connection_between_nodes(
                        successeur, station)
                    edge.add_direction(terminus.name)


"""q = Queue()
counter = 0
for line in lines:
    for terminus in line.get_terminus_nodes():
        q.put(terminus)
        while not q.empty():
            station = q.get()
            for successeur in station:
                for edge in Edge.get_edge_list():
                    start_node = edge.get_starting_node()
                    end_node = edge.get_arrival_node()
                    if start_node.name == successeur.name and end_node.name == station.name and successeur.get_id() in line and start_node.name != end_node.name:
                        counter += 1
                        print(counter)
                        edge.add_direction(terminus)
                        q.put(successeur)

"""
for edge in Edge.get_edge_list():
    print(edge)

"""uvsq = Graph()
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

print(find_shortest_path(uvsq, 1, 6))
"""
