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
        if node is None:
            return None
        
        hashmap = {}
        

        def dfs(old_node):
            if old_node in hashmap:
                return hashmap[old_node]
            
            new_node = Node(old_node.val)
            
            hashmap[old_node] = new_node

            for neighbors in old_node.neighbors:
                cloned_neighbor = dfs(neighbors)
                new_node.neighbors.append(cloned_neighbor)


            
            
            return new_node

        return dfs(node)
