class Graph:
    def __init__(self):
        self.nodes = {}

def add_node(graph, node):
    if node in graph.nodes:
        raise ValueError("Node already exists")
    else:
        graph.nodes[node] = []

def add_edge(graph, edge):
    node1 = edge.get_node1()
    node2 = edge.get_node2()
    if node1 not in graph.nodes:
        raise ValueError("Node not in graph")
    if node2 not in graph.nodes:
        raise ValueError("Node not in graph")
    graph.nodes[node1].append(node2)

def is_node_in(graph, node):
        return node in graph.nodes

def get_node(graph, name):
        for node in graph.nodes:
            if node.name == name:
                return node
        print(f'Node {name} is not in the graph')

def get_neighbours(graph, node):
        return graph.nodes[node]

def get_all_nodes(graph):
        return graph.nodes.keys()

def show_edges(graph):
        all_edges = ""
        for node1 in graph.nodes:
            for node2 in graph.nodes[node1]:
                all_edges += node1.name + " ---> " + node2.name + "\n"
        return all_edges

def delete_node(graph, node):
    if node not in graph.nodes:
        print(f'Node {node.name} is not in the graph')
        return
    
    for n in graph.nodes:
        if node in graph.nodes[n]:
            graph.nodes[n].remove(node)
 
    del graph.nodes[node]

def BFS_path(graph, start, end):
    visited = set()
    queue = [[start]]

    while queue:
        current_path = queue.pop(0)
        current_node = current_path[-1]
        if current_node == end:
            return current_path
        
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in get_neighbours(graph ,current_node):
            new_path = current_path + [neighbor]
            queue.append(new_path)
    
    return None

def DFS_path(graph, start, end, paths=[]):
    # create a new list of paths if it's the first call of the function
    if not paths:
        paths = [[start]]
    
    # get the last path in the list
    current_path = paths[-1]

    # base case
    if current_path[-1] == end:
        return current_path
    
    # explore the neighbors of the last node in the path
    for node in get_neighbours(graph, current_path[-1]):
        if node not in current_path:
            new_path = current_path + [node]
            paths.append(new_path)
            result = DFS_path(graph, start, end, paths)
            if result is not None:
                return result
            paths.pop()
            

""" def DFS_all_paths(graph, start, end, path=[], all_paths=[]):
    path = path + [start]

    if start == end:
        all_paths.append(path)

    for node in get_neighbours(graph, start):
        if node not in path:
            new_path = DFS_all_paths(graph, node, end, path, all_paths)
            if new_path is not None:
                all_paths.append(new_path)

    return all_paths """



