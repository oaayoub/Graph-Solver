import queue
import Graph


def DFS(graph, S, G, visited=[], path=[]):
    print(S)
    if S not in graph:
        print("ERROR NOT IN GRAPH")
    path.append(S)
    if S == G:
        # print("FOUNDS")
        # print(path,"Path")
        return path

    if S not in visited:
        visited.append(S)
        # print(S)
        if S in graph:
            for i in graph[S]:
                # print(i,"Children")
                if DFS(graph, i, G, visited, path):
                    # print(path, "Path")
                    return path
    if path:
        path.pop()
    return False


def BFS(graph, S, G, Queue=[], visited=[], path=[]):
    queue = [(S, [S])]
    visited = set()

    while queue:
        s, path = queue.pop(0)
        visited.add(s)
        if s in graph:
            for node in graph[s]:
                if node == G:
                    return path + [G]
                else:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, path + [node]))


def Limited_DFS(graph, S, G, li, lv, visited=[], path=[]):
    print("limited dfs started", li, " ", lv)
    path.append(S)
    print(S)
    if lv <= li:
        print("INSIDE")
        if S not in graph:
            print("ERROR NOT IN GRAPH")
        if S == G:
            # print("FOUNDS")
            # print(path,"Path")
            return path

        if S not in visited:
            visited.append(S)
            # print(S)
            if S in graph:
                for i in graph[S]:
                    # print(i,"Children")
                    if Limited_DFS(graph, i, G, li, lv + 1, visited, path):
                        # print(path, "Path")
                        print("limited dfs working")
                        return path
    if path:
        path.pop()
    return False


def Itr_Lim_DFS(graph, S, G, max_depth, step):
    counter = step
    print("HERE")
    while counter <= max_depth:
        print(counter)
        if Limited_DFS(graph, S, G, counter, 0, visited=[], path=[]):
            return Limited_DFS(graph, S, G, counter, 0, visited=[], path=[])
        counter = counter + step


def Uniform_Cost_search(graph,graph_nodes,S):
    print("INSIDE ALGO")
    mygraph = graph
    print(graph,"GRAPH")
    print("IA GRAPH MADE")
    unvisited = graph_nodes
    print("IA GRAPH unvisited",unvisited)
    #cost of visiting node
    shortest_path={}
    #shortest path to node #road
    previous_nodes={}
    curr_min_node = None
    print("IA GRAPH 1")

    for i in unvisited:
        shortest_path[i]=1e6
    shortest_path[S]=0
    print(1)
    print(2)
    while unvisited:
        print(3)
        current_min_node = None
        for node in unvisited:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        print(4)
        print("current node",current_min_node)
        if not (current_min_node in mygraph):
            print(current_min_node,"NOT")
            unvisited.remove(current_min_node)
            continue

        if not isinstance(mygraph[current_min_node], list):
            neighbors = [mygraph[current_min_node]]
        else:
            neighbors = mygraph[current_min_node]
        print(neighbors,"NEIGHBORS")
        print(5)
        for neighbor in neighbors:
            print("neighbour", neighbor)
            print(6)
            key = str(neighbor[0])
            print(7)
            val = neighbor[1]
            print(8)
            print(key, val, " KEY/VAL")
            tentative_value = shortest_path[current_min_node] + val
            if tentative_value < shortest_path[key]:
                shortest_path[key] = tentative_value
                # We also update the best path to the current node
                previous_nodes[key] = current_min_node
        unvisited.remove(current_min_node)
        print(9)
    print(10)
    print(shortest_path)
    return (previous_nodes,shortest_path)


# sorting algorithm for list of tuples according to value
def Sort(sub_li):
    return (sorted(sub_li, key=lambda x: x[1]))

def dijkstra_result(parent_map,shortest_path,start,goal):
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent_map[node]
    path.append(start)
    path.reverse()
    return path

