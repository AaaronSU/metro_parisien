#!/usr/bin/python3
import time
from os import system, name
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


def dijkstra(graph: Graph, start_node: int):
    dico = {node.get_id(): float('inf') for node in graph}
    dico[start_node] = 0

    nodes_visited = []

    pq = PriorityQueue()
    pq.put((0, start_node))

    while not pq.empty():
        (_, current_vertex) = pq.get()
        nodes_visited.append(current_vertex)

        current_vertex = graph.get_node(current_vertex)
        for neighbor in current_vertex:
            distance = Edge.get_weight_of_nodes(current_vertex, neighbor)
            if neighbor.get_id() not in nodes_visited:
                old_cost = dico[neighbor.get_id()]
                new_cost = dico[current_vertex.get_id()] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor.get_id()))
                    dico[neighbor.get_id()] = new_cost
                    neighbor.set_predecessor(current_vertex)
    return dico


def find_shortest_path(graph: Graph, start_node: int, destination: int) -> Optional[List[int]]:
    dico = dijkstra(graph, start_node)
    total_second = dico[destination]
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
    find_direction()
    return Line.get_line_list()


def find_direction():
    q = Queue()
    for line in Line.get_line_nodes():
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


def ask_line_number(msg_ask_line: str) -> str:
    line_number = input(msg_ask_line)
    if line_number in Line.get_line_number():
        return line_number
    clear()
    print("Votre saisir n'est pas bon.")
    print("Les choix suivants sont disponibles : ")
    print(list(Line.get_line_number()))
    return ask_line_number(msg_ask_line)


def ask_station_number(line_number: str, msg_print_line: str, msg_ask_station) -> int:
    clear()
    print(
        f"{msg_print_line} {line_number} qui ont pour les stations suivantes : ")
    list_station = []
    line = Line.get_line_stations(line_number)
    for station in line:
        list_station.append((station.get_id(), station.get_name()))
    list_station.sort()
    for station in list_station:
        station_id, station_name = station
        print(f"{station_id} : {station_name}")

    station_number = input(msg_ask_station)
    try:
        station_number = int(station_number)
    except:
        clear()
        print("Veuillez sélectionner un nombre...")
        time.sleep(1)
        return ask_station_number(line_number, msg_print_line, msg_ask_station)
    else:
        if line.get_node(station_number):
            return station_number
        clear()
        print("Veillez sélectionner un numéro de station valable...")
        time.sleep(1)
        return ask_station_number(line_number, msg_print_line, msg_ask_station)


def get_station(message: str):
    clear()
    if message == "départ":
        msg_ask_line = "Quelle est la ligne que vous êtes actuellement ?\n"
        msg_print_line = "Vous êtes actuellement à la ligne"
        msg_ask_station = "Quelle est la station que vous êtes actuellement ? (Veuillez sélectionner un numéro)\n"
    else:
        msg_ask_line = "Quelle est la ligne que vous voulez y aller ?\n"
        msg_print_line = "Vous voulez allé à la ligne"
        msg_ask_station = "Quelle est la station que vous voulez allez ? (Veuillez sélectionner un numéro)\n"
    line_number = ask_line_number(msg_ask_line)
    station_number = ask_station_number(
        line_number, msg_print_line, msg_ask_station)

    return station_number


def describe_trajet(graph: Graph, trajet: List[int], total_second: int):
    while len(trajet) > 1 and graph.get_node(trajet[0]).get_name() == graph.get_node(trajet[1]).get_name():
        trajet = trajet[1:]
    print(f"Vous êtes à {graph.get_node(trajet[0]).get_name()}.")
    line = graph.get_node(trajet[0]).get_line()
    first_phrase = True
    station_name = graph.get_node(trajet[0]).get_name()
    for i in range(2, len(trajet)-1):
        if trajet[i] not in Line.get_line_stations(line):
            edge = Edge.get_connection_between_nodes(
                graph.get_node(trajet[i-2]), graph.get_node(trajet[i-1]))

            station_line = graph.get_node(trajet[i-2]).get_line()
            list_directions = "/".join(edge.get_direction())
            if first_phrase:
                first_phrase = False
                print("Prenez la ligne %s direction %s." %
                      (station_line, list_directions))
                station_name = graph.get_node(trajet[i]).get_name()
            else:
                print("A %s, changez et prenez la ligne %s direction %s." %
                      (station_name, station_line, list_directions))
                station_name = graph.get_node(trajet[i]).get_name()
            line = graph.get_node(trajet[i]).get_line()
    if len(trajet) > 1:
        edge = Edge.get_connection_between_nodes(
            graph.get_node(trajet[-2]), graph.get_node(trajet[-1]))
        station_line = graph.get_node(trajet[i-2]).get_line()
        list_directions = "/".join(edge.get_direction())
    print("A %s, changez et prenez la ligne %s direction %s." %
          (station_name, station_line, list_directions))

    if total_second % 60:
        second = " et %s seconde" % (
            total_second % 60) + "s" if total_second % 60 > 0 else "" + "."
    else:
        second = ""
    print("Vous devriez arriver à %s dans %s minutes%s" %
          (graph.get_node(trajet[-1]).get_name(), total_second//60, second))


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == "__main__":
    metro_parisien = init()
    # print(is_connexe(metro_parisien))
    lines = initialize_metro_lines(metro_parisien)
    depart = get_station("départ")
    arrivee = get_station("arrivée")
    trajet, total_second = find_shortest_path(metro_parisien, depart, arrivee)
    clear()
    describe_trajet(metro_parisien, trajet, total_second)
