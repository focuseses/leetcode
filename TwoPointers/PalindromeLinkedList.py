# stack O(n) space and time
# can achieve O(1) space using two pointers one from the start, one from the beginning (to get mid, add 1 to one pointer, 
# add 2 to the other, when 2nd one reaches end, 1st one is in the middle)
class Solution:
    def isPalindrome(self, head):
        stack = [] 
        curr = head
        while curr != None:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr != None: 
            elem = stack.pop()
            if elem != curr.val:
                return False
            curr = curr.next
        return True

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next