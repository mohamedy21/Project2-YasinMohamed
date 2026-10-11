from node import Node
class Graph:
    '''
    nodes: the list of nodes, these should be node objects
    '''
    nodes = []
    
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes
    
    def addEdge(self, sourceId, destId):
        pass

    def bfs(self, startId):
        ##BREADTHFIRSTSEARCH
        path = []
        return path
        
    def dfs(self, startId):
        ##DEPTHFIRST SEARCH
        path = []
        return path

    def __str__(self):
        pass