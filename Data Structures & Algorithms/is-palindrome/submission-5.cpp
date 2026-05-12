class Solution {
public:
    bool isPalindrome(string s) {
        
        int start = 0;
        int end = s.size() - 1;

        while (start < end) {
            if(!std::isalnum(s[start])) {
                start += 1;
            }
            if(!std::isalnum(s[end])) {
                end -= 1;
            }
            
            if(std::isalnum(s[start]) && std::isalnum(s[end])) {
                std::cout << s[start] << " : " << s[end] << std::endl;

                if(static_cast<char>(std::tolower(s[start])) != static_cast<char>(std::tolower(s[end]))) {
                    return false;
                }

                start += 1;
                end -= 1;
            }
        }

        return true;
    }
};
