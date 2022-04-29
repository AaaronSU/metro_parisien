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
    node_list : Mapping[int: Node]
        Liste des noeuds du graphe, 
        clée : ID d'un noeud x 
        valeur : Adresse d'un noeud x, noeud x est une instance de la class Node
        (initialisé à vide)
    """
    # a revoir node_list

    def __init__(self):
        """
        Constructeur de la class Graph
        """
        self.number_of_node: int = 0
        self.node_list: Mapping[int, Node] = {}

    def get_number_of_node(self) -> int:
        """
        Getter number_of_node (obtenir nombre de noeuds du graphe)

            Parametre :
                None 

            Retourne :
                self.number_of_node (int) : Nombre de noeuds du graphe 
        """
        return self.number_of_node

    def set_number_of_node(self, number: int) -> NoReturn:
        """
        Setter number_of_node (changer nombre de noeuds du graphe)

            Parametre : 
                number (int) : nouveau nombre noeuds du graphe

            Retourne : 
                None
        """
        self.number_of_node = number

    def get_nodes(self) -> List[int]:
        """
        Getter nodes (obtenir noeuds du graphe par leur identifiant)

            Parametre :
                None 

            Retourne :
                [self.node_list.keys()] (List[int]) : liste ID des noeuds du graphe ??????????? #changer en liste, va rien faire ? 
        """
        return [self.node_list.keys()]

    def get_node(self, number_of_node: int) -> Optional[Node]:
        """
        number_of_node : Identifiant d'un noeud x (instance de la class Node)
        Si noeud dans le graphe, alors renvoie le noeud x et la liste connectedTo de la class Node du noeud x ???? #la liste des noeuds connectés au noeud x
        Sinon si l'identifiant n'est pas dans graphe, alors renvoie None

            Parametre :
                None 

            Retourne :
                [self.node_list.keys()] (List[int]) : liste ID des noeuds du graphe ??????????? #changer en liste, va rien faire ? 
        """
        if number_of_node in self:
            return self.node_list[number_of_node]
        else:
            return None

    def add_node(self, number_of_node: int, name_of_node: str) -> NoReturn:
        """
        Ajoute un nouveau noeud dans le graphe
        Augmente le number_of_node par 1

            Parametre : 
                number_of_node (int) : Identifiant du nouveau noeud à ajouter 
                name_of_node (str) : Nom du nouveau noeud à ajouter 

            Retourne : 
                None
        """
        self.node_list[number_of_node] = Node(number_of_node, name_of_node)
        self.number_of_node += 1

    def remove_node(self, number_of_node: int) -> Node:
        """
        Supprime un noeud du graphe 
        Rélève une exception si le noeud n'est pas dans le graphe 

            Parametre : 
                number_of_node (int): Identifiant du noeud à supprimer

            Retourne : 
                None
        """
        if number_of_node in self:
            return self.node_list.pop(number_of_node)
        raise Exception("Node not exist in Graph")

    def add_edge(self, node1: int, node2: int, weight: int) -> Edge:
        # Rajouter une exception si node1 et node2 ne sont pas dans le graphe ? OU ca sert à rien ?
        """ if node1 in self and node2 in self: 
                blabla 
            raise Exception("Node not exist in Graphe")
        """
        """
            Parametre : 
                node1 (int) : Identifiant du noeud 1
                node2 (int) : Identifiant du noeud 2
                weight (int) : Poids du Edge, distance entre noeud 1 et noeud 2

            Retourne : 
                Edge(self.get_node(node1), self.get_node(node2), weight) (Edge) : crée une instance de la class Edge ??????
        """
        self.get_node(node1).add_connection(node2, self.get_node(node2))
        return Edge(self.get_node(node1), self.get_node(node2), weight)

    def __contains__(self, number_of_node: int):
        return number_of_node in self.node_list.keys()

    def __iter__(self):
        return iter(self.node_list.values())
