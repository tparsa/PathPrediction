import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

class MapBuilder:

    def __init__(self):
        self.data_df = pd.read_csv('data.csv')
        number_of_edges = len(self.data_df)
        self.G = nx.DiGraph()
    #     pos = nx.layout.spring_layout(self.G)
    #     # self.G.draw()

    #     node_sizes = [3 + 10 * i for i in range(len(self.G))]
    #     M = self.G.number_of_edges()
    #     edge_colors = range(2, M + 2)
    #     dge_alphas = [(5 + i) / (M + 4) for i in range(M)]
        
    #     nodes = nx.draw_networkx_nodes(self.G, pos, node_size=node_sizes, node_color='blue')
    #     edges = nx.draw_networkx_edges(self.G, pos, node_size=node_sizes, arrowstyle='->',
    #                                     arrowsize=10, edge_color=edge_colors,
    #                                     edge_cmap=plt.cm.Blues, width=2)
    # # set alpha value for each edge
    #     for i in range(M):
    #         edges[i].set_alpha(edge_alphas[i])

    #     pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
    #     pc.set_array(edge_colors)
    #     plt.colorbar(pc)

    #     ax = plt.gca()
    #     ax.set_axis_off()
    #     plt.show()

        for i in range(0, number_of_edges):
            start = self.data_df.iloc[i]['start']
            end = self.data_df.iloc[i]['end']
            Energy = self.data_df.iloc[i]['Energy']
            Time = self.data_df.iloc[i]['Time']

            self.G.add_edge(start, end, Energy=Energy, Time=Time)

        black_edges = [edge for edge in self.G.edges()]

        # Need to create a layout when doing
        # separate calls to draw nodes and edges
        pos = nx.spring_layout(self.G)
        labels = nx.get_edge_attributes(self.G,'Energy')
        nx.draw_networkx_nodes(self.G, pos, cmap=plt.get_cmap('jet'), 
                         node_size = 500)
        nx.draw_networkx_labels(self.G, pos)
        # nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
        nx.draw_networkx_edges(self.G, pos, edgelist=black_edges, arrows=False)
        nx.draw_networkx_edge_labels(self.G,pos,edge_labels=labels)
        plt.show()

    def next_State(self, state):
        edges = [n for n in self.G.neighbors(state)]
        return edges

    def get_Reward(self, start, end):
        edge = self.data_df.loc[(self.data_df['start'] == (start)) & (self.data_df['end'] == (end))]
        Energy = edge.iloc[0]['Energy']
        Time = edge.iloc[0]['Time']
        return [np.random.normal(Energy, 0.5), np.random.normal(Time, 0.5)]

    def initial_state(self):
        return 1

    def terminal_state(self):
        return 11