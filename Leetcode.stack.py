class Solution:
    def isValid(self, s: str) -> bool:
        Map = {')': '(' , '}': '{' , ']': '['}
        stack = []

        for c in s:
            ## First we add all the open brackets to stack:
            if c not in Map:
                stack.append(c)
            else:
                if len(stack) != 0 and stack[-1] == Map[c]:
                    stack.pop()
                else: 
                    return False
        
        return len(stack) == 0