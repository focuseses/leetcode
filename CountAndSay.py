from typing import Optional

class Solution:
    def countAndSay(self, n: int) -> str:
        # return string
        def say(x):
            string = ""
            counter = 1
            for i in range(len(x)):
                if i <= len(x) - 2 and x[i] == x[i + 1]:
                    counter += 1
                else:
                    string += str(counter) + str(x[i])
                    counter = 1
            return string

        if n == 1:
            return "1"
        else:
            return say(self.countAndSay(n - 1))

x = Solution()
print(x.countAndSay(4))
        
                