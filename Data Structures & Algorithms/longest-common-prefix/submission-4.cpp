class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // sliding window
        for(int i = 0; i < strs[0].length(); ++i) {
            for(auto s : strs) {
                if(i == s.length() || s[i] != strs[0][i]) {
                    return s.substr(0,i);
                }
            }
        }
        

        return strs[0];
    }
};