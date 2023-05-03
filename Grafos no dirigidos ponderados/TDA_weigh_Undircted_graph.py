class Graph:
    def __init__(self):
        self.nodes = {}

def add_node(graph, node):
    if node in graph.nodes:
        raise ValueError("Node already exists")
    else:
        graph.nodes[node] = []


def add_edge_undirected(graph, edge):
    node1 = edge.get_node1()
    node2 = edge.get_node2()
    if node1 not in graph.nodes:
        raise ValueError("Node not in graph")
    if node2 not in graph.nodes:
        raise ValueError("Node not in graph")
    graph.nodes[node1].append((node2, edge.weight))
    graph.nodes[node2].append((node1, edge.weight))


def is_node_in(graph, node):
        return node in graph.nodes


def get_node(graph, name):
        for node in graph.nodes:
            if node.name == name:
                return node
        print(f'Node {name} is not in the graph')


def get_neighbours(graph, node):
    neighbours = []
    for neighbour in graph.nodes[node]:
        neighbours.append((neighbour[0], neighbour[1]))
    return neighbours


def get_all_nodes(graph):
        return graph.nodes.keys()


def show_edges(graph):
        all_edges = ""
        for node1 in graph.nodes:
            for edge in graph.nodes[node1]:
                node2 = edge[0]
                weight = edge[1]
                all_edges += node1.name + " --- " + str(weight) + " --> " + node2.name + "\n"
        return all_edges


def delete_node(graph, node):
    if node not in graph.nodes:
        print(f'Node {node.name} is not in the graph')
        return
    
    for n in graph.nodes:
        if node in graph.nodes[n]:
            graph.nodes[n].remove(node)
 
    del graph.nodes[node]

def dijkstra(graph, start, end):
    distances = {node: float('inf ') for node in graph.nodes}
    distances[start] = 0
    visited = set()
    prev = {node: None for node in graph.nodes}

    queue = [(start, 0)]
    while queue:
        current, current_distance = min(queue, key=lambda x: x[1])
        queue.remove((current, current_distance))

        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = prev[current]
            path.reverse()
            return path, distances[end]

        visited.add(current)

        for neighbor, weight in graph.nodes[current]:
            if neighbor in visited:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                prev[neighbor] = current
                queue.append((neighbor, new_distance))
