from typing import Mapping, NoReturn, Optional, List, Any
import sys


class Node(object):
    """
    Class qui représente un noeud ( un sommet )

    Attributs : 
    id  : int 
        Identifiant du noeud
    name : str
        Nom du noeud 
    color : str 
        Couleur du noeud, par défault blanc
    predecessor : Node
        ????
    distance : int 
        ????
    connectedTo : dictionnaire (clée : ID noeuds, valeur : Node)
        Noeuds connectés 


    """

    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name
        self.color: str = "white"
        self.predecessor: Optional[Any] = None
        self.distance: int = sys.maxsize
        self.connectedTo: Mapping[int, Any] = {}

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int) -> NoReturn:
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> NoReturn:
        self.name = name

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str) -> NoReturn:
        self.color = color

    def get_predecessor(self) -> Optional[Any]:
        return self.predecessor

    def set_predecessor(self, predecessor: Any) -> NoReturn:
        self.predecessor = predecessor

    def get_distance(self) -> int:
        return self.distance

    def set_distance(self, distance: int) -> NoReturn:
        self.distance = distance

    def get_connections(self) -> List[int]:
        return self.connectedTo.keys()

    def add_connection(self, number_of_node: int, connection: Any) -> NoReturn:
        if isinstance(connection, Node):
            if connection.id != number_of_node:
                raise Exception("Id doen't match")
            self.connectedTo[number_of_node] = connection

    def remove_connection(self, number_of_node: int):
        if number_of_node in self:
            self.connectedTo.pop(number_of_node)
        raise Exception("Connection not exist in node")

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self])

    def __iter__(self):
        return iter(self.connectedTo.values())

    def __contains__(self, number_of_node: int):
        return number_of_node in self.connectedTo.keys()
