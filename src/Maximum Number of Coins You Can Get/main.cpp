#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        int maxCoins(vector<int>& piles) {
            std::sort(piles.begin(), piles.end());
            int answer = 0;
            int index = piles.size() - 2;
            for (int i = 0; i < piles.size() / 3; ++i) {
                answer += piles[index];
                index -= 2;
            }
            return answer;
        }
};