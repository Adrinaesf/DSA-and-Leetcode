class Solution: 
  def isPalindrome(self, s: str) -> bool:
        # keep only lowercase alphanumeric characters
        cleaned = ""
        for ch in s.lower():
            if ch.isalnum():
                cleaned += ch

        L, R = 0, len(cleaned) - 1
        while L < R:
            if cleaned[L] != cleaned[R]:
                return False
            L += 1
            R -= 1
        return True
        
  def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] == target:
                return [L+1, R+1]
            elif numbers[L] + numbers[R] > target:
                R -= 1
            else: 
                L += 1

  def maxArea(self, heights: List[int]) -> int:
        res = 0
        L, R = 0, len(heights) - 1


        while L < R:
            area = (R - L) * min(heights[L], heights[R])
            res = max(res, area)
            if heights[L] <= heights[R]:
                L += 1
            else: 
                R -=1

        return res