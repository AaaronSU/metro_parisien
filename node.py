from typing import Mapping, NoReturn, Optional, List, Any
import sys


class Node(object):
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

    def add_connection(self, number_of_node: int, connection) -> NoReturn:
        self.connectedTo[number_of_node] = connection

    def remove_connection(self, number_of_node: int):
        if number_of_node in self:
            self.node_list.pop(number_of_node)
        raise Exception("Node not exist in Graph")

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def __iter__(self):
        return self.connectedTo.values()

    def __contains__(self, number_of_node: int):
        return number_of_node in self.connectedTo.keys()
