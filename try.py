from pyvis.network import Network
import networkx as nx
import Graph, Algo

'''
#print(Algo.DFS_search(graph,'A','G',visited=[],path=[]))


G=Graph.GraphDS("def")

s={'':''}
s=['3']*12
G.makeDS(G.graph)
print(G.number_verticies)
dist = { ('3', 1), ('2', 2), ('4', 5), ('6', 12)}
dist = Algo.Sort(dist)
print(dist)
'''
g = Network(directed=True)
g.add_node(0)
g.add_node(1)
g.add_edge(0, 1)

g.add_edge(0, 1)
g.options.edges =False
g.set_edge_smooth('dynamic')
g.show("Graph.html")
