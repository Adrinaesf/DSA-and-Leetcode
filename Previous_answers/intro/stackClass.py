##
## Stack Class:
##
from tabulate import tabulate
class Stack:
    def __init__(self):
        self.stack = []
    
    def __repr__(self):
        return tabulate([[x] for x in self.stack], headers=["Stack"])
    
    def __eq__(self, other):
        if not isinstance(other, Stack):
            return False
        return self.stack == other.stack

    def push(self, item): 
        return self.stack.append(item)
    
    def last_element(self):
        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
    
    def extend(self, array):
        self.stack.extend(array)





