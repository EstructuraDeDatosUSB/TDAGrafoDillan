from TDA_weigh_Undircted_graph import Graph, add_edge_undirected, add_node, show_edges, get_node, dijkstra
from node import Node
from weigh_edge import Edge

def build_graph(graph):
    g = graph()
    for node in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'):
        add_node(g, Node(node, []))
    add_edge_undirected(g, Edge(get_node(g, 's'), get_node(g, 'a'), 1))
    add_edge_undirected(g, Edge(get_node(g, 's'), get_node(g, 'b'), 2))
    add_edge_undirected(g, Edge(get_node(g, 's'), get_node(g, 'c'), 3))
    add_edge_undirected(g, Edge(get_node(g, 's'), get_node(g, 'd'), 4))
    add_edge_undirected(g, Edge(get_node(g, 'a'), get_node(g, 'b'), 5))
    add_edge_undirected(g, Edge(get_node(g, 'a'), get_node(g, 'g'), 6))
    add_edge_undirected(g, Edge(get_node(g, 'b'), get_node(g, 'c'), 7))
    add_edge_undirected(g, Edge(get_node(g, 'c'), get_node(g, 'd'), 8))
    add_edge_undirected(g, Edge(get_node(g, 'c'), get_node(g, 'f'), 9))
    add_edge_undirected(g, Edge(get_node(g, 'c'), get_node(g, 'i'), 10))
    add_edge_undirected(g, Edge(get_node(g, 'd'), get_node(g, 'e'), 11))
    add_edge_undirected(g, Edge(get_node(g, 'd'), get_node(g, 'f'), 12))
    add_edge_undirected(g, Edge(get_node(g, 'e'), get_node(g, 'x'), 13))
    add_edge_undirected(g, Edge(get_node(g, 'f'), get_node(g, 'i'), 14))
    return g

g2 = build_graph(Graph)
print(show_edges(g2))

path, peso = dijkstra(g2, get_node(g2, 's'), get_node(g2, 'x'))

for node in path:
    print(node.name)
print(peso)

