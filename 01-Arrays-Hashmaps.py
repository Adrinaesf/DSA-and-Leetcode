class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Steps:
        # 1. Crete a new list called ans
        # 2. We go through range(n), where n = length(nums)
        # 3. We update the new list with values in nums 
        # 4. Do this again, and return the result

        res = []
        n = len(nums)
        for i in range(n):
            res.append(nums[i])
        
        for i in range(n):
            res.append(nums[i])
        
        return res
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. Crete hashmap :  key:val -> num:(how many times we have it in list)
        # 2. go through the list and insert the data to the hashmap that we have
        # 3. if any value is greter than equal to 2, then return true
        # 4. otherwise return false

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return True
        
        return False
    

