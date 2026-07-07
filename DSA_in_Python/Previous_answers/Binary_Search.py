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
      
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix[0]) - 1


        ## 1 , 2, 3, 4, 5. target: 4
        for List in matrix:
            while L <= R: 
                mid = (L + R) // 2
                if target > List[mid]:
                    L = mid + 1
                elif target < List[mid]:
                    R = mid - 1
                elif target == List[mid]:
                    return True
            
            L = 0
            R = len(matrix[0]) - 1

        
        return False
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## Example: [1, 2, 3] , h = 3, if k = 2 --> pile 1 ~. so h = 2  pile 2 ~ 2h h = 0, but u have 3 more
        ## so k = 1 not correct --> Input: piles = [1,4,3,2], h = 9, Output: 2

        ## so brute force solution: 
        ## the hour = pile // rate
        ## We start with k = 1 --> Go through the array and see if h > 0 at the end, if so return k, 
        ## if not increase k by one and do the same process:

        '''
        First solutipn:
        found_rate = False
        k = 1
        original_h = h
        while (found_rate == False):
            for pile in piles:
                hour_to_eat_pile = math.ceil(pile / k)
                h = h - hour_to_eat_pile
            
            if h < 0:
                k += 1
                found_rate = False
                h = original_h
            else: 
                found_rate = True
        
        return k
        '''
        ## Ok so we wanna find the min k so that she can eat all bananas in rate k
        ## [1, 2, 5] and h = 4 --> the max k = 5, and the lowest is 1
        ## so we have a possible array of solution which is [1, 2, 3, 4, 5] 
        ## we can find that value using binary search 
        ## L = 0, R = len(arr) - 1
        ## mid = (l + R) // 2

    
        ## Input: piles = [25,10,23,4], h = 4 --> poss_ans = [1, 2, ..., 25]
        L = 1
        R = max(piles)
        res = R

        while (L <= R):
            k = (L + R) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h: ## k is too big
                res = min(res, k) 
                R = k - 1
            else:
                L = k + 1
        
        return res