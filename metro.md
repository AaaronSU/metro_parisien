## Graph

+ number_of_node: int
+ node_list: Mapping[int, Node]
---
+ get_number_of_node(): int
+ set_number_of_node(number_of_node)

+ get_nodes: List[int]
+ get_node: Optional[Node]
+ add_node(number_of_node: int, node: Node)
+ remove_node(number_of_node: int): Node

+ add_edge(node1: int, node2: int, weight: int): Edge

+ __contains__(number_of_node: int)
+ __iter__()


## Vertex

+ id: int
+ name: str
+ color: str
+ predecessor: Optional[str]
+ distance: int
+ connectedTo: Mapping[int, Edge]
---
+ get_id(): int
+ set_id(id: int)

+ get_name(): str
+ set_name(name: str)

+ get_color(): str
+ set_color(color: str)

+ get_predecessor(): Optional[str]
+ set_predecessor(predecessor: str)

+ get_distance(): int
+ set_distance(distance: int)

+ get_connections(): List[int]
+ add_connection(number_of_node: int, connection: Edge)
+ remove_connection(number_of_node: int): Optional[Edge]

+ __str__()
+ __iter__()
+ __contains__(number_of_node: int)


## Edge
+ cls.edge_list: List = []

+ direction: Optional[str]
+ starting_node: Node
+ arrival_node: Node
+ weight: int
+ direction: Optional[str]
---
+ get_starting_node(): Node
+ set_starting_node(node: Node)

+ get_arrival_node(): Node
+ set_arrival_node(node: Node)

+ get_weight(): int
+ set_weight(weight: int)

+ get_direction(): str
+ set_direction(direction: Optional[str])

+ get_number_of_edge(cls): int
+ get_edge_list(cls): List[Edge]

+ __iter__()
+ __str__()



## Line
+ numero: str
+ color: str
+ node_list: Mapping[int: Node]
+ number_of_node: int
+ terminus: Mapping[int: Node]
---
+ get_numero(): int:
+ set_numero(numero: str)

+ get_color(): str:
+ set_color(color: str)

+ get_nodes(): List[int]
+ get_node(number_of_node: int): Optional[Node]
+ add_node(number_of_node: int, node: Node)
+ remove_node(number_of_node: int): Node

+ get_number_of_node(): int:
+ set_number_of_node(number_of_node: int)

+ get_terminus_nodes(): List[Node]
+ get_terminus_number(): List[int]
+ get_terminus(): Iterator

+ add_terminus(number_of_node: int, node: Node)
+ remove_terminus(number_of_node: int)

+ __iter__()
+ __contains__(number_of_node)
