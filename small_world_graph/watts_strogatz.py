import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from pyvis import network as net
from IPython.display import display, HTML

def watts_strogatz_graph(n_vertices : int = 10, n_edges_max : int = 3,
                         probability : float = 0.15, nx_graph : bool = True,
                         **kwargs):
    watts_strogatz = nx.watts_strogatz_graph(n_vertices,n_edges_max,probability)
    if nx_graph:
        G = net.Network(**kwargs)
        G.from_nx(watts_strogatz)
        return watts_strogatz, G
    return watts_strogatz, 
        
if __name__ == '__main__':
    a, g4 = watts_strogatz_graph(n_vertices = 20, height='400px', width='50%',notebook=True,heading='Zachary’s Karate Club graph')
    # g4 = net.Network()
    
    # g4.from_nx(watts_strogatz)
    
    g4.show_buttons(filter_=['physics'])
    g4.show('karate.html')
