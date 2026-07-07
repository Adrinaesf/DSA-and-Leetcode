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
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            prev_list = [1, 1]

            for _ in range(2, numRows):
                resu_list = [1]  # start each row with 1
                for i in range(len(prev_list) - 1):
                    number = prev_list[i] + prev_list[i + 1]
                    resu_list.append(number)
                resu_list.append(1)  # end each row with 1
                res.append(resu_list)
                prev_list = resu_list  # update prev_list

            return res
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            # build next row using the previous one
            new_row = [1]
            for i in range(len(row) - 1):
                new_row.append(row[i] + row[i + 1])
            new_row.append(1)
            row = new_row
        return row