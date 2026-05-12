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
            int floor = int(nums.size() / 3);
            
            std::cout << pair.second << " : ";
            std::cout << pair.first << " : ";
            std::cout << floor << std::endl;

            
            if(pair.second > floor) {
                results.push_back(pair.first);
            }
        }


        return results;
    }
};