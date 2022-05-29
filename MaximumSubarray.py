# dp O(n)
class Solution(object):
    def maxSubArray(self, nums):
        m = nums[0]
        maxSum = [0 for a in range(len(nums))]
        for i in range(0, len(nums)):
            if i == 0:
                maxSum[i]= nums[i]
            else:
                maxSum[i] = max(maxSum[i - 1] + nums[i],  nums[i])
                if maxSum[i] > m:
                    m = maxSum[i]
        return m
        