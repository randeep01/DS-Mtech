# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:18:00 2020

@author: Group 030
"""
from collections import defaultdict 
import sys 
class Route:
    def __init__(self,start,end,dist):
        self.start = start
        self.end = end
        self.dist = dist
        
    def __str__(self):
        return self.start + " " + self.end + " " +str( self.dist )   
        
class City():

    def __init__(self,fileText):
        self.nodes = []
        self.count = 0
        self.src = ''
        self.dest = ''
        self.routes = []
        for line in fileText:
            line = line.replace("\n","")
            print(line)
            if "/" in line:
    #           Process line as a node
                line = line.replace(" ","")
                nodeDistSplit = line.split("/")
               #      print(nodeDistSplit)
                self.nodes = self.nodes + [nodeDistSplit[0],nodeDistSplit[1]]
               
                route = Route(nodeDistSplit[0],nodeDistSplit[1],nodeDistSplit[2])
               # print('$'+ str( route))
                self.routes = self.routes + [route]
                
            elif "Airport" in line:
                strSplit =  line.split(":")
                self.dest = strSplit[1]
            elif "Hospital" in line:
                strSplit = line.split(":")
                self.src = strSplit[1]
        self.count =  len(set(self.nodes))
        
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes  
    # of min heap. Needed for min heapify 
    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped.Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2
        
        if left < self.size and self.array[left][1]  < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min  
        # heap if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum  
    # node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is  
        # not hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)//2 ) 
  
            # move to parent index 
            i = (i - 1) // 2; 
  
    # A utility function to check if a given  
    # vertex 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
  
def printArr(dist, n,dest): 
    val = 0
    print("Vertex\tDistance from source")
    for i in range(n): 
        print("%d\t\t%d" % (i,dist[i]))
        if(i==dest):
            val = dist[i]
    return val        
  
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
  
    # Adds an edge to an undirected graph 
    def addEdge(self, src, dest, weight): 
  
        # Add an edge from src to dest.  A new node  
        # is added to the adjacency list of src. The  
        # node is added at the beginning. The first  
        # element of the node has the destination  
        # and the second elements has the weight 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
  
        # Since graph is undirected, add an edge  
        # from dest to src also 
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
  
    # The main function that calulates distances  
    # of shortest paths from src to all vertices.  
    # It is a O(ELogV) function 
    def dijkstra(self, src,dest): 
  
        V = self.V  # Get the number of vertices in graph 
        dist = []   # dist values used to pick minimum  
                    # weight edge in cut 
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        #  Initialize min heap with all vertices.  
        # dist value of all vertices 
        for v in range(V): 
            dist.append(sys.maxsize) 
            minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
            minHeap.pos.append(v) 
  
        # Make dist value of src vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[src] = src 
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
  
        # In the following loop, min heap contains all nodes 
        # whose shortest distance is not yet finalized. 
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
  
            # Traverse through all adjacent vertices of  
            # u (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less  
                # than its previously calculated distance 
                if minHeap.isInMinHeap(v) and dist[u] != sys.maxsize and pCrawl[1] + dist[u] < dist[v]: 
                        dist[v] = pCrawl[1] + dist[u] 
  
                        # update distance value  
                        # in min heap also 
                        minHeap.decreaseKey(v, dist[v]) 
  
        return printArr(dist,V,dest) 
  

#def preProcessInputFile(fileText):
#    nodeTraversalList = []
#    for line in fileText:
#        line = line.replace("\n","")
#        if "/" in line:
##           Process line as a node
#            line = line.replace(" ","")
#            nodeDistSplit = line.split("/")
#            print(nodeDistSplit)
#            nodeTraversalList = nodeTraversalList + [nodeDistSplit[0],nodeDistSplit[1]]
#        else:
#            print(line)
#    print(set(nodeTraversalList))
#    return len(set(nodeTraversalList)),set(nodeTraversalList)


# Driver program to test the above functions 
def main():
    parentFolderPath = ''
    inputFileName = 'inputPS6.txt'
#    outputFile = 'outputPS6.txt'
    with open(parentFolderPath+inputFileName, 'r') as inpf:
        fileText = inpf.readlines()
#    print(preProcessInputFile(fileText))
                

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
    print("hospital dist" + str(dist))


if __name__=="__main__":
    main()

