# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:05:38 2020

@author: sidus
"""

w_graph = Graph.create_from_nodes([a,b,c,d,e,f])

w_graph.connect(a,b,5)
w_graph.connect(a,c,10)
w_graph.connect(a,e,2)
w_graph.connect(b,c,2)
w_graph.connect(b,d,4)
w_graph.connect(c,d,7)
w_graph.connect(c,f,10)
w_graph.connect(d,e,3)

w_graph.print_adj_mat()