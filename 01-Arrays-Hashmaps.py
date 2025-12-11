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
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ok consider: nums = [3,6,5,4], target = 7
        # comp_list = [4, 3, 2, 1]
        # We want to take 3, and say 4 is complement that is in the array
        # Then we want the index of 3, and 4

        # Consider the map: {3:0, 4:1, 5:2, 6:3} -> num:index
        # Then we do:
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num # comp = 3
            if comp in seen:
                return [seen[comp], i]

            seen[num] = i # seen = {3:0, 6:1, 5:2, 4:3} 
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Think about sorting the strings

        res = ""
        strs.sort()

        # Now let's get the first and last string
        first = strs[0]
        last = strs[len(strs) - 1]
        print(strs)
        for i in range(len(first)):
            if first[i] == last[i]:
                res += first[i]
            else:
                break
                
        return res
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if two words are anagram of one another, then 
        # When you sort them, they are the same word:
        # so I will have a map that has the sorted word as key
        # and the array as the groups

        # Algo:
        # 1. Crete a Map, and a list
        # 2. Go through the words in the list
        # 3. Consider the sorted version of that word = "sort_w"
        # 4. if sort_w in Map, then Map[sort_w].append(word)
        # 5. else Map[word] = []
        # 6. Append the values to the res by the end
        
        anagram_Map = {}
        res = []

        for word in strs:
            char_list = sorted(word)
            sorted_string = "".join(char_list)
            if sorted_string in anagram_Map:
                anagram_Map[sorted_string].append(word)
            else:
                anagram_Map[sorted_string] = [word]
        
        for val in anagram_Map.values():
            res.append(val)
        
        
        return res

    def removeElement(self, nums: List[int], val: int) -> int:
        # [1, 2, 3, 1, 5, 6, 2]
        # val = 1
        # [2, 3, 5, 6, 2]

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
  
        return k

    def majorityElement(self, nums: List[int]) -> int:
        Map = {}
        n = math.floor(len(nums) / 2)

        for num in nums:
            if num in Map:
                Map[num] += 1
            else: 
                Map[num] = 1
            
            if Map[num] > n:
                return num

    def sortArray_insertion(self, nums: List[int]) -> List[int]:
        # [10,9,1,1,1,2,3,1]
        def swap(p1, p2):
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp

        def insert(pos):
            ## This sorts the nums from 0 to pos:
            ## Example: L = [1, 4, 2, 5, 3], pos = 3, output: L = [1, 2, 6, 5, 3]
            ## Requires: L from 0 to pos - 1 is sorted
            while (pos > 0 and nums[pos] < nums[pos-1]):
                swap(pos, pos - 1)
                pos = pos - 1
        
        for i in range(1, len(nums)):
            insert(i)
        
        return nums
