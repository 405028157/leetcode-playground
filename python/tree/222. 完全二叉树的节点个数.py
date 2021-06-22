# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        node = root
        while node.left:
            depth += 1
            node = node.left
        
        l = 1 << depth
        r = (l << 1) - 1

        while l < r:
            mid = (l + r) >> 2
            path = 1 << (depth - 1)
            cur = root

            while path:
                if path & mid: 
                    cur = cur.right
                else:
                    cur = cur.left
                path >>= 1
            if node: # 使节点数为mid的节点存在，应该向右查找
                l = mid + 1
            else:
                r = mid - 1
        
        return l