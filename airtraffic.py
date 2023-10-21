import matplotlib.pyplot as plt
import networkx as nx

# Step 1: Identify Airports and Routes

airports = ['A', 'B', 'C', 'D', 'E']
routes = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('A', 'E')]

# Step 2: Node and Edge Representation

G = nx.Graph()
G.add_nodes_from(airports)
G.add_edges_from(routes)

# Step 3: Edge Weights

edge_weights = {('A', 'B'): 500, ('B', 'C'): 300, ('C', 'D'): 200, ('D', 'E'): 400, ('A', 'E'): 600}

# Step 4: Graph Creation

pos = nx.spring_layout(G)  # you can choose a layout algorithm based on your preference
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')

# Draw edge labels with weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Display the graph
plt.show()
