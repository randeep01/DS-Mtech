# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:38:49 2020

@author: sidus
"""

# Driver program to test the above functions 
def main():
    parentFolderPath = ''
    inputFileName = 'inputPS6.txt'
#    outputFile = 'outputPS6.txt'
    with open(parentFolderPath+inputFileName, 'r') as inpf:
        fileText = inpf.readlines()
                

    city = City(fileText)
    graph = Graph(city.count) 
    print("count "+ str(city.count))
    for x in range(len(city.routes)): 
        src = ord(city.routes[x].start.strip()) - ord('a')
        dest  = ord(city.routes[x].end.strip()) - ord('a')
        weight =  int(city.routes[x].dist)
        graph.addEdge(src,dest ,weight)
    start = ord(city.src.strip()) - ord('a')
    end = ord(city.dest.strip()) - ord('a')
    print(start)
    print(end)
    dist = graph.dijkstra(start,end)
    print("hospital dist " + str(dist))
    print("time " + str((dist/80)*60) )

if __name__=="__main__":
    main()
