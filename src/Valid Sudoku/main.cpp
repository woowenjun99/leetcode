#include <vector>
using namespace std;

class Solution {
    public:
        bool isValidSudoku(vector<vector<char>>& board) {
            for (int row = 0; row < 9; ++row) {
                vector<bool> used(9, false);
                for (int col = 0; col < 9; ++col) {
                    if (board[row][col] == '.') continue;
                    int num = board[row][col] - '0' - 1;
                    if (used[num]) return false;
                    used[num] = true;
                }
            }

            for (int col = 0; col < 9; ++col) {
                vector<bool> used(9, false);
                for (int row = 0; row < 9; ++row) {
                    if (board[row][col] == '.') continue;
                    int num = board[row][col] - '0' - 1;
                    if (used[num]) return false;
                    used[num] = true;
                }
            }

            for (int outer_row = 0; outer_row < 3; ++outer_row) {
                for (int outer_col = 0; outer_col < 3; ++outer_col) {
                    vector<bool> used(9, false);
                    for (int row = outer_row * 3; row < outer_row * 3 + 3; ++row) {
                        for (int col = outer_col * 3; col < outer_col * 3 + 3; ++col) {
                            if (board[row][col] == '.') continue;
                            int num = board[row][col] - '0' - 1;
                            if (used[num]) return false;
                            used[num] = true;
                        }
                    }
                }
            }
            return true;
        }
};