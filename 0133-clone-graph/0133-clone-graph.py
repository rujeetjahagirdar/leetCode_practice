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
            return node
        
        visited = {}

        q = deque([node])
        visited[node] = Node(node.val, [])

        while q:
            n = q.popleft()

            for neighbour in n.neighbors:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val, [])

                    q.append(neighbour)

                visited[n].neighbors.append(visited[neighbour])
        
        return visited[node]