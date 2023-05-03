from TDA_directed_graph import Graph, add_edge, add_node, show_edges, get_node, delete_node, BFS_path, DFS_path
from edge import Edge
from node import Node

def build_graph(graph):
    g = graph()
    for node in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'):
        add_node(g, Node(node, []))
    add_edge(g,Edge(get_node(g,'s'), get_node(g,'a')))
    add_edge(g,Edge(get_node(g,'s'), get_node(g,'b')))
    add_edge(g,Edge(get_node(g,'s'), get_node(g,'c')))
    add_edge(g,Edge(get_node(g,'s'), get_node(g,'d')))

    add_edge(g,Edge(get_node(g,'a'), get_node(g,'b')))
    add_edge(g,Edge(get_node(g,'a'), get_node(g,'g'))) 

    add_edge(g,Edge(get_node(g,'b'), get_node(g,'c')))

    add_edge(g,Edge(get_node(g,'c'), get_node(g,'d')))
    add_edge(g,Edge(get_node(g,'c'), get_node(g,'f')))
    add_edge(g,Edge(get_node(g,'c'), get_node(g,'i')))

    add_edge(g,Edge(get_node(g,'d'), get_node(g,'e')))
    add_edge(g,Edge(get_node(g,'d'), get_node(g,'f')))

    add_edge(g,Edge(get_node(g,'e'), get_node(g,'x')))

    add_edge(g,Edge(get_node(g,'f'), get_node(g,'i')))

    return g


g1 = build_graph(Graph)

print(show_edges(g1))

path = BFS_path(g1, get_node(g1,'s'), get_node(g1,'x'))

for node in path:
    print(node.name, end=" ")

path2 = DFS_path(g1, get_node(g1,'s'), get_node(g1,'x'))

print("\n")

for node in path2:
    print(node.name, end=" ")