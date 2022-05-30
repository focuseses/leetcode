class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end)/2
        while (start < end):
            if nums[mid] < nums[mid - 1]:
                