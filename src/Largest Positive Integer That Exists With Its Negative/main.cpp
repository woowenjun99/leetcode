#include <algorithm>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    public:
        int findMaxK(vector<int>& nums) {
            int answer = -1;
            std::unordered_set<int> s;
            for (auto num: nums) {
                if (s.find(-num) != s.end()) answer = std::max(answer, std::abs(num));
                s.insert(num);
            }
            return answer;
        }
};