#!/usr/bin/python3
from ctypes import Union
import time
from os import system, name
from typing import List, Mapping, NoReturn, Optional, Sequence
from metro_line import Line
from queue import PriorityQueue, Queue
from graph import Graph
from node import Node
from edge import Edge


def init() -> Graph:
    """
    Cré le graphe du réseau métro parisien d'après les données du fichier "metro.txt"
    --------- 
        Paramètre: Aucun paramètre nécessaire

        Retourne:
        ---------
            graph (Graph): graphe du métro parisien
    """
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


def get_metro_lines(graph: Graph) -> List[Sequence[Mapping[int, Node]]]:
    """
    Crée des lignes de métro d'après un graphe en faisant un parcours en profondeur
    --------- 
        Paramètre:
        ---------
            graph (Graph): graphe représentant un réseau métro

        Retourne:
        ---------
            lines (List): liste des stations de métro composant la ligne de métro
    """
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
    """
    pp : Parcours en profondeur.
    Permets de faire le parcours en profondeur d'un graphe.
    --------- 
        Paramètre:
        ---------
            graph (Graph): graphe qui représente un réseau métro.
            vertex (Node): station de métro.
            stations_ligne (Mapping[int, Node]): les identifiants et l'adresse de toutes les stations de la ligne.
            terminus (Mapping[int, Node]): identifiants et adresses de tous les terminus de la ligne après le traitement.
        Retourne:
        --------
            stations_ligne (Mapping[int, Node]): identifiants et adresses de toutes les stations de la ligne après le traitement.
            terminus (Mapping[int, Node]): identifiants et adresses de tous les terminus de la ligne après le traitement.
    """
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
    """
    bfs : Parcours en largeur.
    marque la couleur du noeud en noir si il existe une liaison possible en partant de la station de départ.
    ---------
        Paramètre:
        ---------
            graph (Graph): graphe qui représente un réseau métro.
            node (Node): station de métro.
        Retourne:
        --------
            None
    """
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


def is_connexe(graph: Graph) -> bool:
    """
    Retourner si un graphe est connexe (marche que dans le cas non orienté)
    ---------
        Paramètre:
        ---------
            graph (Graph): graphe qui représente un réseau métro.
        Retourne:
        --------
            retourne True si le graphe est connexe et False sinon
    """
    bfs(graph, graph.get_node(0))
    for vertex in graph:
        if vertex.color != "black":
            return False
    return True


def dijkstra(graph: Graph, start_node: int) -> Mapping[int: Union[float, int]]:
    """
    L'implémentation de l'algorithme de Dijkstra permettant de trouver le plus court chemin d'un point aux tous les autres points.
        ---------
        Paramètre:
        ---------
            graph (Graph): graphe qui représente un réseau métro.
            start_node (int): identifiant unique d'une station
        Retourne:
        --------
            retourne True si le graphe est connexe et False sinon

    """
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


def find_shortest_path(graph: Graph, start_node: int, destination: int) -> Sequence[List[int], int]:
    """
    En récupérant le dictionnaire retourné par l'algorithme de Dijkstra avec start_node, trouver le plus chemin pour aller de la destination en remontant dans le prédécesseur de la destination
        ---------
        Paramètre:
        ---------
            graph (Graph): graphe qui représente un réseau métro.
            start_node (int): identifiant unique de la station de départ
            destionation (int): identifiant unique de la station d'arrivée
        Retourne:
        --------
            liste (List[int]): liste des sommets passant pour aller du sommet de départ au sommet d'arrivée
            total_second: nombre total de seconde pour aller du sommet de départ au sommet d'arrivée

    """
    dico = dijkstra(graph, start_node)
    total_second = dico[destination]
    liste = [destination]

    while graph.get_node(destination).get_predecessor():
        destination = graph.get_node(destination).get_predecessor().get_id()
        liste = [destination] + liste

    return liste, total_second


def initialize_metro_lines(graph: Graph) -> List[Line]:
    """
    Instancie les lignes de métro en faisant appel à la fonction get_metro_lines(graph)
        ---------
        Paramètre:
        ---------
            graph (Graph): graphe qui représente un réseau métro.
        Retourne:
        --------
            (List[Line]) retourner les adresses de tous les lignes de métro dans le graphe

    """
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


def find_direction() -> NoReturn:
    """
    Pour toutes les liaisons entre deux stations des lignes de métro, trouver la direction de cette liaison, c'est-à-dire le terminus de cette liaison.
    """
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
    """
    Demande à l'utilisateur de rentrer une ligne de métro valable. Si les données ne sont pas valables, redemande jusqu'à ce soit valable.
        ---------
        Paramètre:
        ---------
            msk_ask_line (str): le message à afficher
        Retourne:
        --------
            retourner le numéro de la ligne 

    """
    line_number = input(msg_ask_line)
    if line_number in Line.get_line_number():
        return line_number
    clear()
    print("Votre saisir n'est pas bon.")
    print("Les choix suivants sont disponibles : ")
    print(list(Line.get_line_number()))
    return ask_line_number(msg_ask_line)


def ask_station_number(line_number: str, msg_print_line: str, msg_ask_station) -> int:
    """
    Idem pour le numéro dans la ligne de métro.
        ---------
        Paramètre:
        ---------
            line_number: Le numéro de la ligne du métro
            msg_print_line: Le message à afficher
            msg_ask_station : Le message à afficher
        Retourne:
        --------
            retourner le numéro de la ligne

    """

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


def get_station(message: str) -> int:
    """
        Obtenir une station de métro valable
        ---------
        Paramètre:
        ---------
            message(str) : message à afficher
        Retourne:
        --------
            (int) : retourne le numéro d'une station qui existe dans le graphe

    """
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


def describe_trajet(graph: Graph, trajet: List[int], total_second: int) -> NoReturn:
    """
    décrire le trajet pour le plus court chemin
    --------- 
        Paramètre:
        --------- 
        graph (Graph): graphe qui représente un réseau métro
        liste (List[int]): liste des sommets passant pour aller du sommet de départ au sommet d'arrivée
        total_second: nombre total de seconde pour aller du sommet de départ au sommet d'arrivée

        Retourne:
        ---------
            None
    """
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
    """
    efface les contenus sur le terminal
    """
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
