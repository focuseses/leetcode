# Naive way is to check for every possible area O(n^2)
# Notice that we can start from first index to last index
# Two pointers 
# O(n), space: O(1)
class Solution:
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        maxArea = -1
        while (start < end):
            area = (end - start) * min(height[start], height[end])
            if area > maxArea:
                maxArea = area
            if (height[start] < height[end]):
                start += 1
            elif (height[start] > height[end]):
                end -= 1
            else: 
                if height[start + 1] > height[end - 1]:
                    start += 1
                else: 
                    end -= 1
        return maxArea
