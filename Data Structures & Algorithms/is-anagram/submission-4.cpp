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
            }
            else {
                seen[s[i]] = 1;
            }
        }

        for(int i = 0; i < size; ++i){
            if(seen.count(t[i])) {
                seen[t[i]] -= 1;

                if(seen[t[i]] == 0) {
                    seen.erase(t[i]);
                }
            }
            else {
                return false;
            }
        }

        return seen.empty();
    }
};
