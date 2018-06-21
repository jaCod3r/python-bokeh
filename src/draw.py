import math
import graph

from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8
from bokeh.plotting import figure
from bokeh.io import show, output_file

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)


plot = figure(title="Graph Layout Demonstration", x_range=(0, 500), y_range=(0, 500),
              tools="", toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color="color")

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

### start of layout code
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

plot.renderers.append(graph)

output_file("graph.html")
show(plot)