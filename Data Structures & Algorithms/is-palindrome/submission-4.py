class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            
            if not self.alphaNum(s[p1]):
                p1 += 1
                continue
            
            if not self.alphaNum(s[p2]):
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                return False

            p1 += 1
            p2 -= 1
        
        return True
        
    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))
