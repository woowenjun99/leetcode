#include <algorithm>
#include <vector>

class Solution {
    public:
        std::vector<int> transformArray(std::vector<int>& nums) {
            std::vector<int> answer;
            for (int i = 0; i < nums.size(); ++i) answer.push_back(nums[i] % 2);
            std::sort(answer.begin(), answer.end());
            return answer;
        }
};