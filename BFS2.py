from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v): 
        self.graph[u].append (v)    
    def Breadth_First_Search(self,s ):
        queue=[]
        visited=[False]*len(self.graph)
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s)
            for node in self.graph[s]:
                if visited[node]==False:
                    queue.append(node)
                    visited[node]=True
            
""" 
S=0
A=1
B=2
C=3
D=4
G=5 """
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(3, 3)
g.addEdge(1, 4)
g.addEdge(4, 5)
g.Breadth_First_Search(0)
print(g.graph) 




