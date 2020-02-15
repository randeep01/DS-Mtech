# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:03:18 2020

@author: sidus
"""

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

graph = Graph.create_from_nodes([a,b,c,d,e,f])

graph.connect(a,b)
graph.connect(a,c)
graph.connect(a,e)
graph.connect(b,c)
graph.connect(b,d)
graph.connect(c,d)
graph.connect(c,f)
graph.connect(d,e)

graph.print_adj_mat()