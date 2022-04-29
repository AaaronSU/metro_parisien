from typing import Mapping, NoReturn, Optional, List, Any


class Node(object):
    """
    Class qui représente un noeud (un sommet)
    Noeud = une station de métro
    --------
    Attributs:
    ---------
        id: int 
            Identifiant du noeud
        name: str
            Nom du noeud 
        color: str 
            Couleur du noeud
            (initialisation: "white")
        predecessor: Node
            Prédécesseur du noeud
            (initialisation: None)
        line: str
            Ligne de métro affilé au noeud
            (initialisation: None)
        connectedTo: Mapping[int: Node]
            Liste des noeuds x connectés au noeud (self),
            Noeuds x successeurs du noeud (self), 
            Clé: ID d'un noeud x 
            Valeur: Adresse d'un noeud x
            (initialisation: {})
    """

    def __init__(self, id: int, name: str):
        """
        Constructeur des attributs de la class Node
        """
        self.id: int = id
        self.name: str = name
        self.color: str = "white"
        self.predecessor: Optional[Any] = None
        self.line: str = None
        self.connectedTo: Mapping[int, Any] = {}

    def get_id(self) -> int:
        """
        Getter ID (obtenir l'identifiant du noeud)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                id (int): ID du noeud 
        """
        return self.id

    def set_id(self, id: int) -> NoReturn:
        """
        Setter ID (changer l'identifiant du noeud)
        ---------
            Paramètre:
            ---------
                id (int): nouvel ID du noeud

            Retourne: Aucun retour
        """
        self.id = id

    def get_name(self) -> str:
        """
        Getter name (obtenir nom du noeud)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                name (str): nom du noeud 
        """
        return self.name

    def set_name(self, name: str) -> NoReturn:
        """
        Setter name (changer nom du noeud)
        ---------
            Paramètre:
            ---------
                name (str): nouveau nom du noeud

            Retourne: 
                None
        """
        self.name = name

    def get_color(self) -> str:
        """
        Getter color (obtenir couleur du noeud)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                color (str): couleur du noeud 
        """
        return self.color

    def set_color(self, color: str) -> NoReturn:
        """
        Setter color (changer couleur du noeud)
        ---------
            Paramètre:
            ---------
                color (str): nouveau couleur du noeud

            Retourne: Aucun retour
        """
        self.color = color

    def get_predecessor(self) -> Optional[Any]:
        """
        Getter predecessor (obtenir prédécesseur du noeud)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                predecessor (Node): prédécesseur du noeud 
                None: Si aucun prédécesseur
        """
        return self.predecessor

    def set_predecessor(self, predecessor: Any) -> NoReturn:
        """
        Setter predecessor (changer prédécesseur du noeud)
        ---------
            Paramètre:
            ---------
                predecessor (Node): nouveau prédécesseur du noeud

            Retourne: Aucun retour
        """
        self.predecessor = predecessor

    def get_line(self) -> Optional[str]:
        """
        Getter line (obtenir ligne de métro du noeud)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                line (str): ligne de métro affilé au noeud
        """
        return self.line

    def set_line(self, line: str) -> NoReturn:
        """
        Setter line (changer ligne de métro du noeud)
        ---------
            Paramètre:
            ---------
                line (str): ligne de métro affilé au noeud

            Retourne: Aucun retour
        """
        self.line = line

    def get_connections(self) -> List[int]:
        """
        Getter connections (obtenir connections du noeud)
        ---------
            Paramètre: Aucun paramètre nécessaire

            Retourne:
            ---------
                connectedTo.keys() (List[int]): Liste ID des noeuds x connectés au noeud 
        """
        return self.connectedTo.keys()

    def add_connection(self, number_of_node: int, connection: Any) -> NoReturn:
        """
        Ajoute un noeud x au dictionnaire connectedTo du noeud (self)
        Rélève une exception si ID du nouveau noeud x et number_of_node ne correspondent pas
        ---------
            Paramètre:
            --------- 
                number_of_node (int): Identifiant du nouveau noeud ajouté
                connection (Node): Adresse du noeud x ajouté

            Retourne: Aucun retour
        """
        if isinstance(connection, Node):
            if connection.id != number_of_node:
                raise Exception("Id doen't match")
            self.connectedTo[number_of_node] = connection

    def remove_connection(self, number_of_node: int):
        """ 
        Supprime le noeud x, ayant ID number_of_node, de connectedTo du noeud (self)
        Rélève une exception si le number_of_node n'est pas dans connectedTo
        ---------
            Parametre:
            ---------
                number_of_node (int): Identifiant du noeud connecté

            Retourne: Aucun retour
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
