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
        route = print(temp[i][1])
        minDist = temp[i][0]
        time = (minDist/80)*60
        
       
print("Shortest route from the hospital" + ' ' +src + ' ' + "to reach airport" + ' ' +dec + ' ' + "is" + ' ') 

print("and it has minimum travel distance" + ' ' +str(minDist))

print("it will take" + ' ' +str(time))

minutes = int(time)
seconds = int((time - minutes)*60)




        

