#include <vector>
using namespace std;

class Solution {
    public:
        int arraySign(vector<int>& nums) {
            int current;
            if (nums[0] > 0) current = 1;
            else if (nums[0] == 0) return 0;
            else current = -1;

            for (int i = 1; i < nums.size(); ++i) {
                if (nums[i] == 0) return 0;
                else if (nums[i] < 0) current = -current;
            }

            return current;
        }
};