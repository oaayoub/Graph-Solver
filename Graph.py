class GraphDS:
    graph = [] #EDGELIST
    graphDS ={} #adjaceny list
    weighted = True # check if graph is weighted
    adj_list=[] #non-weighted ajaceny list
    unvisited =[] #list of all nodes
    heuristic_dict ={} #heuristic of each node
    goals =[] #goals list
    heuristic_valid=True
    heuristic_valid_long=False

    def __init__(self,Default):
        self.graph=[]
        with open("Default.txt") as text:
            text = text.readlines()
        for i in text:
            i = i.rstrip()
            i = i.lstrip()
            i = i.split(' ')
            if i == ['']:
                continue
            i[len(i) - 1] = i[len(i) - 1].removesuffix("\n")
            i[len(i) - 1] = i[len(i) - 1].removesuffix(" ")
            if i not in self.graph:
                self.graph.append(i)


    ##mult appended !!!!!!!!!
    def reload(self):
        self.graph=[]
        with open("FILE.txt") as text:
            text = text.readlines()
        for i in text:
            i = i.rstrip()
            i = i.lstrip()
            i = i.split(' ')
            if i ==['']:
                continue

            i[len(i) - 1] = i[len(i) - 1].removesuffix("\n")
            i[len(i) - 1] = i[len(i) - 1].removesuffix(" ")
            if i not in self.graph:
                self.graph.append(i)

    def makeDS(self,edgelist,directed):
        self.graphDS={}
        self.weighted =True
        self.unvisited=[]
        print("MAKE_DS")
        self.vertix_list={}
        print("HERE")
        if directed:
            print("directed")
            for i in edgelist:
                if len(i) < 3:
                    print(i, "LESS")
                    self.weighted = False
                    if  len(i)==2:
                        self.graphDS.setdefault(i[0], []).append((i[1], 1))
                        if i[0] not in self.unvisited:
                            self.unvisited.append(i[0])
                        if i[1] not in self.unvisited:
                            self.unvisited.append(i[1])
                        continue
                elif len(i)>3:
                    return False

                print(i, "OKAY")
                try:
                    int(i[2])
                except:
                    return False

                self.graphDS.setdefault(i[0], []).append((i[1], int(i[2])))
                if i[0] not in self.unvisited:
                    self.unvisited.append(i[0])
                if i[1] not in self.unvisited:
                    self.unvisited.append(i[1])
        else:
            print("not directed")
            for i in edgelist:
                if len(i) < 3:
                    print(i, "LESS")
                    self.weighted = False
                    if  len(i)==2:
                        self.graphDS.setdefault(i[0], []).append((i[1], 1))
                        self.graphDS.setdefault(i[1], []).append((i[0], 1))
                        if i[0] not in self.unvisited:
                            self.unvisited.append(i[0])
                        if i[1] not in self.unvisited:
                            self.unvisited.append(i[1])
                        continue
                elif len(i)>3:
                    return False

                print(i, "OKAY")
                #Exception handling
                try:
                    int(i[2])
                except:
                    return False
                self.graphDS.setdefault(i[0],[]).append((i[1], int(i[2])))
                self.graphDS.setdefault(i[1],[]).append((i[0], int(i[2])))
                if i[0] not in self.unvisited:
                    self.unvisited.append(i[0])
                if i[1] not in self.unvisited:
                    self.unvisited.append(i[1])

        print("VERTIX NUM")
        self.number_verticies = len(self.vertix_list)
        print("First Done")
        print(self.graphDS)
        return True
    def makeHeuristicsList(self,lines):
        self.heuristic_valid =True
        self.heuristic_valid_long = False
        self.heuristic_dict={}
        for i in lines:
            i = i.rstrip()
            i = i.lstrip()
            i = i.split()
            print(i)
            if len(i)>2:
                self.heuristic_valid_long = True
                return False
            key = i[0]
            value = i[1]
            try:
                int(value)
            except:
                self.heuristic_valid=False
                return
            self.heuristic_dict[key]=int(value)

    def makeGoalsList(self,lines):
        print("Make Goal list started",lines)
        i=[]
        self.goals=[]
        i = lines
        i = i.rstrip()
        i = i.lstrip()
        i = i.split()


        for j in i:
            if not j == " " :
                self.goals.append(j)
        print("goal list made",self.goals)






    def makeNonWeightedAdj_list(self,directed):
        print("make non weighted adj list")

        self.adj_list={}
        if directed:
            print("directed")
            for i in self.graph:
                if  len(i)>=2:
                    self.graphDS.setdefault(i[0], []).append(i[1])
                print(i, "OKAY")

        else:
            print("not directed")
            for i in self.graph:
                if  len(i)>=2:
                    self.adj_list.setdefault(i[0], []).append(i[1])
                    self.adj_list.setdefault(i[1], []).append(i[0])
            print(i, "OKAY")




#{'2': {'3', '1'}, '3': {'2'}, '1': {'2'}}