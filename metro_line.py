<<<<<<< HEAD
from typing import Any, List, Iterator, Mapping, NoReturn, Optional
from node import Node


class Line(object):
    """
    Class qui représente une ligne de métro
    --------
    Attribut de la class Line:
    --------
        line_list: Mapping[str, Line]
            Dictionnaire de tous les lignes de métro crée (tous les instances de Line crée)
            Clée: numero de la ligne de métro 
            Valeur: adresse de la ligne de métro

    Attributs:
    --------
        numero: str 
            Numero de la ligne de métro
        color: str
            Couleur de la ligne de métro
        node_list: Mapping[int: Node]
            Dictionnaire des stations de métro (Node) de la ligne
            Clé: Identifiant du noeud 
            Valeur: Adresse du noeud 
            (initialisé à vide)
        number_of_node: int
            Nombre de station de métro (Node) de la ligne
            (initialisé à vide)
        terminus: Mapping[int: Node]
            Dictionnaire des stations (Node) de terminus de la ligne
            Clé: Identifiant du noeud 
            Valeur: Adresse du noeud
            (initialisé à vide)
    """
    line_list: Mapping[str, Any] = {}

    def __init__(self, numero: str, color: str):
        """
        Constructeur de la class Line
        """
        self.numero: str = numero
        self.color: str = color
        self.node_list: Mapping[int: Node] = {}
        self.number_of_node: int = 0
        self.terminus: Mapping[int: Node] = {}
        Line.line_list[numero] = self

    def get_numero(self) -> int:
        """
        Getter numero (obtenir le numero de la ligne)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
                numero (int): numero de la ligne
        """
        return self.numero

    def set_numero(self, numero: str) -> NoReturn:
        """
        Setter numero (changer le numero de la ligne)

            Paramètre:
                numero (int): nouveau numero de la ligne 

            Retourne: Aucun retour
        """
        self.numero = numero

    def get_color(self) -> str:
        """
        Getter color (obtenir couleur de la ligne)

            Paramètre: Aucun paramètre nécessaire

            Retourne:
                self.color (str) : couleur de la ligne de métro
        """
        return self.color

    def set_color(self, color: str) -> NoReturn:
        self.color = color

    def get_nodes(self) -> List[int]:
        """
        Getter nodes (obtenir les stations (Node), par leur identifiant, de la ligne de métro)

            Parametre: 
                None 

            Retourne:
                self.node_list.keys (List[int]) : Liste des identifiants des stations (Node) de la ligne de métro
        """
        return self.node_list.keys()

    def get_node(self, number_of_node: int) -> Optional[Node]:
        """
        Si noeud, ayant pour identifiant number_of_node, dans ligne alors retourne le noeud et la liste 
        Sinon, retourne None

            Parametre : 
                number_of_node : Identifiant du noeud (node) cherché
            
            Retourne:
                self.node_list[number_of_node]
        """
        if number_of_node in self.get_nodes():
            return self.node_list[number_of_node]
        else:
            return None

    def add_node(self, number_of_node: int, node: Node) -> NoReturn:
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        node.set_line(self.numero)
        self.node_list[number_of_node] = node
        self.number_of_node += 1

    def remove_node(self, number_of_node: int) -> Node:
        if number_of_node not in self:
            raise Exception("Number of node not exist in metro line")
        self.number_of_node -= 1
        return self.node_list.pop(number_of_node)

    def get_number_of_node(self) -> int:
        return self.number_of_node

    def set_number_of_node(self, number_of_node: int) -> NoReturn:
        self.number_of_node = number_of_node

    def get_terminus_nodes(self) -> List[Node]:
        return self.terminus.values()

    def get_terminus_number(self) -> List[int]:
        return self.terminus.keys()

    def get_terminus(self) -> Iterator:
        return iter(zip(self.get_terminus_number(), self.get_terminus_nodes()))

    def add_terminus(self, number_of_node: int, node: Node) -> NoReturn:
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        self.terminus[number_of_node] = node

    def remove_terminus(self, number_of_node: int) -> Node:
        if number_of_node in self:
            return self.terminus.pop(number_of_node)
        raise Exception("Node doesn't exist in terminus of the line")

    @classmethod
    def get_line_list(cls) -> Mapping[str, Any]:
        return cls.line_list

    @classmethod
    def get_line_number(cls) -> List[str]:
        return cls.line_list.keys()

    @classmethod
    def get_line_nodes(cls) -> List[Any]:
        return cls.line_list.values()

    @classmethod
    def get_line_stations(cls, line_number: str) -> Optional[List[Node]]:
        if line_number in Line.get_line_number():
            return Line.line_list[line_number]
        return None

    def __iter__(self):
        return iter(self.node_list.values())

    def __contains__(self, number_of_node):
        return number_of_node in self.get_nodes()
=======
from typing import Any, List, Iterator, Mapping, NoReturn, Optional
from node import Node


