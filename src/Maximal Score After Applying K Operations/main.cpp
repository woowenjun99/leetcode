#include <queue>
#include <vector>

class Solution {
    public:
        long long maxKelements(std::vector<int>& nums, int k) {
            long long score = 0;
            std::priority_queue<int> pq;
            for (auto &num: nums) pq.push(num);
            while (k--) {
                int temp = pq.top();
                score += temp;
                pq.pop();
                pq.push(std::ceil(temp / (3 * 1.0)));
            }
            return score;
        }
};
