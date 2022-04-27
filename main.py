from pyvis.network import Network
import networkx as nx

net = Network()
g = Network(directed=True)
g.set_edge_smooth('dynamic')

def makenet():
    g.options.edges.inherit_colors(False)
    g.add_node('1')
    g.add_node('2')
    g.add_node('3')
    g.add_edge('1', '2')
    g.add_edge('2', '3', weight=1, label="1")
    g.save_graph("graph.html")


def physics_off():
    g.toggle_physics(False)
    g.save_graph("graph.html")


def physics_on():
    g.toggle_physics(True)
    g.save_graph("graph.html")


def save():
    g.save_graph("graph.html")






