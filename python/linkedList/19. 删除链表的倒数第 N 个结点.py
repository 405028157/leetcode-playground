# Definition for singly-linked list.
# https://github.com/405028157/leetcode-master/blob/master/problems/0019.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.md
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head
        slow = fast = dummy_head

        # n + 1 步要先走 n 步，这 n 步如果 fast 是 None, 说明没有倒数第 n 个数，因为一共都没有 n 个数
        for _ in range(n):
            if not fast:
                return head
            fast = fast.next
        # 这一步是为了让 fast 指到 None 的时候，slow 能指到倒数第 n + 1 个数
        fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy_head.next
        

        