from typing import Any, List, NoReturn, Optional, Tuple
from node import Node


class Edge(object):
    edge_list: List = []

    def __init__(self, starting_node: Node, arrival_node: Node, weight: int, direction: Optional[str] = None):
        if (not isinstance(starting_node, Node)) or (not isinstance(arrival_node, Node)):
            raise Exception("Invalid node for initialization")
        self.starting_node: Node = starting_node
        self.arrival_node: Node = arrival_node
        self.weight: int = weight
        self.direction: Optional[List[str]] = direction
        Edge.edge_list.append(self)

    def get_starting_node(self) -> Node:
        return self.starting_node

    def set_starting_node(self, node: Node) -> NoReturn:
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        self.starting_node = node

    def get_arrival_node(self) -> Node:
        return self.arrival_node

    def set_arrival_node(self, node: Node) -> NoReturn:
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        self.arrival_node = node

    def get_weight(self) -> int:
        return self.weight

    def set_weight(self, weight: int) -> NoReturn:
        self.weight = weight

    def get_direction(self) -> str:
        return self.direction

    def add_direction(self, direction: str) -> NoReturn:
        if not self.direction:
            self.direction = [direction]
        else:
            self.direction.append(direction)

    def remove_direction(self, direction: str):
        if direction not in self.direction:
            raise Exception("Direction doesn't exist in edge")
        self.direction.remove(direction)

    @classmethod
    def get_connections_of_node(cls, node: Node) -> List[Tuple[Node, int, Optional[str]]]:
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
        return f"The class Edge contains about {Edge.get_number_of_edge()} on total, which are {Edge.get_edge_list()}"
