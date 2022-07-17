# O(n)
class Solution:
    def removeElement(self, nums, val):
        count = 0
        for element in nums:
            if(element == val):
                count += 1
        for i in range(count):
            nums.remove(val)


        