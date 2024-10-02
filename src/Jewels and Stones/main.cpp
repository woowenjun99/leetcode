#include <unordered_set>
#include <string>
using namespace std;

class Solution {
    public:
        int numJewelsInStones(string jewels, string stones) {
            std::unordered_set<char> unique;
            for (int i = 0; i < jewels.size(); ++i) unique.insert(jewels[i]);
            int count = 0;
            for (int i = 0; i < stones.size(); ++i) {
                if (unique.find(stones[i]) == unique.end()) continue;
                count++;
            }
            return count;
        }
};