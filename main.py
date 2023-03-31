class Graph:
    vertsAndEdges = ([],[])
    edgesWeight = {} #tutaj dict se dla krawedz odpowiada wadze

    def __init__(self, verts=[], edges=[], weights=[]):
        for vertex in verts:
            self.vertsAndEdges[0].append(vertex)
        for edge in edges:
            for point in edge:
                if not findInList(verts, point):
                    raise Exception("Vertex given making edge, doesn't exsists in vertex list")
        for edge in edges:
            self.vertsAndEdges[1].append(edge)
        j = 0
        for edge in edges:
            self.edgesWeight[edge] = weights[j]
            j+= 1

    def addVertex(self,name):
        self.vertsAndEdges[0].append(name)
    def addEdge(self,name, value):
        for vertex in self.vertsAndEdges[0]:
            if vertex == name[0] or vertex == name[1]:
                raise Exception("Creating edge with non-exsistent verticies")
        self.vertsAndEdges[1].append(name)
        self.edgesWeight[name] = value
        
    def deleteVertex(self,name):
        for edge in self.vertsAndEdges[1]:
            for point in edge:
                if name == point:
                    self.vertsAndEdges[1].remove(edge)
        for element in self.edgesWeight:
            for value in element:
                if value == name:
                    del self.edgesWeight[element]
        self.vertsAndEdges[0].remove(name)
        
    def deleteEdge(self,name):
        pass

    def showEdges(self):
        print(self.vertsAndEdges[1])
    def showVerticies(self):
        print(self.vertsAndEdges[0])

def findInList(list, elementToFind):
    for element in list:
        if element == elementToFind:
            return True
    return False

def kruszec(G):
    A = set()



if __name__ == "__main__":
    A = (['a','b','c','d','e','f'],[('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','g'),('g','a'),('b','f')])
    v = {}
    listVertex = ['a','b','c','d','e','f']
    listOfEdges = [(2, ['a','b']),(),('c','d'),('d','e'),('e','f'),('f','g'),('g','a'),('b','f')]
    B = Graph(['a','b','c'], [('a','b'), ('a', 'c')], [2, 4])
    B.showEdges()
    B.showVerticies()
    B.addVertex('d')
    B.showVerticies()
    B.showEdges()
    #pomysl na fix knorr
    #([a,b,c],[(a,b),(a,c)]) pierwszy sublist wszystkie vertexy
    #{(a,b):2, (a,c):54)}
    # pierwsza podlista tupla, vertexy
    # druga podlista krawedzie
