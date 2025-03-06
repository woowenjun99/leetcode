#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        long long maxProfit(vector<int>& workers, vector<vector<int>>& tasks) {
            std::unordered_map<int, std::priority_queue<int>> mappers;
            long long answer = 0;
            for (std::vector<int> task: tasks) mappers[task[0]].push(task[1]);
            for (int worker: workers) {
                if (mappers.find(worker) == mappers.end() or mappers[worker].empty()) continue;
                answer += mappers[worker].top();
                mappers[worker].pop();
            }
            std::priority_queue<int> pq;
            for (auto &[k, v]: mappers) {
                while (not v.empty()) {
                    pq.push(v.top());
                    v.pop();
                }
            }
            if (not pq.empty()) answer += pq.top();
            return answer;
        }
};
