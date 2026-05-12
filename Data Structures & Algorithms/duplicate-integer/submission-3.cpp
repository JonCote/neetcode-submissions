class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> seen;

        for(auto num : nums) {
            if (seen[num]) {
                return true;
            }
            else {
                seen[num] = 1;
            }
        }


        return false;
    }
};