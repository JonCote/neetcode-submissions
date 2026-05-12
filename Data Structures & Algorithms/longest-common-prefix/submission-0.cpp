class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        int min_len = -1;
        for (auto str : strs) {
            if (min_len == -1) {
                min_len = str.length();
            }
            else {
                if (min_len > str.length()) {
                    min_len = str.length();
                }
            }
        }

        string common_prefix = "";
        for (int i = 0; i<min_len; ++i) {
            char cur = strs[0][i];

            for(auto str : strs) {
                std::cout << str[i] << " | ";

                if (cur != str[i]) {
                    std::cout << "[" << cur << " : " << str[i] << "]";
                    
                    return common_prefix;
                }


                std::cout << std::endl;
            }
            
            

            common_prefix += cur;
        }

       return common_prefix;
    }
};