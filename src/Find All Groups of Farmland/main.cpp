#include <vector>
using namespace std;

class Solution {
    public:
        void dfs(int row, int col, vector<vector<int>>& land, vector<int>& answer) {
            if (row < 0 or row >= land.size() or col < 0 or col >= land[row].size() or land[row][col] == 0) return;
            land[row][col] = 0;
            answer[2] = std::max(answer[2], row);
            answer[3] = std::max(answer[3], col);
            dfs(row - 1, col, land, answer);
            dfs(row + 1, col, land, answer);
            dfs(row, col - 1, land, answer);
            dfs(row, col + 1, land, answer);
        }

        vector<vector<int>> findFarmland(vector<vector<int>>& land) {
            std::vector<std::vector<int>> farmlands;
            for (int row = 0; row < land.size(); ++row) {
                for (int col = 0; col < land[row].size(); ++col) {
                    if (land[row][col] == 0) continue;
                    std::vector<int> answer = {row, col, 0, 0};
                    dfs(row, col, land, answer);
                    farmlands.push_back(answer);
                }
            }
            return farmlands;    
        }
};