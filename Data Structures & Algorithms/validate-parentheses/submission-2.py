class Solution:
    def isValid(self, s: str) -> bool:
        ##create dict to map the pairs
        ##create stack
        ##if it is right facing(c in dict) ,else append
        ##if not empty and left facing and equals the last element in the stack, pop the last element
        ##repeat and if stack empty return true

        dic = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in dic:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False  
