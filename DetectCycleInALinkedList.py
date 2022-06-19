# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# create a hashtable, hash the node addresses then traverse and check if present before
# O(n)
# space: O(n)
class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        current = head
        hashtable = {}
        while current != None:
            if hashtable.get(current) != None:
                return True
            hashtable[current] = current
            current = current.next