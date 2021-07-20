"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children: list=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> list[int]:
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
                
        return output