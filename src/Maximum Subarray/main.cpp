#include <vector>
using namespace std;

class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int answer = -1e9, running_sum = 0;
            for (auto &num: nums) {
                running_sum += num;
                answer = std::max(answer, running_sum);
                if (running_sum < 0) running_sum = 0;
            }
            return answer;
        }
};