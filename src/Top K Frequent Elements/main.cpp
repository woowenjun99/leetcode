#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            std::vector<int> answer;
            std::unordered_map<int, int> counter;
            for (auto num: nums) counter[num]++;
            std::priority_queue<std::pair<int, int>> pq;
            for (auto &[key, v]: counter) pq.push({v, key});
            while (k--) {
                answer.push_back(pq.top().second);
                pq.pop();
            }
            return answer;
        }
};