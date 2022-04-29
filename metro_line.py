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
        --------
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
                self.color (str): couleur de la ligne de métro
        """
        return self.color

    def set_color(self, color: str) -> NoReturn:
        """
        Setter numero (changer le numero de la ligne)
        --------
            Paramètre:
            --------
                color (str): nouvelle couleur de la ligne 

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
                self.node_list.keys (List[int]) : Liste des identifiants des stations (Node) de la ligne de métro
        """
        return self.node_list.keys()

    def get_node(self, number_of_node: int) -> Optional[Node]:
        """
        Si noeud, ayant pour identifiant number_of_node, dans ligne alors retourne l'adresse du noeud
        Sinon, retourne None
        --------
            Paramètre:
            --------
                number_of_node : Identifiant du noeud (node) cherché

            Retourne:
            --------
                self.node_list[number_of_node]
        """
        if number_of_node in self.get_nodes():
            return self.node_list[number_of_node]
        else:
            return None

    def add_node(self, number_of_node: int, node: Node) -> NoReturn:
        """
        Ajoute un noeud à la ligne de métro
        --------
            Paramètre:
            --------
                number_of_node (int): Identifiant du noeud (node)
                node (Node) : Adresse en mémoire du noeud

            Retourne: Aucun retour
        """
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        node.set_line(self.numero)
        self.node_list[number_of_node] = node
        self.number_of_node += 1

    def remove_node(self, number_of_node: int) -> Node:
        """
        Supprime un noeud à la ligne de métro
        --------
            Paramètre:
            --------
                number_of_node (int): Identifiant du noeud (node)

            Retourne:
            --------
                node_list (list): nouvel liste node_list sans noeud supprimé

        """
        if number_of_node not in self:
            raise Exception("Number of node not exist in metro line")
        self.number_of_node -= 1
        return self.node_list.pop(number_of_node)

    def get_number_of_node(self) -> int:
        """
        Getteur number_of_node (obtenir nombre de station dans ligne)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                number_of_node (int): nombre de station de la ligne de métro

        """
        return self.number_of_node

    def set_number_of_node(self, number_of_node: int) -> NoReturn:
        """
        Setter number_of_node (changer le nombre de station de la ligne)
        --------
            Paramètre:
            --------
                number_of_node (str): nouveau nombre de station de la ligne 

            Retourne: Aucun retour
        """
        self.number_of_node = number_of_node

    def get_terminus_nodes(self) -> List[Node]:
        """
        Getteur terminus_node (obtenir terminus de la ligne de métro)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                terminus_node (list): Liste des noeud terminus de la ligne de métro

        """
        return self.terminus.values()

    def get_terminus_number(self) -> List[int]:
        """
        Getteur terminus_number (obtenir l'identifiant des terminus)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                terminus_number (int): identifiant des terminus d'une ligne de métro

        """
        return self.terminus.keys()

    def get_terminus(self) -> Iterator:
        """
        Getteur terminus (obtenir nombre de station dans ligne)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                terminus_number, terminus_nodes (iterator): identifiant d'un terminus et son adresse

        """
        return iter(zip(self.get_terminus_number(), self.get_terminus_nodes()))

    def add_terminus(self, number_of_node: int, node: Node) -> NoReturn:
        """
        Ajoute un terminus à une ligne de métro
        Rélève une exception si terminus n'est pas un node
        --------
            Paramètre:
            --------
                number_of_node (int): identifiant du Terminus
                node (Node): Adresse du noeud

            Retourne: Aucun retour
        """
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        self.terminus[number_of_node] = node

    def remove_terminus(self, number_of_node: int) -> Node:
        """
        Supprime un terminus à une ligne de métro
        Rélève une exception si terminus n'est pas dans la liste des terminus de la ligne
        --------
            Paramètre:
            --------
                number_of_node (int): identifiant du Terminus

            Retourne: Aucun retour
        """
        if number_of_node in self:
            return self.terminus.pop(number_of_node)
        raise Exception("Node doesn't exist in terminus of the line")

    @classmethod
    def get_line_list(cls) -> Mapping[str, Any]:
        """
        Getteur line_list (obtenir la liste des lignes)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                line_list (list): tous les instances de la ligne de métro

        """
        return cls.line_list

    @classmethod
    def get_line_number(cls) -> List[str]:
        """
        Getteur line_number (obtenir la liste des numéros de lignes)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                line_number (list): Le numero de tous les instances de la class line

        """
        return cls.line_list.keys()

    @classmethod
    def get_line_nodes(cls) -> List[Any]:
        """
        Getteur line_nodes (obtenir les adresses de toutes les lignes)
        --------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            --------
                line_values (list): Les adresses de tous les instances crée de la ligne de métro

        """
        return cls.line_list.values()

    @classmethod
    def get_line_stations(cls, line_number: str) -> Optional[List[Node]]:
        """
        Getteur line_stations (obtenir les stations d'une ligne de métro)
        --------
            Paramètre:
            --------
                line_number (str): Numéro de la ligne de métro

            Retourne:
            --------
                line_station (list[Node]): Liste des adresses stations de métros désservi par la ligne de métro
                None: L'instance de la ligne de métro possèdant le numero line_number non existant
        """
        if line_number in Line.get_line_number():
            return Line.line_list[line_number]
        return None

    def __iter__(self):
        return iter(self.node_list.values())

    def __contains__(self, number_of_node):
        return number_of_node in self.get_nodes()
