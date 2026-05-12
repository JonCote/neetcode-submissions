class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c_dict = {}
        t_dict = {}
        for i, c in enumerate(s):
            if c not in c_dict.keys():
                c_dict[c] = 1
            else:
                c_dict[c] += 1

            if t[i] not in t_dict.keys():
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        
        if c_dict.keys() != t_dict.keys():
            return False
        
        for k in c_dict.keys():
            if c_dict[k] != t_dict[k]:
                return False
        
        return True


        
            

