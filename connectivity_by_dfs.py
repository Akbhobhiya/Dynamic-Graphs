
from collections import defaultdict 
  

#  Check connectivity using DFS

class Graph: 
  
    def __init__(self): 
        self.adList = defaultdict(list)
        self.vertex=[]
        self.visited=[None]*100
        self.length=0

    def addVertex(self,u):
        self.vertex.append(u)
        self.visited[u]=False
        self.length = self.length+1

    def cutVertex(self,u):
        self.vertex.remove(u)
        for i in range(len(self.adList)):
            if u in self.adList[i]:
                self.adList[i].remove(u)
        del self.adList[u]

    def addEdge(self,u,v):
        self.adList[u].append(v)
        self.adList[v].append(u)

    def dfs(self,v):
        # print(self.visited)
        self.visited[v]=True
        # print(v)

        for u in self.adList[v]:
            # print(u)
            if self.visited[u] == False:
                self.dfs(u)


    def isConnected(self):
        # print(self.length)
        self.visited=[False]*self.length
        self.dfs(self.vertex[0])
        # print(self.visited)
        for i in ((self.adList)):
            # print("yes")
            if self.visited[i] == False:
                # print("yeahhhh...")
                return False
        return True
# Driver code 
g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2) 
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addEdge(0, 2) 
g.addEdge(0, 3)
g.addEdge(0, 5)
g.addEdge(1, 3)  
g.addEdge(1, 5)
g.addEdge(2, 4)
print(g.isConnected())
# print(g.adList)
# print(len(g.adList))
g.cutVertex(0)
# print(len(g.adList))
# print(g.adList)
print(g.isConnected())
# g.addVertex(4)
# g.addEdge(2,4)
# g.addEdge(2,0)
# print(g.isConnected())
# g.cutVertex(4)
# print(g.isConnected())
# g.cutVertex(4)
# g.addVertex(4)
# g.addEdge(2, 4)
# g.cutVertex(0)
# print(g.adList)
# print(g.vertex)
# print(g.adList)
  
# print ("Following is DFS traversal")
# g.dfs(2) 