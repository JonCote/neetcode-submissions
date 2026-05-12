class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_dict = {}
        for i, c in enumerate(s):
            if c not in letter_dict.keys():
                letter_dict[c] = 1
            else:
                letter_dict[c] += 1
                if letter_dict[c] == 0:
                    del letter_dict[c]
            
            if t[i] not in letter_dict.keys():
                letter_dict[t[i]] = -1
            else:
                letter_dict[t[i]] -= 1
                if letter_dict[t[i]] == 0:
                    del letter_dict[t[i]]
            
        if len(letter_dict.keys()) == 0:
            return True
        return False


        
            

