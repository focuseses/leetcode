# binary search
# O(logn)
import math
class Solution:
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = int(start + (end - start)/2)
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[len(nums) - 1] < nums[mid]:
                start = mid + 1
            else: 
                end = mid - 1 
        return nums[mid]

                
