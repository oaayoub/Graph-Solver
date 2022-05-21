import collections

VIS_NODES_ALGO = []

['1','2','3','4']
def DFS(graph, S, G, visited=[], path=[]):
    print("DFS ALGO")
    print(S)
    VIS_NODES_ALGO.append(S)
    print("HERE")

    path.append(S)
    print("HERE")

    for goal in G:
        print("each goal in G", goal)
        if S == goal:
            print("FOUNDS")
            print(path, "Path")
            return path

    '''
    if S in G or (S == G):
        print("FOUNDS")
        print(path,"Path")
        return path
    '''
    print("HERE")
    if S not in visited:
        visited.append(S)
        # print(S)
        if S in graph:
            for i in graph[S]: #search in all children
                print(i, "Children")
                if DFS(graph, i, G, visited, path):
                    print(path, "Path DFS ALGO")
                    return path
    if path:
        path.pop()
    return []


def BFS(graph, S, G, Queue=[], visited=[], path=[]):
    extras = []
    queue = [(S, [S])] #S , [S]
    visited = set()

    while queue:
        s, path = queue.pop(0)
        '''if s in G:
            return path, extras'''

        for goal in G:
            if s == goal:
                return path, extras

        extras.append(s)
        visited.add(s)
        if s in graph:
            for node in graph[s]:
                #search cildren
                '''
                if node == G:
                    return path + [G] , extras
                '''
                if node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))

    return [], extras

def Limited_DFS(graph, S, G, li, lv, visited=[], path=[], extras=[]):
    print("limited dfs started", li, " ", lv)
    path.append(S)
    print(S)
    VIS_NODES_ALGO.append(S)
    extras.append(S)
    if lv <= li:
        print("INSIDE")
        if S in graph:
            print("ERROR NOT IN GRAPH")
        print("HERE 1")
        if S in G:
            print("FOUNDS")
            print(path, "Path")
            return True, path, VIS_NODES_ALGO
        print("HERE 1")
        if S not in visited:
            print("HERE 2")
            visited.append(S)
            # print(S)
            if S in graph:
                print("HERE 3")
                for i in graph[S]:
                    print("HERE 4")
                    # print(i,"Children")
                    if Limited_DFS(graph, i, G, li, lv + 1, visited, path)[0] and (lv+1) <= li:
                        print(path, "Path")
                        print("limited dfs working")
                        return True, path, VIS_NODES_ALGO
    if path:
        path.pop()
    print("FALSE , EXTRAS")
    print("EXTRAS", extras)
    print("Vis_NODES", VIS_NODES_ALGO)
    return False, [], VIS_NODES_ALGO


def Itr_Lim_DFS(graph, S, G, max_depth, step):
    counter = step
    # (graph, S, G, li, lv, visited=[], path=[], extras=[])
    print("HERE")
    print("GOALS", G)
    while counter <= max_depth:
        print(counter)
        if Limited_DFS(graph, S, G, counter, 0, visited=[], path=[], extras=[])[0]:
            print("FOUND ITERATIVE DEEPINING ")
            return Limited_DFS(graph, S, G, counter, 0, visited=[], path=[], extras=[])
        counter = counter + step

    return Limited_DFS(graph, S, G, counter - step, 0, visited=[], path=[], extras=[])


def Uniform_Cost_search(graph, graph_nodes, S):
    VIS_NODES_ALGO = []
    print("INSIDE ALGO UC")
    mygraph = graph #adjacency listt
    print(graph, "GRAPH")
    print("IA GRAPH MADE")
    unvisited = graph_nodes  #list of all node [n1,n2,n3,......]
    print("IA GRAPH unvisited", unvisited)
    # cost of visiting node
    shortest_path = {} #S: 10
    # shortest path to node #road
    previous_nodes = {}
    curr_min_node = None
    print("IA GRAPH 1")
    # initiating shortest path values
    for i in unvisited:
        VIS_NODES_ALGO.append(i)
        shortest_path[i] = 1e9
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
        #[n1:2000, n2:3000, N3:10] ->curr min node =N3
        print(4)
        print("current node", current_min_node)
        # if graph is directed and node to have outhoing edges
        #######double check
        if not (current_min_node in mygraph):
            print(current_min_node, "NOT")
            unvisited.remove(current_min_node)
            continue
        ##########
        # if node have only one outgoing edge it puts it in list
        if not isinstance(mygraph[current_min_node], list):
            neighbors = [mygraph[current_min_node]]
        else:
            neighbors = mygraph[current_min_node] #[N2:30,N3:40] ->N2:30 ->key N2 -> val
        ####################
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
                previous_nodes[key] = current_min_node  #{N2:N1}


        unvisited.remove(current_min_node)
        print(9)
    print(10)
    print(shortest_path)
    print(previous_nodes)
    print(VIS_NODES_ALGO, "EXTRAS")
    return (previous_nodes, shortest_path, VIS_NODES_ALGO) #ShortPath{N1:10,N2:20} Pn{N1:N0,N2:N0}


