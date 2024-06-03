#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        bool isNStraightHand(vector<int>& hand, int groupSize) {
            if (hand.size() % groupSize > 0) return false;
            std::sort(hand.begin(), hand.end());
            std::unordered_map<int, int> counter;
            for (auto &card: hand) counter[card]++;
            for (int i = 0; i < hand.size(); ++i) {
                if (counter[hand[i]] == 0) continue;
                for (int j = 0; j < groupSize; ++j) {
                    if (counter[hand[i] + j] == 0) return false;
                    counter[hand[i] + j]--;
                }
            }
            return true;
        }
};