class GraphDS:
    graph = []
    graphDS ={}
    weighted = True
    adj_list=[]
    number_verticies=0
    vertix_list={}
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

    def makeDS(self,edgelist):
        print("MAKE_DS")
        self.vertix_list={}
        for i in edgelist:
            if len(i)<3:
                print(i,"LESS")
                self.weighted=False
                return {}
            print(i,"OKAY")
            self.graphDS[i[0]]=(i[1],i[2])
            for j in i:
                if j not in self.vertix_list:
                    self.vertix_list[j]=0
            self.number_verticies = len(self.vertix_list)
            print("First Done")
            print(self.graphDS)


