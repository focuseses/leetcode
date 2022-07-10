# two pointers
#  O(n)
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast.next: 
            return head.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

        