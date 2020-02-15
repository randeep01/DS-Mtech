# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:05:40 2020

@author: sidus
"""

class MinHeap(BinaryTree):

    def __init__(self, nodes):
        BinaryTree.__init__(self, nodes)
        self.min_heapify()

    # Heapify at a node assuming all subtrees are heapified
    def min_heapify_subtree(self, i):
        size = self.size()
        ileft = self.ileft(i)
        iright = self.iright(i)
        imin = i
        if( ileft < size and self.nodes[ileft] < self.nodes[imin]):
            imin = ileft
        if( iright < size and self.nodes[iright] < self.nodes[imin]):
            imin = iright
        if( imin != i):
            self.nodes[i], self.nodes[imin] = self.nodes[imin], self.nodes[i]
            self.min_heapify_subtree(imin)


    # Heapify an un-heapified array
    def min_heapify(self):
        for i in range(len(self.nodes), -1, -1):
            self.min_heapify_subtree(i)

    def min(self):
        return self.nodes[0]

    def pop(self):
        min = self.nodes[0]
        if self.size() > 1:
            self.nodes[0] = self.nodes[-1]
            self.nodes.pop()
            self.min_heapify_subtree(0)
        elif self.size() == 1: 
            self.nodes.pop()
        else:
            return None
        return min

    # Update node value, bubble it up as necessary to maintain heap property
    def decrease_key(self, i, val):
        self.nodes[i] = val
        iparent = self.iparent(i)
        while( i != 0 and self.nodes[iparent] > self.nodes[i]):
            self.nodes[iparent], self.nodes[i] = self.nodes[i], self.nodes[iparent]
            i = iparent
            iparent = self.iparent(i) if i > 0 else None