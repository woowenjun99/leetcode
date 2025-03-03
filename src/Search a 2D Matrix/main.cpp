#include <iostream>
#include <vector>

class Solution {
    public:
        bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
            int left = 0, right = matrix.size() - 1, row = 0;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (matrix[mid][0] <= target and target <= matrix[mid][matrix[mid].size() - 1]) {
                    row = mid;
                    break;
                }

                if (matrix[mid][matrix[mid].size() - 1] < target) left = mid + 1;
                else right = mid - 1;
            }
            if (left > right) return false;
            left = 0, right = matrix[0].size() - 1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (matrix[row][mid] == target) return true;
                if (matrix[row][mid] < target) left = mid + 1;
                else right = mid - 1;
            }
            return false;
        }
};