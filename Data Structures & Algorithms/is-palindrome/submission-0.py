import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for c in s:
            if c.isalnum():
                str += c.lower()

        return True if str[::-1] == str[:] else False
    
        