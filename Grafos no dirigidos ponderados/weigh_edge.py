class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def get_node1(self):
        return self.node1
    
    def get_node2(self):
        return self.node2

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.node1.name + " ---" + str(self.weight) + "--> " + self.node2.name
