class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;

        for(int i = 0; i < nums.size(); ++i) {
            if (k - nums[i] == 0) {
                count++;
            }

            int remain = k - nums[i];
            for(int j = i+1; j<nums.size(); ++j) {
                if(remain - nums[j] == 0) {
                    count++;
                }
                remain -= nums[j];
            }
            
        }
        return count;
    }
};