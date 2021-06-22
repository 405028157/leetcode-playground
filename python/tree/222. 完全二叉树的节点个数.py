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
            # 为了解决，l 和 r 相差一，不能退出循环的情况
            mid = int((l + r + 1) / 2)
            path = 1 << (depth - 1)
            # print(f'l = {l}, r = {r}, mid = {mid}, path = {path}')
            cur = root

            while path:
                if path & mid: 
                    cur = cur.right
                else:
                    cur = cur.left
                path >>= 1
                # print(f'cur = {cur}')
            if cur:
                l = mid # 注意此处，使节点数为mid的节点存在，只能说明节点数至少为mid，不能说明节点数至少为mid+1
            else:
                r = mid - 1
            # print(f'after: l = {l}, r = {r}, mid = {mid}')
        
        return l
