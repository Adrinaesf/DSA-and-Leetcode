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

    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Check if they are in the same length or not
        # 2. Then we get to a point where len(s) == len(t)
        # 3. We crete two hashmap that maps char: # of occurance
        # 4. then we go through the keys in has_s, and comapre if their values is the same as hash_t

        # "abc" "aabbcc"
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        hash_s = defaultdict(int)
        for ch in s:
            hash_s[ch] += 1
        # hash_s = {'r': 2 , 'a': 2, 'c': 2, 'e': 1}

        hash_t = defaultdict(int)
        for ch in t:
            hash_t[ch] += 1
        # hash_t = {'c': 2 , 'a': 2, 'r': 2, 'e': 1}

        for key in hash_s.keys():
            if hash_s[key] != hash_t[key]:
                return False
        
        return True
    

