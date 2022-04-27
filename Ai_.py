from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import os

import Algo
import main, Graph
from pyvis.network import Network

G = Graph.GraphDS("default")
print(G.graph)


class Ui_MainWindow(object):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph.html"))
    local_url = QtCore.QUrl.fromLocalFile(file_path)

    def __init__(self):
        self.Directed_clicked = False
        self.counterPhysics = 0

    def setupUi(self, MainWindow):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "graph.html"))
        local_url = QtCore.QUrl.fromLocalFile(file_path)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEntry.setGeometry(QtCore.QRect(0, 40, 271, 511))
        self.TextEntry.setObjectName("TextEntry")
        self.Directed_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Directed_Button.setGeometry(QtCore.QRect(0, 10, 111, 23))
        self.Directed_Button.setObjectName("Directed_Button")
        self.Directed_Button.setCheckable(True)
        self.Directed_Button.setChecked(False)
        self.Physics_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Physics_Button.setGeometry(QtCore.QRect(280, 10, 101, 23))
        self.Physics_Button.setCheckable(True)
        self.Physics_Button.setChecked(True)
        self.Physics_Button.setDefault(True)
        self.Physics_Button.setObjectName("Physics_Button")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.webEngineView.load(self.local_url)
        self.webEngineView.setGeometry(279, 39, 601, 511)
        self.UniformCostButton = QtWidgets.QPushButton(self.centralwidget)
        self.UniformCostButton.setGeometry(QtCore.QRect(20, 560, 131, 61))
        self.UniformCostButton.setObjectName("UniformCostButton")
        self.DFS_Button = QtWidgets.QPushButton(self.centralwidget)
        self.DFS_Button.setGeometry(QtCore.QRect(170, 560, 75, 61))
        self.DFS_Button.setObjectName("DFS_Button")
        self.BFSButton = QtWidgets.QPushButton(self.centralwidget)
        self.BFSButton.setGeometry(QtCore.QRect(260, 560, 75, 61))
        self.BFSButton.setObjectName("BFSButton")
        self.Start_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Start_line_edit.setGeometry(QtCore.QRect(740, 10, 41, 20))
        self.Start_line_edit.setObjectName("Start_line_edit")
        self.goal_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.goal_lineEdit.setGeometry(QtCore.QRect(832, 10, 41, 20))
        self.goal_lineEdit.setObjectName("goal_lineEdit")
        self.Start_label = QtWidgets.QLabel(self.centralwidget)
        self.Start_label.setGeometry(QtCore.QRect(708, 10, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Start_label.setFont(font)
        self.Start_label.setObjectName("Start_label")
        self.Goal_label = QtWidgets.QLabel(self.centralwidget)
        self.Goal_label.setGeometry(QtCore.QRect(800, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        self.Goal_label.setFont(font)
        self.Goal_label.setObjectName("Goal_label")
        self.iterative_deepening_Button = QtWidgets.QPushButton(self.centralwidget)
        self.iterative_deepening_Button.setGeometry(QtCore.QRect(360, 560, 121, 61))
        self.iterative_deepening_Button.setObjectName("iterative_deepening_Button")
        self.Lim_DFS_button = QtWidgets.QPushButton(self.centralwidget)
        self.Lim_DFS_button.setGeometry(QtCore.QRect(664, 558, 121, 61))
        self.Lim_DFS_button.setObjectName("Lim_DFS_button")
        self.Limited_dfs_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Limited_dfs_lineEdit.setGeometry(QtCore.QRect(794, 598, 81, 20))
        self.Limited_dfs_lineEdit.setObjectName("Limited_dfs_lineEdit")
        self.limit_limited_dfs_label = QtWidgets.QLabel(self.centralwidget)
        self.limit_limited_dfs_label.setGeometry(QtCore.QRect(800, 570, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.limit_limited_dfs_label.setFont(font)
        self.limit_limited_dfs_label.setObjectName("limit_limited_dfs_label")
        self.Limit_Iterative_deepening_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Limit_Iterative_deepening_line_edit.setGeometry(QtCore.QRect(570, 570, 51, 20))
        self.Limit_Iterative_deepening_line_edit.setObjectName("Limit_Iterative_deepening_line_edit")
        self.Limit_iterative_deepening_label = QtWidgets.QLabel(self.centralwidget)
        self.Limit_iterative_deepening_label.setGeometry(QtCore.QRect(500, 570, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Limit_iterative_deepening_label.setFont(font)
        self.Limit_iterative_deepening_label.setObjectName("Limit_iterative_deepening_label")
        self.iterations_label = QtWidgets.QLabel(self.centralwidget)
        self.iterations_label.setGeometry(QtCore.QRect(500, 590, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.iterations_label.setFont(font)
        self.iterations_label.setObjectName("iterations_label")
        self.iterative_deep_iter_linde_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.iterative_deep_iter_linde_edit.setGeometry(QtCore.QRect(570, 590, 51, 20))
        self.iterative_deep_iter_linde_edit.setObjectName("iterative_deep_iter_linde_edit")
        self.Cost_label = QtWidgets.QLabel(self.centralwidget)
        self.Cost_label.setGeometry(QtCore.QRect(410, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Cost_label.setFont(font)
        self.Cost_label.setObjectName("Cost_label")
        self.Cost_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Cost_line_edit.setGeometry(QtCore.QRect(440, 10, 261, 20))
        self.Cost_line_edit.setReadOnly(True)
        self.Cost_line_edit.setClearButtonEnabled(False)
        self.Cost_line_edit.setObjectName("Cost_line_edit")
        self.Heuristic_Text_entry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Heuristic_Text_entry.setGeometry(QtCore.QRect(890, 40, 131, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Heuristic_Text_entry.setFont(font)
        self.Heuristic_Text_entry.setTabChangesFocus(False)
        self.Heuristic_Text_entry.setObjectName("Heuristic_Text_entry")
        self.Astar_button = QtWidgets.QPushButton(self.centralwidget)
        self.Astar_button.setGeometry(QtCore.QRect(890, 560, 131, 31))
        self.Astar_button.setObjectName("Astar_button")
        self.Greedy_button = QtWidgets.QPushButton(self.centralwidget)
        self.Greedy_button.setGeometry(QtCore.QRect(890, 590, 131, 31))
        self.Greedy_button.setObjectName("Greedy_button")
        self.FormatLabel = QtWidgets.QLabel(self.centralwidget)
        self.FormatLabel.setGeometry(QtCore.QRect(190, 40, 81, 21))
        self.FormatLabel.setObjectName("FormatLabel")
        self.Heuristic_list = QtWidgets.QLabel(self.centralwidget)
        self.Heuristic_list.setGeometry(QtCore.QRect(910, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Heuristic_list.setFont(font)
        self.Heuristic_list.setObjectName("Heuristic_list")

        self.retranslateUi(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TextEntry.setFont(font)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TextEntry.setToolTip(_translate("MainWindow", "ex->2 3 1 -> Node 2 Node 3 Edge 1"))
        self.TextEntry.setStatusTip(_translate("MainWindow", "ex->2 3 1 -> Node 2 Node 3 Edge 1"))
        self.TextEntry.setPlainText(_translate("MainWindow", "2 3 1\n" "1 2\n" ""))
        self.Directed_Button.setText(_translate("MainWindow", "Directed"))
        self.Physics_Button.setText(_translate("MainWindow", "Physics"))
        self.UniformCostButton.setText(_translate("MainWindow", "Uniform cost search"))
        self.DFS_Button.setText(_translate("MainWindow", "DFS"))
        self.BFSButton.setText(_translate("MainWindow", "BFS"))
        self.Start_line_edit.setStatusTip(_translate("MainWindow", "Start Node"))
        self.goal_lineEdit.setStatusTip(_translate("MainWindow", "Goal Node"))
        self.Start_label.setText(_translate("MainWindow", "Start"))
        self.Goal_label.setText(_translate("MainWindow", "Goal"))
        self.iterative_deepening_Button.setText(_translate("MainWindow", "Iterative deepening"))
        self.Lim_DFS_button.setText(_translate("MainWindow", "Limited Dfs"))
        self.limit_limited_dfs_label.setText(_translate("MainWindow", "Limit:"))
        self.Limit_iterative_deepening_label.setText(_translate("MainWindow", "Max Depth:"))
        self.iterations_label.setText(_translate("MainWindow", "Step:"))
        self.Cost_label.setText(_translate("MainWindow", "Cost:"))
        self.Cost_line_edit.setStatusTip(_translate("MainWindow", "Cost will show infinity if there is no such route "))
        self.Heuristic_Text_entry.setToolTip(_translate("MainWindow", "format->Node Heuristic"))
        self.Heuristic_Text_entry.setStatusTip(_translate("MainWindow", "Node heuristic ex:A 5"))
        self.Astar_button.setText(_translate("MainWindow", "A* search"))
        self.Greedy_button.setText(_translate("MainWindow", "Greedy search"))
        self.FormatLabel.setText(_translate("MainWindow", "Node Node Edge"))
        self.Heuristic_list.setText(_translate("MainWindow", "Heuristics list"))
        self.Physics_Button.setChecked(True)
        self.Physics_Button.clicked.connect(lambda: self.Phys_clicked())
        self.Directed_Button.clicked.connect(lambda: self.directed_clicked())
        self.TextEntry.textChanged.connect(lambda: self.text_Changed())
        self.DFS_Button.clicked.connect(lambda: self.DFS_clicked())
        self.BFSButton.clicked.connect(lambda: self.BFS_clicked())
        self.Lim_DFS_button.clicked.connect(lambda: self.LimDFS_clicked())
        self.iterative_deepening_Button.clicked.connect(lambda: self.Itr_deep_clicked())
        self.UniformCostButton.clicked.connect(lambda: self.UC_clicked())
        self.Astar_button.clicked.connect(lambda: self.A_star_clicked())
        self.Greedy_button.clicked.connect(lambda: self.GreedyClicked())

    def Phys_clicked(self):
        if self.counterPhysics % 2 == 0:  # odd->ucnchecked
            self.counterPhysics = self.counterPhysics + 1
            main.g.toggle_physics(False)
            main.g.save_graph("graph.html")
        else:
            self.counterPhysics = self.counterPhysics + 1
            main.g.toggle_physics(True)
            main.g.save_graph("graph.html")
        self.webEngineView.load(self.local_url)

    def directed_clicked(self):
        if self.Directed_Button.isChecked() == True:
            main.directed_on()
            main.g.directed = True
            self.Physics_Button.setEnabled(False)
        else:
            self.text_Changed()
            main.g.directed = False
            self.Physics_Button.setEnabled(True)

        main.g.save_graph("graph.html")
        self.webEngineView.load(self.local_url)

    def text_Changed(self):
        with open("FILE.txt", 'w') as f:
            f.write(self.TextEntry.toPlainText())
        G.reload()
        print(G.graph)
        ##reload graph from data structure
        temp = Network()
        for i in G.graph:
            if len(i) == 1:
                temp.add_node(i[0])
            elif (len(i) == 2):
                temp.add_node(i[0])
                temp.add_node(i[1])
                temp.add_edge(i[0], i[1])
            elif (len(i) == 3):
                temp.add_node(i[0])
                temp.add_node(i[1])
                temp.add_edge(i[0], i[1], label=str(i[2]), weight=int(i[2]))
        main.g = temp
        if self.Directed_Button.isChecked() == True:
            main.directed_on()
        main.g.save_graph("graph.html")

        ##update .HTML
        self.webEngineView.load(self.local_url)

    def DFS_clicked(self):
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        self.text_Changed()

        ## get adj_list
        print("DFS CLICKED")
        G.adj_list = main.g.get_adj_list()
        print(G.adj_list)
        # do DFS
        print(self.Start_line_edit.text(),"Start")
        print(self.goal_lineEdit.text(),"Goal")
        temp = Algo.DFS(G.adj_list,self.Start_line_edit.text(),self.goal_lineEdit.text(),visited=[],path=[])
        print(temp,"DFS DONE")
        # change color of nodes and edges
        if temp:
            self.color_path(temp)
            if self.Directed_Button.isChecked():
                main.directed_on()
            self.webEngineView.load(self.local_url)

    def LimDFS_clicked(self):
        ## get adj_list
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        print("Limited DFS CLICKED")
        G.adj_list = main.g.get_adj_list()
        print(G.adj_list)
        # do Limited_DFS
        print(self.Start_line_edit.text(),"Start")
        print(self.goal_lineEdit.text(),"Goal")
        print(self.Limited_dfs_lineEdit.text(),"Limit")
        temp = Algo.Limited_DFS(G.adj_list,self.Start_line_edit.text(),self.goal_lineEdit.text(),int(self.Limited_dfs_lineEdit.text()),0,visited=[],path=[])
        print(temp,"Limited DFS DONE")
        # change color of nodes and edges
        if temp:
            self.color_path(temp)
            if self.Directed_Button.isChecked():
                main.directed_on()
            self.webEngineView.load(self.local_url)

    def Itr_deep_clicked(self):
        ## get adj_list
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        print("Limited DFS CLICKED")
        graph = main.g.get_adj_list()
        print(graph)
        # do Limited_DFS
        print(self.Start_line_edit.text(),"Start")
        print(self.goal_lineEdit.text(),"Goal")
        print(int(self.iterative_deep_iter_linde_edit.text()),"Step")
        print(int(self.Limit_Iterative_deepening_line_edit.text()),"MAX DEPTH")
        S=self.Start_line_edit.text()
        G=self.goal_lineEdit.text()
        step = int(self.iterative_deep_iter_linde_edit.text())
        Max_dep = int(self.Limit_Iterative_deepening_line_edit.text())

        temp = Algo.Itr_Lim_DFS(graph, S, G, Max_dep, step)
        print(temp,"Limited DFS DONE")
        # change color of nodes and edges
        if temp:
            self.color_path(temp)
            if self.Directed_Button.isChecked():
                main.directed_on()
            self.webEngineView.load(self.local_url)




    def BFS_clicked(self):
        ## get adj_list
        print("BFS CLICKED")
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        G.adj_list = main.g.get_adj_list()
        print(G.adj_list)
        # do BFS
        print(self.Start_line_edit.text(),"Star")
        print(self.goal_lineEdit.text(),"Goal")
        temp = Algo.BFS(G.adj_list,self.Start_line_edit.text(),self.goal_lineEdit.text(),Queue=[],visited=[],path=[])
        print(temp,"BFS DONE")
        # change color of nodes and edges
        self.color_path(temp)
        if self.Directed_Button.isChecked():
            main.directed_on()
        self.webEngineView.load(self.local_url)

    def color_path(self, path):
        temp = Network()
        temp.options.edges.inherit_colors(False)
        print(path)
        for i in path:
            temp.add_node(i,color='#00ff1e')
        print("NODES ADDED")
        for i in range(len(path) - 1):
            temp.add_edge(path[i], path[i + 1], color='#00ff1e')
        print("EDGES ADDED")
        for i in G.graph:
            if len(i) == 1:
                temp.add_node(i[0])
            elif (len(i) == 2):
                temp.add_node(i[0])
                temp.add_node(i[1])
                temp.add_edge(i[0], i[1])
            elif (len(i) == 3):
                temp.add_node(i[0])
                temp.add_node(i[1])
                temp.add_edge(i[0], i[1], label=str(i[2]), weight=int(i[2]))
        main.g = temp
        main.g.save_graph("graph.html")

    def color_path_dir(self, path,graph):
        temp = Network()
        temp.options.edges.inherit_colors(False)
        print(path)
        for i in path:
            temp.add_node(i, color='#00ff1e')
        print("NODES ADDED")
        for i in range(len(path) - 1):
            t1 = path[i]
            t2 = path[i+1]
            l1 = graph[t1]
            for j in l1:
                if j[0]==t2:
                    Weight = j[1]
            temp.add_edge(path[i], path[i + 1], color='#00ff1e',label=Weight)
        print("EDGES ADDED")
        for i in G.graph:
            if len(i) == 1:
                temp.add_node(i[0])
            elif (len(i) == 2):
                temp.add_node(i[0])
                temp.add_node(i[1])
                temp.add_edge(i[0], i[1])
            elif (len(i) == 3):
                temp.add_node(i[0])
                temp.add_node(i[1])
                temp.add_edge(i[0], i[1], label=str(i[2]), weight=int(i[2]))
        main.g = temp
        main.g.save_graph("graph.html")
    def UC_clicked(self):
        print("UC CLICKED")
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        if G.makeDS(G.graph,self.Directed_Button.isChecked()):
            if G.weighted==False:
                self.Cost_line_edit.setText("Cost cant be determined")
                return
            print("DS MADE")
            print(self.Start_line_edit.text(), "Start")
            start = self.Start_line_edit.text()
            print(self.goal_lineEdit.text(), "Goal")
            goal = self.goal_lineEdit.text()
            parent_map , shortest_path = (Algo.Uniform_Cost_search(G.graphDS,G.unvisited,start))
            if parent_map =={}:
                self.Cost_line_edit.setText("infinity")
                return
            cost = shortest_path[goal]
            path = Algo.dijkstra_result(parent_map,shortest_path,start,goal)
            print("PATH",path,G.graphDS)

            if self.Directed_Button.isChecked():
                print("Directed")
                print(G.graphDS)
                gds = G.graphDS
                self.color_path_dir(path,gds)
                main.directed_on()
            else:
                print("UNDIRECTED")
                self.color_path_dir(path,G.graphDS)
            self.webEngineView.load(self.local_url)
            print("LOCAL LOADED")
            self.Cost_line_edit.setText(str(cost))

    def A_star_clicked(self):
        print("A* CLICKED")
        lines = self.Heuristic_Text_entry.toPlainText().splitlines()
        G.makeHeuristicsList(lines)
        print("heuristic made",G.heuristic_dict)
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        if G.makeDS(G.graph,self.Directed_Button.isChecked()):
            if G.weighted==False:
                self.Cost_line_edit.setText("Cost cant be determined")
                return
            print("DS MADE")
            print(self.Start_line_edit.text(), "Start")
            start = self.Start_line_edit.text()
            print(self.goal_lineEdit.text(), "Goal")
            goal = self.goal_lineEdit.text()
            path,cost = (Algo.A_star_search(G.graphDS,G.unvisited,start,goal,G.heuristic_dict))
            print("PATH",path,G.graphDS)

            if self.Directed_Button.isChecked():
                print("Directed")
                print(G.graphDS)
                gds = G.graphDS
                self.color_path_dir(path,gds)
                main.directed_on()
            else:
                print("UNDIRECTED")
                self.color_path_dir(path,G.graphDS)
            self.webEngineView.load(self.local_url)
            print("LOCAL LOADED")
            self.Cost_line_edit.setText(str(cost))


    def GreedyClicked(self):
        lines = self.Heuristic_Text_entry.toPlainText().splitlines()
        G.makeHeuristicsList(lines)
        G.makeDS(G.graph,self.Directed_Button.isChecked())
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text()=="":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        path = Algo.greedy_Search(self.Start_line_edit.text(),self.goal_lineEdit.text(),G.heuristic_dict,G.graphDS)
        print("path inside GReedy clicked",path)
        self.color_path(path)
        self.webEngineView.load(self.local_url)
        print("LOCAL LOADED")




    @property
    def getTextEntry(self):
        return self.TextEntry.toPlainText()

    def getTextLimited_dfs(self):
        return self.Limited_dfs_lineEdit.toPlainText()

    def getTextIterative_dfs_limit(self):
        return self.Limit_Iterative_deepening_line_edit.toPlainText()

    def getTextIterative_dfs_iterations(self):
        return self.iterative_deep_iter_linde_edit.toPlainText()

    def getTextGoal(self):
        return self.goal_lineEdit.toPlainText()

    def getTextStart(self):
        return self.Start_line_edit.toPlainText()


if __name__ == "__main__":
    import sys

    main.makenet()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
