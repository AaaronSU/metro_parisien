from typing import Any, List, NoReturn, Optional, Tuple
from node import Node


class Edge(object):
    """
    Class qui représente un Edge (arrête)
    Liaison entre deux stations de ligne de métro
    --------

    Attribut de la class Edge :

    edge_list: List
        Liste de tous les liaisons (Edge) entre deux noeuds
    -------

    Attributs :

    starting_node: Node
        Noeuds de départ
    arrival_node: Node
        Noeuds d'arrivé
    weight: int
        Poids de la liaison : distance entre les deux noeuds
    direction: None ou List[str]
    """

    edge_list: List = []

    def __init__(self, starting_node: Node, arrival_node: Node, weight: int, direction: Optional[str] = None):
        """
        Constructeur de la class Edge
        Rélève une exception si starting_node et arrival_node ne sont pas des instances de la class Node
        """
        if (not isinstance(starting_node, Node)) or (not isinstance(arrival_node, Node)):
            raise Exception("Invalid node for initialization")
        self.starting_node: Node = starting_node
        self.arrival_node: Node = arrival_node
        self.weight: int = weight
        self.direction: Optional[List[str]] = direction
        Edge.edge_list.append(self)

    def get_starting_node(self) -> Node:
        """
        Getter starting_node (obtenir station de départ du edge)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                starting_node (Node): station de départ 
        """
        return self.starting_node

    def set_starting_node(self, node: Node) -> NoReturn:
        """
        Setter starting_node (changer station de départ du edge)
        Rélève une exception si starting_node n'est pas une instance de la class Node
        ---------
            Paramètre:
            ---------
                starting_node (Node): Nouveau noeud de départ

            Retourne: Aucun retour
        """
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        self.starting_node = node

    def get_arrival_node(self) -> Node:
        """
        Getter arrival_node (obtenir station d'arrivé du edge)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                arrival_node (Node): Station d'arrivé
        """
        return self.arrival_node

    def set_arrival_node(self, node: Node) -> NoReturn:
        """
        Setter arrival_node (changer station d'arrivé du edge)
        Rélève une exception si starting_node n'est pas une instance de la class Node

            Paramètre:
            ---------
                arrival_node (Node): Nouvelle station d'arrivé

            Retourne: Aucun retour
        """
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        self.arrival_node = node

    def get_weight(self) -> int:
        """
        Getter weight (obtenir poid du edge)
        ---------
            Paramètre: Aucun paramètre necéssaire

            Retourne:
            ---------
                weight (int): Poids du edge, distance entre deux stations.
        """
        return self.weight

    def set_weight(self, weight: int) -> NoReturn:
        """
        Setter weight (changer poid du edge)
        ---------
            Paramètre:
            ---------
                weight (int): Nouveau poids du edge, distance entre deux noeuds

            Retourne: Aucun retour
        """
        self.weight = weight

    def get_direction(self) -> str:
        """
        Getter direction (obtenir direction du edge)
        ---------
            Paramètre: Aucun paramètre

            Retourne:
            ---------
                direction (str) :  ???
        """
        return self.direction

    def add_direction(self, direction: str) -> NoReturn:
        """
        ????
        ??? 
        ---------
            Paramètre:
            ---------
                direction (str) : ???
<<<<<<< HEAD

            Retourne : 
                None 
=======

            Retourne: Aucun retour
>>>>>>> f662777bac116ef2885c24fb989401fc36db61aa
        """
        if not self.direction:
            self.direction = [direction]
        else:
            self.direction.append(direction)

    def remove_direction(self, direction: str):
        """
        Supprime une direction  ????
        Rélève une exception si la direction n'existe pas dans le edge
<<<<<<< HEAD

            Parametre :
                direction (str) : ??? 

            Retourne : 
                None
=======
        ---------
            Paramètre:
            ---------
                direction (str) : ??? 

            Retourne: Aucun retour
>>>>>>> f662777bac116ef2885c24fb989401fc36db61aa
        """
        if direction not in self.direction:
            raise Exception("Direction doesn't exist in edge")
        self.direction.remove(direction)

    @classmethod
    def get_connection_between_nodes(cls, start_node: Node, end_node: Node) -> Any:
        """
<<<<<<< HEAD

=======
        Prends deux noeuds et renvoie la liaison entre les deux
        ---------
            Paramètre: 
            ---------
                start_node (Node):
                end_node (Node):

            Retourne:
            ---------
                edge (Edge): instance de la class Edge correcpondant
>>>>>>> f662777bac116ef2885c24fb989401fc36db61aa
        """
        for edge in Edge.get_edge_list():
            if edge.starting_node == start_node and edge.arrival_node == end_node:
                return edge

    @classmethod
    def get_connections_of_node(cls, node: Node) -> List[Tuple[Node, int, Optional[str]]]:
        """
        ??????
        ---------
            Paramètre: 
            ---------
                node (Node): ????

            Retourne:
            ---------
                list_connection (List[Tuple[Node, int, Optional[str]]]) : ???
        """
        list_connection = []
        for edge in cls:
            if edge.starting_node == node:
                list_connection.append(
                    (edge.arrival_node, edge.weight, edge.direction))
        return list_connection

    @staticmethod
    def get_weight_of_nodes(starting_node: Node, arrival_node: Node) -> Optional[int]:
        if not (isinstance(starting_node, Node) and isinstance(arrival_node, Node)):
            raise Exception("Invalid node")
        for edge in Edge.get_edge_list():
            if edge.starting_node == starting_node and edge.arrival_node == arrival_node:
                return edge.weight
        raise Exception("Edge doesn't exist in the list of Edges")

    @staticmethod
    def get_direction_of_nodes(starting_node: Node, arrival_node: Node) -> Optional[str]:
        if not (isinstance(starting_node, Node) and isinstance(arrival_node, Node)):
            raise Exception("Invalid node")
        for edge in Edge.get_edge_list():
            if edge.starting_node == starting_node and edge.arrival_node == arrival_node:
                return edge.direction
        raise Exception("Edge doesn't exist in the list of Edges")

    @classmethod
    def get_number_of_edge(cls) -> int:
        return len(cls.edge_list)

    @classmethod
    def get_edge_list(cls) -> List[Any]:
        return cls.edge_list

    def __iter__(self):
        return iter(Edge.edge_list)

    def __str__(self):
        return f"C'est un arc qui pars de {self.starting_node.name} et qui arrive à {self.arrival_node.name}, direction {self.direction} avec un poids de {self.weight}"
