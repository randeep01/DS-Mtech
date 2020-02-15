# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:11:33 2020

@author: sidus
"""

class MinHeap(BinaryTree):

    def __init__(self, nodes, is_less_than = lambda a,b: a < b, get_index = None, update_node = lambda node, newval: newval):
        BinaryTree.__init__(self, nodes)
        self.order_mapping = list(range(len(nodes)))
        self.is_less_than, self.get_index, self.update_node = is_less_than, get_index, update_node
        self.min_heapify()

    # Heapify at a node assuming all subtrees are heapified
    def min_heapify_subtree(self, i):

        size = self.size()
        ileft = self.ileft(i)
        iright = self.iright(i)
        imin = i
        if( ileft < size and self.is_less_than(self.nodes[ileft], self.nodes[imin])):
            imin = ileft
        if( iright < size and self.is_less_than(self.nodes[iright], self.nodes[imin])):
            imin = iright
        if( imin != i):
            self.nodes[i], self.nodes[imin] = self.nodes[imin], self.nodes[i]
            # If there is a lambda to get absolute index of a node
            # update your order_mapping array to indicate where that index lives
            # in the nodes array (so lookup by this index is O(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[imin])] = imin
                self.order_mapping[self.get_index(self.nodes[i])] = i
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
            # Update order_mapping if applicable
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[0])] = 0
            self.min_heapify_subtree(0)
        elif self.size() == 1: 
            self.nodes.pop()
        else:
            return None
        # If self.get_index exists, update self.order_mapping to indicate
        # the node of this index is no longer in the heap
        if self.get_index is not None:
            # Set value in self.order_mapping to None to indicate it is not in the heap
            self.order_mapping[self.get_index(min)] = None
        return min

    # Update node value, bubble it up as necessary to maintain heap property
    def decrease_key(self, i, val):
        self.nodes[i] = self.update_node(self.nodes[i], val)
        iparent = self.iparent(i)
        while( i != 0 and not self.is_less_than(self.nodes[iparent], self.nodes[i])):
            self.nodes[iparent], self.nodes[i] = self.nodes[i], self.nodes[iparent]
            # If there is a lambda to get absolute index of a node
            # update your order_mapping array to indicate where that index lives
            # in the nodes array (so lookup by this index is O(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[iparent])] = iparent
                self.order_mapping[self.get_index(self.nodes[i])] = i
            i = iparent
            iparent = self.iparent(i) if i > 0 else None

    def index_of_node_at(self, i):
        return self.get_index(self.nodes[i])