"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children: list=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> list[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return res