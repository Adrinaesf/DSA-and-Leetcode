class Solution: 
  def windowEqualElement(nums, k):
    '''
    Return true if there is a slice of size k in the nums such that
    there are two elements that are equal. 
    '''
    ## We solve this using two pointer of left or right
    # That is because suppose L = [1, 2, 3, 1, 3]
    # We want to check if 1 == 2, or 1 == 3, and so on --> 
    # So we need 2 pointers to check that

    # We also solve this using set()

    window = set()
    L = 0

    for R in range(len(nums)):
      if R - L + 1 > k: ## That is the slice is greater than k
        window.remove(nums[L])
        L += 1
      if nums[R] in window:
        return True  
      window.add(nums[R])
    return False
  
  def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = len(prices) - 1
        maxVal = 0

        while L < R:
            profit = prices[R] - prices[L]
            if prices[L+1] < prices[L]:
                L += 1
            else:
                R -= 1
            maxVal = max(maxVal, profit)

        return 0 if maxVal <= 0 else maxVal

  def lengthOfLongestSubstring(self, s: str) -> int:
        ## We can solve this using their asccii values
        nums = []
        for ch in s:
            nums.append(ord(ch)) # O(n)

        L = 0
        window = set()
        # Consider asc = [1, 2, 3, 1] --> k = 3
        length = 0
        for R in range(len(nums)):
            if nums[R] in window:
                window.remove(nums[L])
                L += 1
                length = max(length, R - L)
            else:
                length = max(length, R - L + 1)
            window.add(nums[R])

        return length
        
