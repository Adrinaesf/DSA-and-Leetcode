##
## Prefix Sum:
##


## nums = array of numbers
def __init__(self, nums):
    self.prefix = []
    total = 0
    for x in nums:
        total += x
        self.prefix.append(total)
    
def rangeSum(self, left, right):
    pre_right = self.prefix[right]
    pre_left = self.prefix[left - 1] if left > 0 else 0
    return (pre_right - pre_left)


