##
## Using Stacks Class
##
from stackClass import Stack
from dynamicArray import DynamicArray

my_stack = Stack()
my_stack.extend([1, 2, 3])
print("Stack: ")
print(my_stack)

my_dynArr = DynamicArray(2)
my_dynArr.pushBack(2)
my_dynArr.pushBack(3)
my_dynArr.pushBack(4)
print("Dynamic Array:")
print(my_dynArr)




