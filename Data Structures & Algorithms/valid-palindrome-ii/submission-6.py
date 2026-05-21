class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        d = 0

        def validSubPalindrome(s: str, l: int, r: int, d: int) -> bool:
            while l < r:
                if not s[l].isalnum():
                    l += 1
                    continue
                if not s[r].isalnum():
                    r -= 1
                    continue
                
                if s[l].lower() != s[r].lower():
                    if d > 0:
                        return False
                    else:
                        d += 1
                        return (validSubPalindrome(s, l+1, r, d) or validSubPalindrome(s, l, r-1, d))

                l += 1
                r -= 1
            
            return True

        return validSubPalindrome(s, l, r, d)