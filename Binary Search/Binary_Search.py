class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## This is basically the binary search algorithem :)

        ## Steps: 
        ## 1. Define boundaries, 2. Define the mid point, 3. Define the conditions
        ## Ex: [-1,0,2,4,6,8], target = 4,  looking for index of target


        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if target > nums[mid]: 
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else: 
                return mid
        
        return -1

        