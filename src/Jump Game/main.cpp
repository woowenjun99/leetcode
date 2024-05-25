#include <vector>
using namespace std;

class Solution {
    public:
        bool canJump(vector<int>& nums) {
            std::vector<bool> visited(nums.size(), false);
            visited[0] = true;
            for (int i = 0; i < nums.size(); ++i) {
                if (not visited[i]) continue;
                for (int j = i + 1; j < nums.size() and j <= i + nums[i]; ++j) visited[j] = true;
            }
            return visited[nums.size() - 1];
        }
};