#include <queue>
#include <vector>
using namespace std;

class Solution {
    public:
        int maxDistToClosest(vector<int>& seats) {
            std::queue<std::pair<int, int>> q;
            std::vector<bool> visited(seats.size(), false);
            for (int i = 0; i < seats.size(); ++i) {
                if (seats[i] == 1) {
                    q.push({i, 0});
                    visited[i] = true;
                }
            }
            int answer = 0;
            while (not q.empty()) {
                auto [index, distance] = q.front();
                q.pop();
                if (index - 1 >= 0 and not visited[index - 1]) {
                    q.push({index - 1, distance + 1});
                    visited[index - 1] = true;
                    answer = std::max(answer, distance + 1);
                }

                if (index + 1 < visited.size() and not visited[index + 1]) {
                    q.push({index + 1, distance + 1});
                    visited[index + 1] = true;
                    answer = std::max(answer, distance + 1);
                }
            }
            return answer;
        }
};