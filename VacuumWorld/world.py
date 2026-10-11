from node import Node
from graph import Graph


class World:

    graph = None
    def __init__(self, num):
        #num is how many cells
        g = Graph()
        #in here, create your nodes
        #connect them to each other
        #and add them to the graph
        #object.  This will run in 
        #the "main" of "interface.py"
        self.setGraph(g)
        

    def getGraph(self):
        return self.graph

    def setGraph(self, gr):
        if type(gr) == Graph:
            print('successfully initialized')
            self.graph = gr