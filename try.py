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
g.set_edge_smooth('dynamic') ##Caution##
g.toggle_physics(True)
g.add_node(0)
g.add_node(1)
g.add_node(3)
g.add_node(4)
g.add_node(2)
g.add_node(5)
g.add_edge(0, 1)
g.add_edge(1,2)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)

g.add_edge(0, 1,label="123")

g.set_edge_smooth('dynamic')
g.toggle_physics(False)
#g.barnes_hut(spring_length=140, damping=1, spring_strength=0)

GraphDS = {'2': [('3', 1), ('1', 1)], '3': [('2', 1)], '1': [('2', 1)]}
l =[]
l.append((1,54))
t = (54,1)
l.append(t)
print(l)