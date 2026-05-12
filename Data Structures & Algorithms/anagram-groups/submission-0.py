class Solution:
    def checkAnagram(self, s: str, t: str) -> bool:
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


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {strs[0] : [strs[0]]}
        
        for s in strs[1:]:
            ana_found = False
            for k in ana_dict.keys():
                if self.checkAnagram(s, k):
                    ana_dict[k].append(s)
                    ana_found = True
                    break
            
            if not ana_found:
                ana_dict[s] = [s]
        
        result = []
        for k in ana_dict.keys():
            result.append(ana_dict[k])

        return result
    