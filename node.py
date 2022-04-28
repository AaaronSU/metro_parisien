from typing import Mapping, NoReturn, Optional, List, Any
import sys

from pyparsing import line


class Node(object):
    """
    --------
    Class qui représente un noeud ( un sommet )
    --------

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
    connectedTo : dicitonnaire {int: Node}
        Liste des noeuds x connecté au noeud (self), 
        clée : ID d'un noeud x 
        valeur : Adresse d'un noeud x, noeud x est une instance de la class Node 
    """

    def __init__(self, id: int, name: str):
        """
        Constructeur des attributs de la class Node
        """
        self.id: int = id
        self.name: str = name
        self.color: str = "white"
        self.predecessor: Optional[Any] = None
        self.distance: int = sys.maxsize
        self.line: str = None
        self.connectedTo: Mapping[int, Any] = {}

    def get_id(self) -> int:
        """
        Getteur ID

            Parametre :
                None 

            Retourne :
                self.id (int) : ID du noeud 
        """
        return self.id

    def set_id(self, id: int) -> NoReturn:
        """
        Setteur ID 

            Parametre :
                id (int) : nouveau ID du noeud

            Retourne : 
                None
        """
        self.id = id

    def get_name(self) -> str:
        """
        Getteur name

            Parametre :
                None 

            Retourne :
                self.name (str) : nom du noeud 
        """
        return self.name

    def set_name(self, name: str) -> NoReturn:
        """
        Setteur name

            Parametre :
                name (str) : nouveau nom du noeud

            Retourne : 
                None
        """
        self.name = name

    def get_color(self) -> str:
        """
        Getteur color

            Parametre :
                None 

            Retourne :
                self.color (str) : couleur du noeud 
        """
        return self.color

    def set_color(self, color: str) -> NoReturn:
        """
        Setteur color

            Parametre :
                color (str) : nouveau couleur du noeud

            Retourne : 
                None
        """
        self.color = color

    def get_predecessor(self) -> Optional[Any]:
        """
        Getteur predecessor

            Parametre :
                None 

            Retourne :
                self.predecessor (Node) : ???? du noeud 
        """
        return self.predecessor

    def set_predecessor(self, predecessor: Any) -> NoReturn:
        """
        Setteur predecessor

            Parametre :
                predecessor (Node) : ???  du noeud

            Retourne : 
                None
        """
        self.predecessor = predecessor

    def get_distance(self) -> int:
        """
        Getteur distance

            Parametre :
                None 

            Retourne :
                self.distance (int) : ???? du noeud 
        """
        return self.distance

    def set_distance(self, distance: int) -> NoReturn:
        """
        Setteur distance

            Parametre :
                distance (int) : ???

            Retourne : 
                None
        """
        self.distance = distance

    def get_line(self) -> Optional[str]:
        return self.line

    def set_line(self, line: str) -> NoReturn:
        self.line = line

    def get_connections(self) -> List[int]:
        """
        Getteur connections

            Parametre :
                None 

            Retourne :
                self.connectedTo.keys() List[int] : Liste ID des noeuds connectés au noeud ( self )  
        """
        return [self.connectedTo.keys()]

    def add_connection(self, number_of_node: int, connection: Any) -> NoReturn:
        """
        Ajoute un noeud x (Node) au dictionnaire connectedTo 
        Ainsi le nouveau noeud x sera connecté au noeud (self)
        Rélève une execption si ID du nouveau noeud x et number_od_node ne correspondent pas

            Parametre : 
                number_of_node (int) : Identifiant du nouveau noeud connecté
                connection (Node) : adresse du noeud connecté  ???

            Retourne : 
                None 
        """
        if isinstance(connection, Node):
            if connection.id != number_of_node:
                raise Exception("Id doen't match")
            self.connectedTo[number_of_node] = connection

    def remove_connection(self, number_of_node: int):
        """ 
        Supprime l'item de connectedTo (dictionnaire) correspondant au number_of_node
        Ainsi, supprime un noeud x connecté au noeud (self)
        Rélève une exception si le number_of_node n'est pas dans connectedTo

            Parametre : 
                number_of_node ( int ) : Identifiant du noeud connecté

            Retourne : 
                None

        """
        if number_of_node in self:
            self.connectedTo.pop(number_of_node)
        raise Exception("Connection not exist in node")

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self])

    def __iter__(self):
        return iter(self.connectedTo.values())

    def __contains__(self, number_of_node: int):
        return number_of_node in self.connectedTo.keys()
