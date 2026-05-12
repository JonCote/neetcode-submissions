class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prof = 0;

        for(int i = 1; i<prices.size(); ++i) {
            if (prices.at(i) > prices.at(i-1)) {
                prof += (prices.at(i) - prices.at(i-1));
            }
        }

        return prof;

    }
};