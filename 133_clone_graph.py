"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return

        copies = {}

        def clone_rec(n):
            copy = Node(n.val)
            copies[n] = copy
            for nei in n.neighbors:
                if nei in copies:
                    copy.neighbors.append(copies[nei])
                else:
                    clone_rec(nei)
                    copy.neighbors.append(copies[nei])
        
        clone_rec(node)
        return copies[node]

