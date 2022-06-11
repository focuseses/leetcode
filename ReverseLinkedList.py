# recursive 
# O(n)
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest 

#iterative
# o(n)
# create new variable to store the previous value then shift the pointers 
class Solution:
    def reverseList(self, head):
        current = head
        previous = None
        while current != None:
           nex = current.next
           current.next = previous 
           previous = current 
           current = nex 
        head = previous
        return head

