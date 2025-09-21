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
        
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            count = 1
            found = False   # reset here for each i
            
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(count)
                    found = True
                    break
                else:
                    count += 1

            if not found:
                result.append(0)
                
        return result


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]