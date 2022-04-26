class GraphDS:
    graph = []
    graphDS ={}
    weighted = True
    adj_list=[]
    unvisited =[]
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
                    return {}
                print(i, "OKAY")
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
                    return {}
                print(i, "OKAY")
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



