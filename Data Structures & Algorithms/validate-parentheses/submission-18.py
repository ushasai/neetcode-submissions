class Solution:
    def isValid(self, s: str) -> bool:
        d =  {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for c in s:
            if c == ")"  or c == "]" or c == "}":
                if stack and d[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True    
        return False

            