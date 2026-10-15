
class Stack:
    def __init__(self):
        self.items = []

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        if (self.is_empty()):
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else: 
            return self.items[-1]

    def is_empty(self):
        if (len(self.items) == 0):
            return True
        else: 
            return False


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())      # 30
print(s.pop())       # 30
print(s.pop())       # 20
print(s.is_empty())  # False