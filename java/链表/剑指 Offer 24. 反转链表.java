
// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
 
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode lastNode = null;
        ListNode nextNode;
        while (head != null) {
            nextNode = head.next;
            head.next = lastNode;
            lastNode = head;
            head = nextNode;
        }

        return lastNode;
    }
}