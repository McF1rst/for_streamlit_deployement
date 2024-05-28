import streamlit as st
from watts_strogatz import watts_strogatz_graph
import streamlit.components.v1 as components
import numpy as np

def main():
    st.title("Small world graph")
    
    st.sidebar.title('Choose paramters')
    vertices = st.sidebar.slider('Choose the number of vertices', 1, 100, 10)
    edges = st.sidebar.slider('Choose the maximum number of edges', 2, 100, 3)
    if edges > vertices : vertices = edges + 1
    probability = st.sidebar.number_input('Choose probability to change', 0., 1., 0.15)
    
    w_s, graph = watts_strogatz_graph(n_vertices=vertices, n_edges_max=edges, probability=probability, height='400px', width='100%', bgcolor = '#000000', notebook=True)
    graph.show_buttons(filter_=['physics'])
    graph.show('small_world.html')
    HtmlFile = open("small_world.html", 'r')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 900,width=890)

    #st.experimental_rerun()
if __name__ == '__main__':
    main()

