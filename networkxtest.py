import networkx as nx
G=nx.Graph()
G.add_edge(1,2,color='red',weight=0.84,size=300)
print(G[1][2]['size'])
