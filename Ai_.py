from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtTest
import os
import itertools
import Algo
import main, Graph
from pyvis.network import Network
import sys
import time
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
        MainWindow.resize(1031, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEntry.setGeometry(QtCore.QRect(0, 60, 271, 491))
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
        self.Format1 = QtWidgets.QLabel(self.centralwidget)
        self.Format1.setGeometry(QtCore.QRect(0, 40, 271, 21))
        self.Format1.setStyleSheet("background-color: rgb(227, 227, 227); \n"
                                   "")
        self.Format1.setObjectName("Format1")
        self.Format2 = QtWidgets.QLabel(self.centralwidget)
        self.Format2.setGeometry(QtCore.QRect(890, 40, 131, 21))
        self.Format2.setStyleSheet("background-color: rgb(227, 227, 227); \n"
                                   "")
        self.Format2.setObjectName("Format2")
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
        self.Start_line_edit.setGeometry(QtCore.QRect(60, 630, 61, 20))
        self.Start_line_edit.setObjectName("Start_line_edit")
        self.goal_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.goal_lineEdit.setGeometry(QtCore.QRect(160, 630, 861, 20))
        self.goal_lineEdit.setObjectName("goal_lineEdit")
        self.Start_label = QtWidgets.QLabel(self.centralwidget)
        self.Start_label.setGeometry(QtCore.QRect(20, 630, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Start_label.setFont(font)
        self.Start_label.setObjectName("Start_label")
        self.Goal_label = QtWidgets.QLabel(self.centralwidget)
        self.Goal_label.setGeometry(QtCore.QRect(130, 630, 31, 20))
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
        self.Limit_iterative_deepening_label.setGeometry(QtCore.QRect(490, 570, 71, 21))
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
        self.Export_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Export_Button.setGeometry(QtCore.QRect(180, 10, 91, 23))
        self.Export_Button.setObjectName("Export_Button")
        self.Heuristic_Text_entry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Heuristic_Text_entry.setGeometry(QtCore.QRect(890, 60, 131, 491))
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
        self.Heuristic_list.setGeometry(QtCore.QRect(910, 10, 141, 21))
        self.Error_Label = QtWidgets.QLabel(self.centralwidget)
        self.Error_Label.setGeometry(QtCore.QRect(20, 660, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Error_Label.setFont(font)
        self.Error_Label.setObjectName("Error_Label")
        self.Error_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.Error_lineedit.setGeometry(QtCore.QRect(60, 660, 961, 21))
        self.Error_lineedit.setObjectName("Error_lineedit")
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Heuristic_list.setFont(font)
        self.Heuristic_list.setObjectName("Heuristic_list")
        self.Error_lineedit.setReadOnly(True)

        self.retranslateUi(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TextEntry.setFont(font)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TextEntry.setToolTip(_translate("MainWindow", "ex->A B 1 -> From (A)  To (B)  Edge = 1"))
        self.TextEntry.setStatusTip(_translate("MainWindow", "ex->A B 1 -> From (A)  To (B)  Edge = 1"))
        self.TextEntry.setPlainText(_translate("MainWindow", "2 3 1\n" "1 2\n" ""))
        self.Format1.setText(_translate("MainWindow", "  From  To   Edge"))
        self.Format2.setText(_translate("MainWindow", "  Node   heuristic"))
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
        #self.FormatLabel.setText(_translate("MainWindow", "Node Node Edge"))
        self.Heuristic_list.setText(_translate("MainWindow", "Heuristics list"))
        self.Export_Button.setText(_translate("MainWindow", "Export"))
        self.Physics_Button.setChecked(True)
        self.Error_Label.setText(_translate("MainWindow", "Error"))

        try:
            self.Physics_Button.clicked.connect(lambda: self.Phys_clicked())
            self.Directed_Button.clicked.connect(lambda: self.directed_clicked())
            self.TextEntry.textChanged.connect(lambda: self.text_Changed())
            self.DFS_Button.clicked.connect(lambda: self.DFS_clicked())
            self.BFSButton.clicked.connect(lambda: self.BFS_clicked())
            self.iterative_deepening_Button.clicked.connect(lambda: self.Itr_deep_clicked())
            self.Lim_DFS_button.clicked.connect(lambda: self.LimDFS_clicked())
            self.UniformCostButton.clicked.connect(lambda: self.UC_clicked())
            self.Astar_button.clicked.connect(lambda: self.A_star_clicked())
            self.Greedy_button.clicked.connect(lambda: self.GreedyClicked())
            self.Export_Button.clicked.connect(lambda: self.Export_Clicked())
        except:
            self.Error_lineedit.setText("Error")

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
        self.text_Changed()

        main.g.save_graph("graph.html")
        self.webEngineView.load(self.local_url)

    def text_Changed(self):
        with open("FILE.txt", 'w') as f:
            f.write(self.TextEntry.toPlainText())

        G.reload()

        print(G.graph)
        ##Check each in graph have <<char char int>>
        for l in G.graph:
            if len(l)>3:
                self.Error_lineedit.setText("Enter only 3 values Node Node Edge, <<char char int>>")
                return
            if len(l)==3:
                try:
                    int(l[2])
                except:
                    self.Error_lineedit.setText("Weight must be <<integer>>")
                    return
        ##reload graph from data structure
        if self.Directed_Button.isChecked():
            temp = Network(directed=True)
            temp.set_edge_smooth('dynamic') ##Caution##
        else:
            temp = Network()

        if self.Physics_Button.isChecked():
            temp.toggle_physics(True)
        else:
            temp.toggle_physics(False)
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
                ##Caution
                try:
                    int(i[2])
                except:
                    self.Error_lineedit.setText("weight must be integer")
                    return
                temp.add_edge(i[0], i[1], label=str(i[2]), weight=int(i[2]))

        main.g = temp
        main.g.save_graph("graph.html")

        ##update .HTML
        self.webEngineView.load(self.local_url)
        ## Clear Error
        self.Error_lineedit.setText(" ")
    def Export_Clicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")
        main_dir = os.getcwd()
        os.chdir(main_dir+"\Export")
        print(os.getcwd(),"inside EXPORT")
        def unique_file(basename, ext):
            actualname = "%s.%s" % (basename, ext)
            c = itertools.count()
            while os.path.exists(actualname):
                actualname = "%s (%d).%s" % (basename, next(c) , ext)
                #next(c) == c++
            return actualname

        #Exported_Text
        print("before catastrophe")
        print (unique_file("Exported_Text","txt"))
        with open(unique_file("Exported_Text","txt"), 'w') as f:
            f.write(self.TextEntry.toPlainText())
        EXP_GRAPH = main.g
        HTML = unique_file("Exported_graph","html")
        EXP_GRAPH.save_graph(HTML)
        os.chdir(main_dir)
        print(main_dir ,"OUTSIDE EXPORT")

    def DFS_clicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")

        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Error_lineedit.setText("ENTER VALID START/END")
            return
        self.text_Changed()

        ## get adj_list
        print("DFS CLICKED")
        G.adj_list = main.g.get_adj_list()
        print(G.adj_list)
        # do DFS
        print(self.Start_line_edit.text(),"Start")
        print(self.goal_lineEdit.text(),"Goal")
        G.makeGoalsList(self.goal_lineEdit.text())
        Algo.VIS_NODES_ALGO=[]
        try:
            path = Algo.DFS(G.adj_list,self.Start_line_edit.text(),G.goals,visited=[],path=[])

        except:
            self.Error_lineedit.setText("Error getting DFS path")
            return

        print(path,"DFS DONE",Algo.VIS_NODES_ALGO)
        G.makeDS(G.graph,self.Directed_Button.isChecked())
        cost = 0
        # change color of nodes and edges
        graphDs = G.graphDS
        print(path,"path")
        try:
            for i in range(len(path)-1):
                for j in graphDs.get(path[i]):
                    print(j,"i")
                    print(j[0],"i[0]")
                    print(j[1], "i[1]")
                    print(j[0],path[i+1],"similarity")
                    if j[0] == path[i+1]:
                        print("here")
                        cost+=int(j[1])
            print(cost,"COST")
            self.Cost_line_edit.setText(str(cost))
            print("here")
        except:
            self.Error_lineedit.setText("Invalid Cost")
            return

        self.color_path_dir(path,G.graphDS,Algo.VIS_NODES_ALGO)
        self.webEngineView.load(self.local_url)

    def LimDFS_clicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")
        ## get adj_list
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "" or self.Limited_dfs_lineEdit.text()=="":
            self.Error_lineedit.setText("ENTER VALID START/END")
            return
        print("Limited DFS CLICKED")
        G.adj_list = main.g.get_adj_list()
        print(G.adj_list)
        # do Limited_DFS
        print(self.Start_line_edit.text(),"Start")
        print(self.goal_lineEdit.text(),"Goal")
        print(self.Limited_dfs_lineEdit.text(),"Limit")
        G.makeGoalsList(self.goal_lineEdit.text())
        ##error int(self.Limited_dfs_lineEdit.text())
        Algo.VIS_NODES_ALGO=[]
        try:
            int(self.Limited_dfs_lineEdit.text())

        except:
            self.Error_lineedit.setText("Enter integer values in <Limit>")
            return

        try:
            Flag,path,vis_nodes = Algo.Limited_DFS(G.adj_list,self.Start_line_edit.text(),G.goals,int(self.Limited_dfs_lineEdit.text()),0,visited=[],path=[],extras=[])
        except:
            self.Error_lineedit.setText("Error getting Lim DFS path")
            return
        print(path,"Limited DFS DONE",vis_nodes)
        G.makeDS(G.graph,self.Directed_Button.isChecked())
        graphDs = G.graphDS
        cost = 0
        try:
            for i in range(len(path)-1):
                for j in graphDs.get(path[i]):
                    print(j,"i")
                    print(j[0],"i[0]")
                    print(j[1], "i[1]")
                    print(j[0],path[i+1],"similarity")
                    if j[0] == path[i+1]:
                        print("here")
                        cost+=int(j[1])
            print(cost,"COST")
            self.Cost_line_edit.setText(str(cost))
            print("here")
            # change color of nodes and edges
            print(len(path),"length path")
        except:
            self.Cost_line_edit.setText("Cant find cost")
        try:
            self.color_path_dir(path,graphDs,vis_nodes)
        except:
            self.Error_lineedit.setText("Cant color path!")
            return
        self.webEngineView.load(self.local_url)

##

    def Itr_deep_clicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")
        ##COLOR PATH DIR
        ## get adj_list
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "" or self.iterative_deep_iter_linde_edit.text()=="" or self.Limit_Iterative_deepening_line_edit.text()=="":
            self.Error_lineedit.setText("ENTER VALID START/END")
            return
        try:
            step = int(self.iterative_deep_iter_linde_edit.text())
            Max_dep = int(self.Limit_Iterative_deepening_line_edit.text())
        except:
            self.Error_lineedit.setText("Limit/Iterations must be integers")
            return

        if int(self.iterative_deep_iter_linde_edit.text())<1:
            self.Error_lineedit.setText("iterations must be integer and bigger than 0")
            return
        print("Limited DFS CLICKED")
        G.adj_list = main.g.get_adj_list()
        print(G.adj_list,"ADJ LIST")
        # do Limited_DFS
        print(self.Start_line_edit.text(),"Start")
        print(self.goal_lineEdit.text(),"Goal")
        ##ERROR NON INTEGERS
        print(int(self.iterative_deep_iter_linde_edit.text()),"Step")
        print(int(self.Limit_Iterative_deepening_line_edit.text()),"MAX DEPTH")
        ##
        S=self.Start_line_edit.text()
        G.makeGoalsList(self.goal_lineEdit.text())
        goals = G.goals


        G.makeDS(G.graph,self.Directed_Button.isChecked())
        graphDs =G.graphDS
        print("BEFORE STORM")
        Algo.VIS_NODES_ALGO=[]
        #Flag,path,vis_nodes = Algo.Limited_DFS(G.adj_list,self.Start_line_edit.text(),G.goals,int(self.Limited_dfs_lineEdit.text()),0,visited=[],path=[],extras=[])
        counter =step
        while counter <= Max_dep:
            try:
                Algo.VIS_NODES_ALGO=[]
                Flag,path,vis_nodes = Algo.Limited_DFS(G.adj_list,self.Start_line_edit.text(),G.goals,counter,0,visited=[],path=[],extras=[])
                print("DONE",counter)
            except:
                self.Error_lineedit.setText("getting path itr deep error")
            print(path,"Iter Limited DFS DONE", vis_nodes)
            cost = 0
            # change color of nodes and edges
            graphDs = G.graphDS
            print(path,"path")
            try:
                for i in range(len(path)-1):
                    for j in graphDs.get(path[i]):
                        print(j,"i")
                        print(j[0],"i[0]")
                        print(j[1], "i[1]")
                        print(j[0],path[i+1],"similarity")
                        if j[0] == path[i+1]:
                            print("here")
                            cost+=int(j[1])
                print(cost,"COST")
                self.Cost_line_edit.setText(str(cost))
                print("here")
            except:
                self.Error_lineedit.setText("Error#3 Invalid Path")
            # change color of nodes and edges
            self.color_path_dir(path,graphDs,vis_nodes)
            self.webEngineView.load(self.local_url)

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(4000, loop.quit)
            loop.exec_()
            counter += step

            if Flag:
                break



    def BFS_clicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")
        ## get adj_list
        print("BFS CLICKED")
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Error_lineedit.setText("ENTER VALID START/END")
            return
        G.adj_list = main.g.get_adj_list()
        print(G.adj_list)
        # do BFS
        print(self.Start_line_edit.text(),"Star")
        G.makeGoalsList(self.goal_lineEdit.text())
        print(G.goals,"Goal")
        try:
            temp,vis_nodes = Algo.BFS(G.adj_list,self.Start_line_edit.text(),G.goals,Queue=[],visited=[],path=[])
        except:
            self.Error_lineedit.setText("Error getting BFS path")
            return
        print(temp,"BFS DONE")
        # change color of nodes and edges
        G.makeDS(G.graph,self.Directed_Button.isChecked())

        path = temp
        cost = 0
        # change color of nodes and edges
        graphDs = G.graphDS
        print(path,"path")
        try:
            for i in range(len(path)-1):
                for j in graphDs.get(path[i]):
                    print(j,"i")
                    print(j[0],"i[0]")
                    print(j[1], "i[1]")
                    print(j[0],path[i+1],"similarity")
                    if j[0] == path[i+1]:
                        print("here")
                        cost+=int(j[1])
            print(cost,"COST")
            self.Cost_line_edit.setText(str(cost))
            print("here")
        except:
            self.Error_lineedit.setText("Error#3 Invalid Path")

        self.color_path_dir(temp,G.graphDS,vis_nodes)
        self.webEngineView.load(self.local_url)

    def color_path(self, path,vis_nodes):
        visited_edges=[]
        print(vis_nodes,"VISITED NODES LIST")
        #E33440 ->red
        temp = Network(directed=True)
        if self.Physics_Button.isChecked():
            temp.barnes_hut(spring_length=160, spring_strength=0.5, damping=0.69,gravity=-1500)
        else:
            temp.barnes_hut(spring_length=160, damping=1, spring_strength=0)
        temp.set_edge_smooth('dynamic')
        temp.options.edges.inherit_colors(False)
        G.makeHeuristicsList(self.Heuristic_Text_entry.toPlainText().splitlines())
        print(path)
        for i in path:
            if str(i) in G.heuristic_dict:
                print("HERE COLOR PATH")
                temp.add_node(i, color='#35DE4E',title=str(G.heuristic_dict[i]))
                print("HERE COLOR PATH1")
                continue
            temp.add_node(i,color='#35DE4E')
        for i in vis_nodes:
            if str(i) in G.heuristic_dict:
                print("HERE COLOR PATH z1")
                temp.add_node(i, color='#E33440',title=str(G.heuristic_dict[i]))
                print("HERE COLOR PATH z2")
                continue
            temp.add_node(i,color='#E33440')

        print("NODES ADDED")
        for i in range(len(path) - 1):
            visited_edges.append((path[i],path[i+1]))
            temp.add_edge(path[i], path[i + 1], color='#35DE4E')

        print("EDGES ADDED")
        for i in G.graph:
            if len(i) == 1:
                temp.add_node(i[0])
            elif (len(i) == 2):
                temp.add_node(i[0])
                temp.add_node(i[1])
                if ((i[0],i[1]) in visited_edges):
                    continue
                temp.add_edge(i[0], i[1])
            elif (len(i) == 3):
                temp.add_node(i[0])
                temp.add_node(i[1])
                if ((i[0],i[1]) in visited_edges):
                    continue
                temp.add_edge(i[0], i[1], label=str(i[2]), weight=int(i[2]))
        main.g = temp
        main.g.save_graph("graph.html")

    def color_path_dir(self, path,graph,vis_nodes):
        #Gold  #F4D03F
        #BLue  #3452F9
        #Red   #E33440
        #Green #35DE4E
        print("Here COLOR PATH 1")

        visited_edges = []
        if self.Directed_Button.isChecked():
            print("DIRECTED GRAPH CLICKED")
            temp = Network(directed=True)
            temp.set_edge_smooth('dynamic')
        else:
            temp = Network()
        print("Here COLOR PATH 1")

        if self.Physics_Button.isChecked():
            temp.toggle_physics(True)
        else:
            temp.toggle_physics(False)
        print("Here COLOR PATH 1")

        temp.options.edges.inherit_colors(False)
        G.makeHeuristicsList(self.Heuristic_Text_entry.toPlainText().splitlines())
        print("Here COLOR PATH 2")
        G.makeGoalsList(self.goal_lineEdit.text())
        print("Here COLOR PATH 3")


        print("Here COLOR PATH 1")
        temp.add_node(self.Start_line_edit.text(), color='#3452F9')
        for goal in G.goals:
            temp.add_node(goal, color='#F4D03F')

        print("Here COLOR PATH 1")

        print(path)
        for i in path:
            if  str(i) in G.heuristic_dict:
                print("COLOR PATH DIR 1")

                temp.add_node(i, color='#35DE4E',title=str(G.heuristic_dict[i]))
                continue
            temp.add_node(i, color='#35DE4E')
        for i in vis_nodes:
            if str(i) in G.heuristic_dict:
                print("COLOR PATH DIR 2")
                temp.add_node(i, color='#E33440',title=str(G.heuristic_dict[i]))
                continue
            temp.add_node(i,color='#E33440')
        print("NODES ADDED")
        print("GraphDS",graph)
        print(len(path),"PATH LENGTH")
        first_vis_edges = [()]
        if len(path)>0:
            print("HERE X")
            for i in range(len(path) - 1):
                print("iii",i)

                t1 = path[i]
                t2 = path[i+1]
                print("i1")
                l1 = graph[t1]
                print("i1")

                for j in l1:
                    if j[0]==t2:
                        Weight = j[1]
                        Weight_found = True
                print("i2")
                print("i2")
                if Weight_found:
                    trash = (path[i],path[i+1])
                    if (trash in first_vis_edges):
                        print("VISITED")
                    else:
                        temp.add_edge(path[i], path[i + 1], color='#35DE4E',label=Weight)
                        print(path[i], path[i + 1],"added 1")
                        visited_edges.append((path[i],path[i+1],str(Weight)))
                        print(path[i], path[i + 1],"added 1")
                        trash = (path[i],path[i + 1])
                        first_vis_edges.append(trash)
                        print(first_vis_edges,"FIR VIS EDGES iteration")

                else:
                    trash = (path[i], path[i + 1])
                    if trash in first_vis_edges:
                        print("VVISTted")
                    else:
                        temp.add_edge(path[i], path[i + 1], color='#35DE4E')
                        visited_edges.append((path[i],path[i+1]))
                        print(path[i], path[i + 1],"added 2")
                        trash = (path[i],path[i+1])
                        first_vis_edges+=trash
                Weight_found =False
                print("i3")
        print("FIR VISITED LIST",first_vis_edges)
        print("EDGES ADDED")
        for i in G.graph:
            if len(i) == 1:
                temp.add_node(i[0])
            elif (len(i) == 2):
                temp.add_node(i[0])
                temp.add_node(i[1])
                if ((i[0],i[1]) in first_vis_edges):
                    continue
                else:
                    temp.add_edge(i[0], i[1])
            elif (len(i) == 3):
                temp.add_node(i[0])
                temp.add_node(i[1])
                if ((i[0],i[1]) in first_vis_edges):
                    continue
                else:
                    temp.add_edge(i[0], i[1], label=str(i[2]), weight=int(i[2]))
        main.g = temp
        main.g.save_graph("graph.html")


    def UC_clicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")

        print("UC CLICKED")
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "":
            self.Error_lineedit.setText("ENTER VALID START/END")
            return

        if not G.makeDS(G.graph, self.Directed_Button.isChecked()):
            self.Error_lineedit.setText("Error in making graph data structure")
            return
        print("DS MADE")
        print(self.Start_line_edit.text(), "Start")
        start = self.Start_line_edit.text()
        G.makeGoalsList(self.goal_lineEdit.text())
        print(G.goals, "Goal")
        G.makeDS(G.graph, self.Directed_Button.isChecked())
        try:
            parent_map, shortest_path, vis_nodes = Algo.Uniform_Cost_search(G.graphDS, G.unvisited, start)
        except:
            self.Error_lineedit.setText("Error getting Uniform cost path")
            return
        if parent_map =={}:
            self.Cost_line_edit.setText("infinity")
            return
        min_goal_cost=1e9
        min_goal = "X"
        for goal in G.goals:
            if shortest_path[goal]<=min_goal_cost:
                min_goal_cost= shortest_path[goal]
                min_goal = goal

        print("min goal", min_goal, ":::", min_goal_cost)
        self.Cost_line_edit.setText(str(min_goal_cost))
        try:
            path = Algo.dijkstra_result(parent_map,shortest_path,start,min_goal)
        except:
            self.Error_lineedit.setText("cant get UC cost <make sure goal is reachable>")
            return
        print("PATH",path,G.graphDS)

        if self.Directed_Button.isChecked():
            print("Directed")
            print(G.graphDS)
            gds = G.graphDS
            self.color_path_dir(path,gds,vis_nodes)
        else:
            print("UNDIRECTED")
            self.color_path_dir(path,G.graphDS,vis_nodes)
        self.webEngineView.load(self.local_url)
        print("LOCAL LOADED")

    def A_star_clicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")

        print("A* CLICKED")
        G.makeDS(G.graph,self.Directed_Button.isChecked())
        lines = self.Heuristic_Text_entry.toPlainText().splitlines()
        G.makeHeuristicsList(lines)
        print("heuristic made",G.heuristic_dict)
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text() == "" or len(G.heuristic_dict) != len(G.unvisited):
            self.Cost_line_edit.setText("ENTER VALID START/END/Heuristics")
            return
        if G.makeDS(G.graph,self.Directed_Button.isChecked()):
            print("DS MADE")
            print(self.Start_line_edit.text(), "Start")
            start = self.Start_line_edit.text()
            G.makeGoalsList(self.goal_lineEdit.text())
            print(G.goals, "Goal")
            try:
                path,cost,vis_nodes = (Algo.A_star_search(G.graphDS,G.unvisited,start,G.goals,G.heuristic_dict))
            except:
                self.Error_lineedit.setText("Cant process A* algorithm")
                return
            print("PATH",path,G.graphDS)

            if self.Directed_Button.isChecked():
                print("Directed")
                print(G.graphDS)
                gds = G.graphDS
                self.color_path_dir(path,gds,vis_nodes)
            else:
                print("UNDIRECTED")
                self.color_path_dir(path,G.graphDS,vis_nodes)
            self.webEngineView.load(self.local_url)
            print("LOCAL LOADED")
            self.Cost_line_edit.setText(str(cost))
        else:
            self.Error_lineedit.setText("Error <<cant make graph data structure>>")
            return


    def GreedyClicked(self):
        ## Clear Error
        self.Error_lineedit.setText(" ")


        try:
            lines = self.Heuristic_Text_entry.toPlainText().splitlines()
            G.makeHeuristicsList(lines)
            if G.heuristic_valid==False:
                self.Error_lineedit.setText("heuristic value must be integer")
                return
            if G.heuristic_valid_long:
                self.Error_lineedit.setText("enter 2 values only <<char integer>>")
                return
        except:
            self.Error_lineedit.setText("Make sure Heuristic list in Node Heuristic format <<char int>> and not empty")
            return

        try:

            for i in G.unvisited:
                G.heuristic_dict[i]

        except:
            self.Error_lineedit.setText("Enter all Nodes Heuristics")
            return

        G.makeDS(G.graph,self.Directed_Button.isChecked())
        if self.Start_line_edit.text() == "" or self.goal_lineEdit.text()=="":
            self.Cost_line_edit.setText("ENTER VALID START/END")
            return
        G.makeGoalsList(self.goal_lineEdit.text())
        try:
            path,vis_nodes = Algo.greedy_Search(self.Start_line_edit.text(),G.goals,G.heuristic_dict,G.graphDS)
        except:
            self.Error_lineedit.setText("Error Getting greedy path")
            return
        print("path inside GReedy clicked",path)
        cost = 0
        # change color of nodes and edges
        graphDs = G.graphDS
        print(path,"path")
        try:
            for i in range(len(path)-1):
                for j in graphDs.get(path[i]):
                    print(j,"i")
                    print(j[0],"i[0]")
                    print(j[1], "i[1]")
                    print(j[0],path[i+1],"similarity")
                    if j[0] == path[i+1]:
                        print("here")
                        cost+=int(j[1])
            print(cost,"COST")
            self.Cost_line_edit.setText(str(cost))
            print("here")
        except:
            self.Error_lineedit.setText("Error#3 Invalid Path")
        self.color_path_dir(path,G.graphDS,vis_nodes)
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
