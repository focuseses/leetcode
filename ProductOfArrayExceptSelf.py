# O(n) create two arrays - suffix, prefix
class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        prefix = [0 for i in range(length)]
        answer = [0 for i in range(length)]
        suffix = [0 for i in range(length)]
        for i in range(length):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i - 1] * nums[i - 1]
        for j in range(length - 1, -1, -1):
            if j == length - 1:
                suffix[j] = 1
            else:
                suffix[j] = suffix[j + 1] * nums[j + 1]
        for k in range(length):
            answer[k] = prefix[k] * suffix[k]
        return answer