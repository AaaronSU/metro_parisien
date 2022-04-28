from typing import Mapping, NoReturn, List, Optional
from edge import Edge
from node import Node


class Graph:
    """
    --------
    Class qui représente un graphe
    --------

    Attributs :

    number_of_node : int
        Nombre de noeuds du graphe 
        (initialisé à 0)
    node_list : dictionnaire {int: Node}
        Liste des noeuds du graphe, 
        clée : ID d'un noeud x 
        valeur : Adresse d'un noeud x, noeud x est une instance de la class Node
        (initialisé à vide)
    """

    def __init__(self):
        """
        Constructeur de la class Graph
        """
        self.number_of_node: int = 0
        self.node_list: Mapping[int, Node] = {}

    def get_number_of_node(self) -> int:
        """
        Getteur number_of_node

            Parametre :
                None 

            Retourne :
                self.number_of_node (int) : Nombre de noeuds du graphe 
        """
        return self.number_of_node

    def set_number_of_node(self, number: int) -> NoReturn:
        self.number_of_node = number

    def get_nodes(self) -> List[int]:
        """
        Getteur nodes

            Parametre :
                None 

            Retourne :
                self.get_nodes (List[int]) : liste ID des noeuds du graphe
        """
        return self.node_list.keys()

    def get_node(self, number_of_node: int) -> Optional[Node]:
        """  
        """
        if number_of_node in self:
            return self.node_list[number_of_node]
        else:
            return None

    def add_node(self, number_of_node: int, name_of_node: str) -> NoReturn:
        self.node_list[number_of_node] = Node(number_of_node, name_of_node)
        self.number_of_node += 1

    def remove_node(self, number_of_node: int) -> Node:
        if number_of_node in self:
            return self.node_list.pop(number_of_node)
        raise Exception("Node not exist in Graph")

    def add_edge(self, node1: int, node2: int, weight: int) -> Edge:
        self.get_node(node1).add_connection(node2, self.get_node(node2))
        return Edge(self.get_node(node1), self.get_node(node2), weight)

    def __contains__(self, number_of_node: int):
        return number_of_node in self.node_list.keys()

    def __iter__(self):
        return iter(self.node_list.values())
