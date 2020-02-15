# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:06:35 2020

@author: sidus
"""

class Graph: 

    def __init__(self, nodes):
        self.adj_list = [ [node, []] for node in nodes ]
        for i in range(len(nodes)):
            nodes[i].index = i


    def connect_dir(self, node1, node2, weight = 1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        # Note that the below doesn't protect from adding a connection twice
        self.adj_list[node1][1].append((node2, weight))

    def connect(self, node1, node2, weight = 1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)

    
    def connections(self, node):
        node = self.get_index_from_node(node)
        return self.adj_list[node][1]
    
    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index