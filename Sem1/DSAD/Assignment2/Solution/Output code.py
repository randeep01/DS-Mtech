# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:19:40 2020

@author: harshit
"""

src = 'a'
dec = 'd'
print([(weight, [n.data for n in node]) for (weight, node) in g.dijkstra(a)])
temp = ([(weight, [n.data for n in node]) for (weight, node) in g.dijkstra(a)])
for i in range(len(temp)):
    print(temp[i])
    if temp[i][1][0]==src and temp[i][1][-1]==dec:
        route = temp[i][1]
        minDist = temp[i][0]
        time = (minDist/80)*60
        break
minutes = int(time)
seconds = int((time - minutes)*60
path = str([node for node in route])
print("Shortest route from the hospital "+src" to reach airport "+dec+" is " + path) 
print("and it has minimum travel distance "+str(minDist))
print("it will take ",str(minutes)+":"+str(seconds)," minutes for the ambulance to reach the airport.")






        

