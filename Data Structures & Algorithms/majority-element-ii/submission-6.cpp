class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        
        std::map<int, int> valueCounts;
        std::vector<int> results;

        for(int num : nums) {
            if(valueCounts.count(num) > 0) {
                valueCounts[num] += 1;
            }
            else {
                valueCounts[num] = 1;
            }
        }

        for(auto pair : valueCounts) {
            if(pair.second > int(nums.size() / 3)) {
                results.push_back(pair.first);
            }
        }


        return results;
    }
};