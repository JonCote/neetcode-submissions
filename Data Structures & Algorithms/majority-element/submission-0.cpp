class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> count;

        int target = nums.size() / 2;
        for(const auto& num : nums) {
            count[num]++;
            if(count[num] > target) {
                return num;
            }
        }
        return 0;
    }
};