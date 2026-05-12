class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> anagrams;

        for(const auto& str : strs) {
            vector<int> letter_counts(26, 0);

            for (char c : str) {
                letter_counts[c - 'a']++;
                std::cout << c << letter_counts[c - 'a'] << " ";
            }

            string key = to_string(letter_counts[0]);
            for(int i = 1; i<26; ++i) {
                std::cout << letter_counts[i];
                key += ',' + to_string(letter_counts[i]);
            }
            std::cout << " | " << key << " : " << str << std::endl;
            anagrams[key].push_back(str);

        }

    
        vector<vector<string>> output;
        for (const auto& [key, value] : anagrams) {
            //std::cout << key << " : " << std::endl;
            output.push_back(value);
        }

        return output;
    }
};
