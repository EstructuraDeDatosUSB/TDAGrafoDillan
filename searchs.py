def DFS_path(graph, start, end, path):
    path.append(start)
    # base case
    if start == end:
        return path

    for node in graph.get_neighbours(start):
        if node not in path:
            new_path = DFS_path(graph, node, end, path)
            if new_path is not None:
                return new_path

def DFS_path2(graph, start, end, path, best):
    path = path + [start]
    # base case
    if start == end:
        return path
    for node in graph.get_neighbours(start):
        if node not in path:
            if best == None or len(path) < len(best):
                new_path = DFS_path2(graph, node,  end, path, best)
                if new_path is not None:
                    best = new_path
    return best    

def BFS_path(graph, start, end):
    path = [start]
    queue = [path]

    while queue:
        current_path = queue.pop(0)
        if current_path[-1] == end:
            return current_path
        
        for node in graph.get_neighbours(current_path[-1]):
            new_path = current_path + [node]
            queue.append(new_path)

def BFS2(graph, start, end):
    path = [start]
    queue = [path]
    #run all the queue
    while queue:
        current_path = queue.pop(0)
        if current_path[-1] == end:
            return current_path
        for next_vertex in graph.get_neighbours(current_path[-1]):
            if next_vertex not in current_path:
                new_path = current_path + [next_vertex]
                queue.append(new_path)