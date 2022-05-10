from pyvis.network import Network
import networkx as nx

net = Network()
g = Network()


def makenet():
    g.options.edges.inherit_colors(False)
    g.add_node('1')
    g.add_node('2')
    g.add_node('3')
    g.add_edge('1', '2')
    g.add_edge('2', '3', weight=1, label="1")
    g.save_graph("graph.html")


def physics_off():
    g.barnes_hut(spring_length=160,damping=1,spring_strength=0,gravity=-1500)
    g.save_graph("graph.html")


def physics_on():
    g.barnes_hut(spring_strength=0.1,damping=0.09,spring_length=160)
    g.save_graph("graph.html")


def save():
    g.save_graph("graph.html")






