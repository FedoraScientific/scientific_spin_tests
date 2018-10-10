
import networkx as nx
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
G=nx.Graph()
#G.add_nodes_from([2,3])
G.add_edges_from([(1,2),(1,3),(2,3)])
print('Number of nodes: {0}'.format(G.number_of_nodes()))

nx.draw(G)
plt.savefig("test.png")