class Line(object):
    """
    Class qui représente une ligne de métro
    --------
    Attribut de la class Line:
    --------
        line_list: Mapping[str, Line]
            Dictionnaire de tous les lignes de métro crée (tous les instances de Line crée)
            Clée: numero de la ligne de métro 
            Valeur: adresse de la ligne de métro

    Attributs:
    --------
        numero: str 
            Numero de la ligne de métro
        color: str
            Couleur de la ligne de métro
        node_list: Mapping[int: Node]
            Dictionnaire des stations de métro (Node) de la ligne
            Clé: Identifiant du noeud 
            Valeur: Adresse du noeud 
            (initialisé à vide)
        number_of_node: int
            Nombre de station de métro (Node) de la ligne
            (initialisé à vide)
        terminus: Mapping[int: Node]
            Dictionnaire des stations (Node) de terminus de la ligne
            Clé: Identifiant du noeud 
            Valeur: Adresse du noeud
            (initialisé à vide)
    """
    line_list: Mapping[str, Any] = {}

    def __init__(self, numero: str, color: str):
        """
        Constructeur de la class Line
        """
        self.numero: str = numero
        self.color: str = color
        self.node_list: Mapping[int: Node] = {}
        self.number_of_node: int = 0
        self.terminus: Mapping[int: Node] = {}
        Line.line_list[numero] = self

    def get_numero(self) -> int:
        """
        Getter numero (obtenir le numero de la ligne)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                numero (int): numero de la ligne
        """
        return self.numero

    def set_numero(self, numero: str) -> NoReturn:
        """
        Setter numero (changer le numero de la ligne)

            Paramètre:
            --------
                numero (int): nouveau numero de la ligne 

            Retourne: Aucun retour
        """
        self.numero = numero

    def get_color(self) -> str:
        """
        Getter color (obtenir couleur de la ligne)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                color (str) : couleur de la ligne de métro
        """
        return self.color

    def set_color(self, color: str) -> NoReturn:
        """
        Setter color (changer couleur de la ligne)
        --------
            Paramètre:
            --------
                color (str): nouvelle couleur de la ligne de métro

            Retourne: Aucun retour 
        """
        self.color = color

    def get_nodes(self) -> List[int]:
        """
        Getter nodes (obtenir les stations (Node), par leur identifiant, de la ligne de métro)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                node_list.keys (List[int]): Liste des identifiants des stations (Node) de la ligne de métro
        """
        return self.node_list.keys()

    def get_node(self, number_of_node: int) -> Optional[Node]:
        """
        Si noeud, ayant pour identifiant number_of_node, dans ligne alors retourne le noeud et la liste 
        Sinon, retourne None

            Paramètre:
            -------- 
                number_of_node: Identifiant du noeud (node) cherché
            
            Retourne:
            --------
                node_list[number_of_node] : 
        """
        if number_of_node in self.get_nodes():
            return self.node_list[number_of_node]
        else:
            return None

    def add_node(self, number_of_node: int, node: Node) -> NoReturn:
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        node.set_line(self.numero)
        self.node_list[number_of_node] = node
        self.number_of_node += 1

    def remove_node(self, number_of_node: int) -> Node:
        if number_of_node not in self:
            raise Exception("Number of node not exist in metro line")
        self.number_of_node -= 1
        return self.node_list.pop(number_of_node)

    def get_number_of_node(self) -> int:
        """
        Getter number_of_node (le nombre de station de la ligne)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                number_of_node (int): numero de la ligne
        """
        return self.number_of_node

    def set_number_of_node(self, number_of_node: int) -> NoReturn:
        self.number_of_node = number_of_node

    def get_terminus_nodes(self) -> List[Node]:
        """
        Getter numero (obtenir le numero de la ligne)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                numero (int): numero de la ligne
        """
        return self.terminus.values()

    def get_terminus_number(self) -> List[int]:
        return self.terminus.keys()

    def get_terminus(self) -> Iterator:
        return iter(zip(self.get_terminus_number(), self.get_terminus_nodes()))

    def add_terminus(self, number_of_node: int, node: Node) -> NoReturn:
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        self.terminus[number_of_node] = node

    def remove_terminus(self, number_of_node: int) -> Node:
        if number_of_node in self:
            return self.terminus.pop(number_of_node)
        raise Exception("Node doesn't exist in terminus of the line")

    @classmethod
    def get_line_list(cls) -> Mapping[str, Any]:
        return cls.line_list

    @classmethod
    def get_line_number(cls) -> List[str]:
        return cls.line_list.keys()

    @classmethod
    def get_line_nodes(cls) -> List[Any]:
        return cls.line_list.values()

    @classmethod
    def get_line_stations(cls, line_number: str) -> Optional[List[Node]]:
        if line_number in Line.get_line_number():
            return Line.line_list[line_number]
        return None

    def __iter__(self):
        return iter(self.node_list.values())

    def __contains__(self, number_of_node):
        return number_of_node in self.get_nodes()
>>>>>>> 708821e2a10accac15daa7042ba911bf72da1a5c
