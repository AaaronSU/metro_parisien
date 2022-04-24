from typing import Mapping, NoReturn, List, Optional
from edge import Edge
from node import Node


class Graph:
    def __init__(self):
        self.number_of_node: int = 0
        self.node_list: Mapping[int, Node] = {}

    def get_number_of_node(self) -> int:
        return self.number_of_node

    def set_number_of_node(self, number: int) -> NoReturn:
        self.number_of_node = number

    def get_nodes(self) -> List[int]:
        return self.node_list.keys()

    def get_node(self, number_of_node) -> Optional[Node]:
        if number_of_node in self:
            return self.node_list[number_of_node]
        else:
            return None

    def add_node(self, number_of_node: int, node: Node) -> NoReturn:
        if not isinstance(node, Node):
            raise Exception("Invalid node")
        else:
            self.node_list[number_of_node] = node
            self.number_of_node += 1

    def remove_node(self, number_of_node: int) -> Node:
        if number_of_node in self:
            return self.node_list.pop(number_of_node)
        raise Exception("Node not exist in Graph")

    def add_edge(self, node1: int, node2: int, weight: int) -> Edge:
        if not (isinstance(node1, Node) and isinstance(node2, Node)):
            raise Exception("Invalid node")
        return Edge(node1, node2, weight)

    def __contains__(self, number_of_node: int):
        return number_of_node in self.node_list.keys()

    def __iter__(self):
        return iter(self.node_list.values())
