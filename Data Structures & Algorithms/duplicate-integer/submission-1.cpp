class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, bool> seen;
        for (int num : nums) {
            if(seen.count(num) > 0) return true;
            seen[num] = true;
        }

        return false;
    }
};