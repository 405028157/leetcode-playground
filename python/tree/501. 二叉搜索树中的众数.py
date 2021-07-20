# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
有相同值的二叉搜索树（BST），中序遍历是一个非递减序列
"""

class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        self.base = None
        self.count = -1
        self.max_count = 0
        self.ans = []

        def inorder(node: TreeNode):
            if not node:
                return
            
            inorder(node.left)

            if node.val == self.base:
                self.count += 1
            else:
                self.base = node.val
                self.count = 1
            
            if self.count > self.max_count:
                self.ans = [node.val]
                self.max_count = self.count
            elif self.count == self.max_count:
                self.ans.append(node.val)

            inorder(node.right)

        inorder(root)

        return self.ans

"""
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        nums = []
        def mid_order(root):
            if root:
                mid_order(root.left)
                nums.append(root.val)
                mid_order(root.right)
        mid_order(root)
        m = collections.Counter(nums)
        max_value = max(m.values())
        result = []
        for key,value in m.items():
            if value == max_value:
                result.append(key)
        return result
"""