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