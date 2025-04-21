#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        int numRabbits(vector<int>& answers) {
            std::unordered_map<int, int> mappers;
            for (int ans: answers) mappers[ans]++;
            int ans = 0;
            for (auto &[k, v]: mappers) {
                while (mappers[k] > 0) {
                    ans = ans + k + 1;
                    mappers[k] = mappers[k] - k - 1;
                }
            }
            return ans;
        }
};