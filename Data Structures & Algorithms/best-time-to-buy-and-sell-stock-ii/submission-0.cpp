class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prof = 0;

        for(int i = 0; i<prices.size(); ++i) {
            for(int j = i+1; j<prices.size(); ++j) {
                std::cout << prices.at(i) << " ";
                std::cout << prices.at(j) << std::endl;
                if(prices.at(j) > prices.at(i)) {
                    prof += prices.at(j) - prices.at(i);
                    i = j-1;
                    break;
                }
                else {
                    i = j;
                }
            }
        }

        return prof;

    }
};