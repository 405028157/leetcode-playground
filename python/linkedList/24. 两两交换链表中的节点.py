# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        string_rep = ''
        cur = self
        while cur:
            string_rep += f'<{cur.val}> ---> '
            cur = cur.next
        string_rep += '<END>'
        return string_rep
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        one = head
        two = one.next
        three = two.next

        two.next = one
        one.next = self.swapPairs(three)
        return two

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)

s = Solution()
reversedHead = s.swapPairs(l)
print(reversedHead)