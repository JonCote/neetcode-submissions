class Solution {
public:
    bool isAnagram(string s, string t) {
        
        int size = s.size();
        if (size != t.size()) {
            return false;
        }

        std::unordered_map<char, int> seen;

        for(int i = 0; i < size; ++i){
            if (seen.count(s[i])) {
                seen[s[i]] += 1;

                if(seen[s[i]] == 0) {
                    seen.erase(s[i]);
                }
            }
            else {
                seen[s[i]] = 1;
            }

             if(seen.count(t[i])) {
                seen[t[i]] -= 1;

                if(seen[t[i]] == 0) {
                    seen.erase(t[i]);
                }
            }
            else {
                seen[t[i]] = -1;
            }
        }

        
        return seen.empty();
    }
};
