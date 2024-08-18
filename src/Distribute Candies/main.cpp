#include <algorithm>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    public:
        int distributeCandies(vector<int>& candyType) {
            int n = candyType.size();
            std::unordered_set<int> candies;
            for (int i = 0; i < n; ++i) candies.insert(candyType[i]);
            return std::min(n / 2, (int) candies.size());
        }
};