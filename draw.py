import networkx as nx
from matplotlib import pyplot as plt
import matplotlib.animation as animation

dict_colors = {
    0: 'b',
    1: 'g',
    2: 'r',
    3: 'c',
    4: 'm',
    5: 'y',    
}

fig = plt.figure()

def animate(i, colors, G):
    current_colors = [dict_colors[colors[node]] if index+1 <= i else 'k' for index, (node, color) in enumerate(colors.items())]
    fig.clear()
    nx.draw_circular(G, node_color=current_colors, with_labels=True)
    

def draw(G, colors):
    
    anim = animation.FuncAnimation(fig, animate, frames=G.number_of_nodes()+2, interval=500, fargs=(colors,G))
    plt.show()

