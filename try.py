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
# [['2', '3', '11'], ['1', '2', '12'], ['3', '4', '13'], ['4', '1', '15']]
G={'2': [('3', 23), ('1', 12)], '3': [('2', 23), ('4', 34)], '1': [('2', 12), ('4', 14)], '4': [('3', 34), ('1', 14)]}

unV = ['1','2','3','4']
# cost of visiting node
shortest_path = {}
# shortest path to node #road
previous_nodes = {}
for i in unV:
    shortest_path[i] = 1e6
shortest_path['1'] = 0
while unV:
    current_min_node = None
    for node in unV:  # Iterate over the nodes
        if current_min_node == None:
            current_min_node = node
            print("Current node",node)
        elif shortest_path[node] < shortest_path[current_min_node]:
            current_min_node = node
            print("Current node",node)

    print(G[current_min_node],"G[current_min_node]")

    # The code block below retrieves the current node's neighbors and updates their distances
    neighbors = G[current_min_node]
    #neighbor[1] -> value
    for neighbor in neighbors:
        key = neighbor[0]
        val = neighbor[1]
        print(key,val," KEY/VAL")
        tentative_value = shortest_path[current_min_node] + val
        if tentative_value < shortest_path[key]:
            shortest_path[key] = tentative_value
            # We also update the best path to the current node
            previous_nodes[key] = current_min_node
    unV.remove(current_min_node)
print(previous_nodes,shortest_path)
path = ['1','2','3']
graphDS ={'1':[('2',4),('3',5)]}
t1 = path[0] #from
t2 = path[1] # to
l1 = graphDS[t1]
print(l1)
for i in l1:
    if i[0] == t2:
        label = i[1]
        break
print(label)
print(int(5))