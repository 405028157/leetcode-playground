"""
用后序遍历，从下往上找要删除的节点。首先后序遍历，是从下往上删的，因此，只需要检查当前节点是否需要删，若当前节点不需要删，他的孩子也不用管，因为已经先一步维
持到了应该的状态。其次，若当前节点需要删，当前节点最多有一个孩子（就可以简单的把孩子提到当前节点的位置），因为若当前节点node不在范围[low, high]里，那么若node.val < low,
则曾经node.left.val < node.val < low, 左孩子早被删，或者若node.val > high, 则曾经node.right.val > node.val > high，右孩子早被删。也有可能左，右孩子都被删，
比如node.left.val < node.val < node.right.val < low。但是一旦有剩下的孩子，则孩子一定满足条件（因为是从下往上删的）

https://leetcode-cn.com/problems/trim-a-binary-search-tree/solution/li-yong-hou-xu-bian-li-he-er-cha-shu-de-dzrtx/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        
        # 叶子节点
        if not (root.left or root.right):
            if root.val > high or root.val < low:
                return None
            return root
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        if root.val > high or root.val < low:
            if not (root.left or root.right):
                root = None
            elif not root.left:
                root = root.right
            else:
                root = root.left
        
        return root

"""
官方非常快的解法，有点像二分
class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
"""