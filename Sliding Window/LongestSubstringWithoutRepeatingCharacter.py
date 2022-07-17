#sliding window
# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        hashmap = {}
        maximum = 0
        while right < len(s):
            window = right - left + 1
            if s[right] in hashmap:
                hashmap.pop(s[left])
                left += 1
            elif s[right] not in hashmap:
                if window > maximum:
                  maximum = window
                hashmap[s[right]] = s[right]
                right += 1
        return maximum