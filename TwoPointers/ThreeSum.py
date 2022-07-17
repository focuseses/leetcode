# two pointer
# O(n^2)
class Solution:
    def threeSum(self,nums):
        nums.sort()
        thisList = []
        for i in range(len(nums)):
            # handle repetitions for 3sum
            if i > 0 and nums[i] == nums[i - 1]:
                print("hi")
                continue
            required = - nums[i]
            pointerOne = i + 1
            pointerTwo = len(nums) - 1
            
            while pointerOne < pointerTwo:
                currSum = nums[pointerOne] + nums[pointerTwo]
                if currSum == required:
                    triplet = [nums[i], nums[pointerOne], nums[pointerTwo]]
                    thisList.append(triplet)
                    pointerOne += 1
                    # handle repetitions for 2sum
                    while pointerOne < pointerTwo and nums[pointerOne] == nums[pointerOne - 1]:
                        pointerOne += 1
                if currSum > required:
                    pointerTwo -= 1
                if currSum < required:
                    pointerOne += 1
        return thisList





