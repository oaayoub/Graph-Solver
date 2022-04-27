import collections


def DFS(graph, S, G, visited=[], path=[],extras=[]):
    print(S)
    extras.append(S)
    if S not in graph:
        print("ERROR NOT IN GRAPH")
    path.append(S)
    if S == G:
        # print("FOUNDS")
        # print(path,"Path")
        return path,extras

    if S not in visited:
        visited.append(S)
        # print(S)
        if S in graph:
            for i in graph[S]:
                # print(i,"Children")
                if DFS(graph, i, G, visited, path):
                    # print(path, "Path")
                    return path,extras
    if path:
        path.pop()
    return False


def BFS(graph, S, G, Queue=[], visited=[], path=[]):
    extras=[]
    queue = [(S, [S])]
    visited = set()

    while queue:
        s, path = queue.pop(0)
        extras.append(s)
        visited.add(s)
        if s in graph:
            for node in graph[s]:
                if node == G:
                    return path + [G] , extras
                else:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, path + [node]))


def Limited_DFS(graph, S, G, li, lv, visited=[], path=[],extras=[]):
    print("limited dfs started", li, " ", lv)
    path.append(S)
    print(S)
    extras.append(S)
    if lv <= li:
        print("INSIDE")
        if S not in graph:
            print("ERROR NOT IN GRAPH")
        if S == G:
            # print("FOUNDS")
            # print(path,"Path")
            return path,extras

        if S not in visited:
            visited.append(S)
            # print(S)
            if S in graph:
                for i in graph[S]:
                    # print(i,"Children")
                    if Limited_DFS(graph, i, G, li, lv + 1, visited, path):
                        # print(path, "Path")
                        print("limited dfs working")
                        return path,extras
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


def Uniform_Cost_search(graph, graph_nodes, S):
    extras=[]
    print("INSIDE ALGO")
    mygraph = graph
    print(graph, "GRAPH")
    print("IA GRAPH MADE")
    unvisited = graph_nodes
    print("IA GRAPH unvisited", unvisited)
    # cost of visiting node
    shortest_path = {}
    # shortest path to node #road
    previous_nodes = {}
    curr_min_node = None
    print("IA GRAPH 1")
    # initiating shortest path values
    for i in unvisited:
        extras.append(i)
        shortest_path[i] = 1e6
    shortest_path[S] = 0
    print(1)
    print(2)
    # visiting all nodes
    while unvisited:
        print(3)
        current_min_node = None
        for node in unvisited:  # Iterate over the nodes to get min node
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        print(4)
        print("current node", current_min_node)
        # if graph is directed and node to have outhoing edges
        if not (current_min_node in mygraph):
            print(current_min_node, "NOT")
            unvisited.remove(current_min_node)
            continue
        # if node have only one outgoing edge it puts it in list
        if not isinstance(mygraph[current_min_node], list):
            neighbors = [mygraph[current_min_node]]
        else:
            neighbors = mygraph[current_min_node]
        print(neighbors, "NEIGHBORS")
        print(5)
        # update the values of children
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
    print(previous_nodes)
    print(extras,"EXTRAS")
    return (previous_nodes, shortest_path,extras)


# sorting algorithm for list of tuples according to value
def Sort(sub_li):
    return (sorted(sub_li, key=lambda x: x[1]))


def Sort_2(sub_li):
    return (sorted(sub_li, key=lambda x: x[2]))


def dijkstra_result(parent_map, shortest_path, start, goal):
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent_map[node]
    path.append(start)
    path.reverse()
    return path


def A_star_search(graph, graph_nodes, S, G, heuristic):
    extras=[]
    print("INSIDE A Star search")
    mygraph = graph
    print(graph, "GRAPH")
    print("IA GRAPH MADE")
    unvisited = graph_nodes
    print("IA GRAPH unvisited", unvisited)
    # cost of visiting node
    shortest_path = {}
    # shortest path to node #road
    previous_nodes = {}
    print("IA GRAPH 1")
    # initiating shortest path values
    for i in graph_nodes:
        shortest_path[i] = 1e6
    shortest_path[S] = 0
    print(1)
    print(2)
    openList = set([S])
    closedList = set()


    # visiting all nodes
    while openList:
        print(3)
        current_min_node = None
        for node in openList:  # Iterate over the nodes to get min node
            extras.append(node)
            print(node, "node")
            print(current_min_node, "curr min node")
            if (current_min_node == None) or (int(shortest_path[node]) + int(heuristic[node])) < (
                    int(shortest_path[current_min_node]) + int(heuristic[current_min_node])):
                current_min_node = node
                print(current_min_node, "curr min node changed")

        if current_min_node == None:
            print("NO PATH")
            return
        print(4)
        print("current node", current_min_node)
        # if graph is directed and node to have outhoing edges
        if current_min_node == G:
            print("FOUND")
            path = []
            node = G
            while node != S:
                path.append(node)
                node = previous_nodes[node]
            path.append(S)
            path.reverse()
            print("A* worked fine ")
            return path,shortest_path[G],extras

        if not (current_min_node in mygraph):
            print(current_min_node, "NOT")
            unvisited.remove(current_min_node)
            continue
        # if node have only one outgoing edge it puts it in list
        if not isinstance(mygraph[current_min_node], list):
            neighbors = [mygraph[current_min_node]]
        else:
            neighbors = mygraph[current_min_node]
        print(neighbors, "NEIGHBORS")
        print(5)
        # update the values of children
        for neighbor in neighbors:
            print("neighbour", neighbor)
            key = str(neighbor[0])
            val = neighbor[1]
            extras.append(key)
            print(key, val, " KEY/VAL")
            if key not in openList and key not in closedList:
                print("here 1")
                openList.add(key)
                previous_nodes[key] = current_min_node
                print("here 2")
                shortest_path[key] = shortest_path[current_min_node] + val
            elif (shortest_path[key]> shortest_path[current_min_node] + val):
                print("here else 3")
                shortest_path[key] = shortest_path[current_min_node]+val
                print("here else 4")
                previous_nodes[key]=current_min_node


        print("here 3")
        openList.remove(current_min_node)
        closedList.add(current_min_node)
        print("here 4")
    print('Path does not exist!')
    return False

    # return (previous_nodes,shortest_path)


def greedy_Search(S, G, heuristics, DS):
    extras=[] #visited NODES
    print("inside Greedy FUNC")
    outgoingedes = {}
    print(DS, "DS")
    for i in DS:
        print(i, "i in DS")
        for j in DS[i]:
            print(j, "of DS of i")
            outgoingedes.setdefault(i, []).append((j[0]))

    visited = [S]
    print(outgoingedes, "outgoing edges")
    print(S, "S")
    print(heuristics, "heu")
    print(heuristics[S], "heu[S]")
    print("G1")
    Q = [(S, heuristics[S], [S])]
    while Q:
        Sort(Q)
        print("Sorted", Q)
        s, val, path = Q.pop(0)
        visited.append(s)
        extras.append(s)
        print(visited, "VISITED")
        for i in outgoingedes[s]:
            print(i, "i in greedy")
            if i in visited:
                continue
            Q.append((i, heuristics[i], path + [i]))
            if i == G:
                print(i, path + [i], "FOUND")
                return path + [i] , extras
        print(Q, "Q after children")
