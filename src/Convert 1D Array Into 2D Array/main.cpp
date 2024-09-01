#include <vector>
using namespace std;

class Solution {
    public:
        vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
            std::vector<std::vector<int>> answer;
            if (m * n != original.size()) return answer;
            int ptr = 0;
            for (int row = 0; row < m; ++row) {
                std::vector<int> new_row;
                for (int col = 0; col < n; ++col) new_row.push_back(original[ptr++]);
                answer.push_back(new_row);
            }
            return answer;
        }
};