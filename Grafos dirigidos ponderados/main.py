from TDA_weigh_directed_graph import Graph, add_edge, add_node, show_edges, get_node, dijkstra
from weigh_edge import Edge
from node import Node

def build_graph(graph):
    g = graph()
    for node in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'):
        add_node(g, Node(node, []))
    add_edge(g, Edge(get_node(g, 's'), get_node(g, 'a'), 4))
    add_edge(g, Edge(get_node(g, 's'), get_node(g, 'b'), 2))
    add_edge(g, Edge(get_node(g, 's'), get_node(g, 'c'), 3))
    add_edge(g, Edge(get_node(g, 's'), get_node(g, 'd'), 1))

    add_edge(g, Edge(get_node(g, 'a'), get_node(g, 'b'), 3))
    add_edge(g, Edge(get_node(g, 'a'), get_node(g, 'g'), 6))

    add_edge(g, Edge(get_node(g, 'b'), get_node(g, 'c'), 1))

    add_edge(g, Edge(get_node(g, 'c'), get_node(g, 'd'), 5))
    add_edge(g, Edge(get_node(g, 'c'), get_node(g, 'f'), 8))
    add_edge(g, Edge(get_node(g, 'c'), get_node(g, 'i'), 10))

    add_edge(g, Edge(get_node(g, 'd'), get_node(g, 'e'), 7))
    add_edge(g, Edge(get_node(g, 'd'), get_node(g, 'f'), 2))

    add_edge(g, Edge(get_node(g, 'e'), get_node(g, 'x'), 3))

    add_edge(g, Edge(get_node(g, 'f'), get_node(g, 'i'), 5))

    return g

g1 = build_graph(Graph)
print(show_edges(g1))

path, cost = dijkstra(g1, get_node(g1, 's'), get_node(g1, 'x'))

for node in path:
    print(node.name)

print(cost)

