#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    public:
        int maximumDifference(vector<int>& nums) {
            int answer = -1;
            for (int i = 0; i < nums.size(); ++i) {
                for (int j = i + 1; j < nums.size(); ++j) {
                    if (nums[j] <= nums[i]) continue;
                    answer = std::max(answer, nums[j] - nums[i]);
                }
            }
            return answer;
        }
};