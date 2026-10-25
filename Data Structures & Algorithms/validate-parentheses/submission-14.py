class Solution:
    def isValid(self, s: str) -> bool:
        d =  {")": "(", "]": "[", "}": "{"}
        stack = []
        
        for c in s:
            if c == ")"  or c == "]" or c == "}":
                if not stack or d[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        if not stack:
            return True    
        return False

            