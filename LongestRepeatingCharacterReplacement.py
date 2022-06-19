class Solution:
    def characterReplacement(self, s, k):
        hashtable = {}
        maximum = 0
        left = 0
        right = 0
        while right < len(s):
            window = right - left + 1
            if (len(hashtable) == 0) :
                greatest = 0
            else : 
                greatest = max(hashtable, key=hashtable.get)
            condition = window <= greatest + k
            if not condition:
                if hashtable[s[left]].get == 1:
                    hashtable.pop(s[left])
                else:
                    hashtable[s[left]] = hashtable.get(s[left]) - 1
            
                left += 1
            elif condition: 
                if window > maximum:
                    maximum = window
                if hashtable.get(s[right]) == None:
                    hashtable[s[right]] = 1
                else:
                    hashtable[s[right]] = hashtable.get(s[right]) + 1
        return maximum 


        
                