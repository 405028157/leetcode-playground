"""
BFS 解法，这道题本质是让每个节点的左右孩子都互换一下
"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left

            # 这里left，right节点和原来的互换，但是不影响
            node.left and q.append(node.left)
            node.right and q.append(node.right)
        
        return root


"""
有个很经典的bug版本
"""

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if not (root.left or root.right):
            return root
        
        # 这条语句之后，root.left 和 root.right 就相同了
        root.left = self.invertTree(root.right)
        
        root.right = self.invertTree(root.left)
    
        return root