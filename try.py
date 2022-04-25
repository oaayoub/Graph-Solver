from pyvis.network import Network
import networkx as nx
import Graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B']),
         'S': set(['G']),
         'F': set(['C','S'])}
#print(Algo.DFS_search(graph,'A','G',visited=[],path=[]))


G=Graph.GraphDS("def")

s={'':''}
s=['3']*12
G.makeDS(G.graph)
print(G.number_verticies)
