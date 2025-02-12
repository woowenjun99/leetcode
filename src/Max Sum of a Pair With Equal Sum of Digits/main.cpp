#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
    public:
        int maximumSum(std::vector<int>& nums) {
            std::unordered_map<int, std::priority_queue<int>> mappers;
            for (int i = 0; i < nums.size(); ++i) {
                int x = nums[i];
                int sum_of_digits = 0;
                while (x > 0) {
                    sum_of_digits += x % 10;
                    x /= 10;
                }
                mappers[sum_of_digits].push(-nums[i]);
                if (mappers[sum_of_digits].size() > 2) mappers[sum_of_digits].pop();
            }

            int answer = -1;
            for (auto [k, v]: mappers) {
                if (v.size() != 2) continue;
                int one = v.top(); v.pop();
                int two = v.top(); v.pop();
                answer = std::max(answer, -one-two);
            }
            return answer;
        }
};