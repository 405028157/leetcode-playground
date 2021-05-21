# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        last = None
        cur = head
        next = head.next
        while next:
            cur.next = last
            last = cur
            cur = next
            next = next.next
        cur.next = last
        return cur