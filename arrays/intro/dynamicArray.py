##
## Dynamic Arrays
##

## Dynamic arrays are kinds of array where you don't specify its size at the beginning. 
## So it's not like statick arrays to have a specific size from the beginning. 

class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.length = 0
        self.array = [None] * capacity
    
    def __repr__(self):
        return "Dynamic Array: %s" % self.array
    
    def resize(self):
        ## In this function we resize the array we have by making a new array, 
        ## and copying elements from the old array. 
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.array[i]
        
        ## Now we just mutate the old array we had:
        self.array = newArr
    
    def pushBack(self, n):
        ## This function insert element to the dynamic array that we have:
        if (self.length == self.capacity):
            self.resize()
        
        self.array[self.length] = n
        self.length += 1
        