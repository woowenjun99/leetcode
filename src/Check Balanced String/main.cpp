#include <string>

class Solution {
    public:
        bool isBalanced(std::string num) {
            int nums[2] = {0, 0};
            for (int i = 0; i < num.size(); ++i) {
                nums[i % 2] += num[i] - '0';
            }
            return nums[0] == nums[1];
        }
};