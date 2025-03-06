#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
    public:
        vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
            std::vector<int> answer(2);
            std::unordered_set<int> mappers;
            for (int row = 0; row < grid.size(); ++row) {
                for (int col = 0; col < grid[row].size(); ++col) {
                    if (mappers.find(grid[row][col]) != mappers.end()) answer[0] = grid[row][col];
                    mappers.insert(grid[row][col]);
                }
            }
            for (int i = 1; i <= grid.size() * grid.size(); ++i) {
                if (mappers.find(i) != mappers.end()) continue;
                answer[1] = i;
                break;
            }
            return answer;
        }
};