# sorting algorithm for list of tuples according to value
def Sort(L):
    return sorted(L, key=lambda x: x[1])


def Sort_2(L):
    return sorted(L, key=lambda x: x[2])


def dijkstra_result(parent_map, shortest_path, start, goal):
    #goal N4,Start N0
    #N4 -> N3
    #N3 -> N2
    #N2 -> N7
    #N7 -> N0
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent_map[node]
    path.append(start)
    path.reverse()
    return path


def A_star_search(graph, graph_nodes, S, G, heuristic):
    VIS_NODES_ALGO = []
    print("INSIDE A Star search")
    mygraph = graph #adjacency list
    print(graph, "GRAPH")
    print("IA GRAPH MADE")
    unvisited = graph_nodes #list of nodes
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
            VIS_NODES_ALGO.append(node)
            print(node, "node")
            print(current_min_node, "curr min node")
            if (current_min_node == None) or (int(shortest_path[node]) + int(heuristic[node])) < (
                    int(shortest_path[current_min_node]) + int(heuristic[current_min_node])):
                current_min_node = node
                print(current_min_node, "curr min node changed")
        ####################
        if current_min_node == None:
            print("NO PATH")
            return
        ###################
        print(4)
        print("current node", current_min_node)
        # if graph is directed and node to have outhoing edges
        if current_min_node in G:
            print("FOUND")
            path = []
            node = current_min_node
            while node != S:
                path.append(node)
                node = previous_nodes[node]
            print("A* worked fine ")

            path.append(S)
            print("A* worked fine ")

            path.reverse()
            print("A* worked fine ")
            return path, shortest_path[current_min_node], VIS_NODES_ALGO

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
            VIS_NODES_ALGO.append(key)
            print(key, val, " KEY/VAL")
            if key not in openList and key not in closedList:
                print("here 1")
                openList.add(key)
                previous_nodes[key] = current_min_node
                print("here 2")
                shortest_path[key] = shortest_path[current_min_node] + val
            elif (shortest_path[key] > shortest_path[current_min_node] + val):
                print("here else 3")
                shortest_path[key] = shortest_path[current_min_node] + val
                print("here else 4")
                previous_nodes[key] = current_min_node

        print("here 3")
        openList.remove(current_min_node)
        closedList.add(current_min_node)
        print("here 4")
    print('Path does not exist!')
    return [], 999999999, VIS_NODES_ALGO

    # return (previous_nodes,shortest_path)


def greedy_Search(S, G, heuristics, DS):
    try:
        VIS_NODES_ALGO = []  # visited NODES
        print("inside Greedy FUNC")
        outgoingedes = {}
        print(DS, "Data Structure")
        for i in DS:
            print(i, "i in DS")
            for j in DS[i]:
                print(j, "of DS of i")
                outgoingedes.setdefault(i, []).append((j[0]))
                #DS[i] ->{n1:[n3,n2]}


        visited = [S]
        print(outgoingedes, "outgoing edges")
        print(S, "S")
        print(heuristics, "heu")
        print(heuristics[S], "heu[S]")
        print("G1")
        Q = [(S, heuristics[S], [S])]
        while Q:
            ##SORT HERE
            Q = Sort(Q)
            print("Sorted", Q)
            s, val, path = Q.pop(0)
            visited.append(s)
            VIS_NODES_ALGO.append(s)
            print(visited, "VISITED")
            for i in outgoingedes[s]:
                print(i, "i in greedy")
                if i in visited:
                    continue
                Q.append((i, heuristics[i], path + [i]))
                if i in G:
                    print(i, path + [i], "FOUND")
                    return path + [i], VIS_NODES_ALGO
            print(Q, "Q after children")
        return [], VIS_NODES_ALGO

    except :
        return

