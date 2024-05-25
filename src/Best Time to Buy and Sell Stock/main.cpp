#include <vector>
using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int left = 0, right = 1, max_so_far = 0;
            while (left < prices.size() and right < prices.size()) {
                if (prices[right] < prices[left]) left = right;
                else max_so_far = max(prices[right] - prices[left], max_so_far);
                right++;
            }
            return max_so_far;
        }
};