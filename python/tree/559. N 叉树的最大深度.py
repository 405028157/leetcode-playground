"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        l = []
        for child in root.children:
            l.append(self.maxDepth(child))
        
        if not l:
            return 1
        
        return max(l) + 1