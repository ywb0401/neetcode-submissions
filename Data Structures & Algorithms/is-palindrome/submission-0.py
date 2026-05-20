class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for word in s:
            if word.isalnum() == True:
                c += word
        l, r = 0, len(c)-1
        while l < r:
            if c[l].lower() != c[r].lower():
                return False
            l += 1
            r -= 1
        return True