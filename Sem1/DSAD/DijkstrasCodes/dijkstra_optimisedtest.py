# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:10:50 2020

@author: sidus
"""

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

g = Graph([a,b,c,d,e,f])

g.connect(a,b,5)
g.connect(a,c,10)
g.connect(a,e,2)
g.connect(b,c,2)
g.connect(b,d,4)
g.connect(c,d,7)
g.connect(c,f,10)
g.connect(d,e,3)

print([(weight, [n.data for n in node]) for (weight, node) in g.dijkstra(a)])