class Node:
    def __init__(self, name, info):
        self.name = name
        self.info = info
    
    def __str__(self):
        return self.name + ": " + self.info