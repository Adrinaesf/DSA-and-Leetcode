class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## Contains Duplicate
        self.nums = nums.sort()
        for i in range(len(nums)- 1):
            if nums[i] == nums[i+1]:
                return True
        
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        ## We can work with their assci char:
        if len(s) != len(t):
            return False
        else: 
            Hash_s = {}
            for c in s:
                if c not in Hash_s:
                    Hash_s[c] = 1
                else:
                    Hash_s[c] += 1

            Hash_t = {}
            for c in t:
                if c not in Hash_t:
                    Hash_t[c] = 1
                else:
                    Hash_t[c] += 1

            return Hash_s == Hash_t

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            ## Now we have to make the map:
            prev_map[tuple(count)].append(word)
        
        return list(prev_map.values())
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in Map:
                return [Map[complement], i]
            Map[nums[i]] = i
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        for x in nums:
            if x not in Map:
                Map[x] = 1
            else:
                Map[x] += 1
        
        ## Now we can get the values of the map and return 
        ## the last k-th elements of it, after sorting
        
        sorted_items = sorted(Map.items(), key=lambda x: x[1], reverse=True)

        res = []
        for items in sorted_items[:k]:
            res.append(items[0])
        
        return res
    
    def encode(self, strs: List[str]) -> str:
        ## We want to transform the strings to 
        ## a single string that is easy to be decoded
        result = ""
        for i in range(len(strs)):
            result = result + strs[i] + " | "

        return result

    def decode(self, s: str) -> List[str]:
        ## Now we incode it to a string: 
        parts = s.split(" | ")
        return parts[:-1]


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        res = []

        if nums.count(0) >= 2: 
            return [0] * len(nums)
    
        elif nums.count(0) == 1:
            index = nums.index(0)
            nums.remove(0)
            for x in nums:
                pro = pro * x 
            
            for i in range(len(nums) + 1):
                if i == index:
                    res.append(pro)
                else: 
                    res.append(0)
            return res
        else: 
            for num in nums:
                pro = pro * num
            
            for elem in nums:
                res.append(pro // elem)
            
            return res
            
    def longestConsecutive(self, nums: List[int]) -> int:
        my_array = set(nums) ## O(n)
        longest = 0
        for n in my_array:
            if (n-1) not in my_array:
                length = 0
                while (n+length) in my_array:
                    length += 1
                longest = max(length, longest)
        return longest

            
        