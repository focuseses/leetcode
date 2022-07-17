# sort within the string
# dictionary to prevent duplicate addition
# max length of string be K
# O(N K log K) as K log K to sort a string using comparison sort
class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in dic:
                dic[sortedString] = [string]
            else: 
                dic[sortedString].append(string)
        newList = [dic[elem] for elem in dic]
        return newList


        


