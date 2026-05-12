class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string common_prefix = "";
        for (int i = 0; i < strs[0].length(); ++i) {
            char cur = strs[0][i];

            for(auto str : strs) {
                if (i == str.length() || cur != str[i]) {
                    return common_prefix;
                }
            }
            common_prefix += cur;
        }

       return common_prefix;
    }
};