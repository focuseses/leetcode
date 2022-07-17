# two pointer
# time: O(n)
# space: O(1), in place
class Solution:
    def moveZeroes(self, nums):
        # pointer1
        pointer1 = 0
        for pointer2 in range(len(nums)):
            # swap
            if nums[pointer1] == 0 and nums[pointer2] != 0:
                temp = nums[pointer2]
                nums[pointer2] = nums[pointer1]
                nums[pointer1] = temp

            if nums[pointer1] != 0:
                pointer1 += 1
        return nums
