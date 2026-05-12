class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charMap;

        if (size(s) != size(t)) {
            return false;
        }

        for (int i = 0; i < size(s); ++i) {
            if (s[i] == t[i]) {
                continue;
            }

            if(charMap.count(s[i]) == 0) {
                charMap.insert({s[i], 1});
            }
            else {
                charMap[s[i]] += 1;
            }


            if(charMap.count(t[i]) == 0) {
                charMap.insert({t[i], -1});
            }
            else {
                charMap[t[i]] -= 1;
            }

            if(charMap[s[i]] == 0) {
                charMap.erase(s[i]);
            }

            if(charMap[t[i]] == 0) {
                charMap.erase(t[i]);
            }

        }

        if(charMap.empty()) {
            return true;
        }

        return false;
    }
};
