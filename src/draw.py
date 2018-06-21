import math
import graph

from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Spectral8
from bokeh.plotting import figure
from bokeh.io import show, output_file

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
graph_data.bfs(graph_data.vertexes[0])
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
graph.node_renderer.glyph = Circle(radius=20, fill_color="color")

start_indexes = []
end_indexes = []

for start_index, vertex in enumerate(graph_data.vertexes):
    for e in vertex.edges:
        start_indexes.append(start_index)
        end_indexes.append(graph_data.vertexes.index(e.destination))



graph.edge_renderer.data_source.data = dict(
    start=start_indexes,
    end=end_indexes)


x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

### start of layout code


plot.renderers.append(graph)

value= [v.value for v in graph_data.vertexes]

label_source = ColumnDataSource(data=dict(x=x, y=y, v=value))

labels = LabelSet(x='x', y='y', text='v', level='overlay',
             render_mode='canvas', source=label_source,
            text_align='center', text_baseline='middle')

plot.add_layout(labels)

output_file("graph.html")
show(plot)