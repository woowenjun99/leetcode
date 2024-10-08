#include <algorithm
#include <vector>
using namespace std;

class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            int ptr = 0;
            for (int i = 0; i < nums.size(); ++i) {
                if (nums[i] != 0) std::swap(nums[ptr++], nums[i]);
            }
        }
};