##
## Hash Maps classes:
##
class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None] ## It could have been pairs instead

    def hash(self, key):
        '''
        Returns the index of the key

        '''
        ## Consider the key is an string and you want to convert it to an integer
        ## What you do is that you get the sum of all ascii num of char of the string
        ## and then mod it by the capacity of the self
        sum = 0
        for x in key:
            sum += ord(x)
        return sum % self.capacity
    
    def get(self, key):
        '''
        Returns the value of the key if it exists. 
        '''

        ## Steps: 
        ## 1. get the index of key
        ## check if the key exist at that index, if so, return the self.val
        ## if not go to the next index
        ## if there is an item there, then check it again
        ## else return None

        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index] == key:
                return self.map[index].val
            else:
                index += 1
                index = index % self.capacity
        
        return None



