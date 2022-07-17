# dynamic programming
# for odd, iterate through as the middle then expand - if left and right are the same can expand
# for even, iterate through but now starting with two elements 
# O(n * n)
import string
class Solution:
    def countSubstrings(self, s):
        count = 0 
        # to count odd 
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            while (left >= 0 and right < len(s)):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
        
        # to count even
        for left in range(len(s)):
            right = left + 1
            while (left >= 0 and right < len(s)):
                if s[left] != s[right]:
                    break
                count += 1
                left -= 1
                right += 1
        count += len(s)
        return count
        