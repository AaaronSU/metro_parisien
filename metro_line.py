from typing import Any, List, Iterator, Mapping, NoReturn, Optional
from node import Node


class Line(object):
    line_list: Mapping[str, Any] = {}

    def __init__(self, numero: str, color: str):
        self.numero: str = numero
        self.color: str = color
        self.node_list: Mapping[int: Node] = {}
        self.number_of_node: int = 0
        self.terminus: Mapping[int: Node] = {}
        Line.line_list[numero] = self

    def get_numero(self) -> int:
        return self.numero

    def set_numero(self, numero: str) -> NoReturn:
        self.numero = numero

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str) -> NoReturn:
        self.color = color

    def get_nodes(self) -> List[int]:
        return self.node_list.keys()

    def get_node(self, number_of_node: int) -> Optional[Node]:
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
