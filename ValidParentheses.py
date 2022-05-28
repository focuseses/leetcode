class Solution(object):
    def isValid(self, s):
        if len(s) == 0:
            return True
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) <= 0:
                    return False
                removed = stack.pop()
                if char == ")" :
                    if removed != "(":
                        return False
                if char == "]" :
                    if removed != "[":
                        return False
                if char == "}":
                    if removed != "{":
                        return False
        if len(stack) != 0:
            return False
        return True
