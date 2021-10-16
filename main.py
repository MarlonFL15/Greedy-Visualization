from greedy_coloring import greedy_coloring
from draw import draw
import networkx as nx

G = nx.Graph()
G.add_edge(5, 1)
G.add_edge(5, 2)
G.add_edge(1, 2)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(2, 7)

colors = greedy_coloring(G)
draw(G, colors)
