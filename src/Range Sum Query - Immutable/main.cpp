#include <vector>
using namespace std;

class NumArray {
    public:
        std::vector<int> prefix_sums;

        NumArray(vector<int>& nums) {
            int prefix_sum = 0;
            for (auto num: nums) {
                prefix_sum += num;
                prefix_sums.push_back(prefix_sum);
            }
        }
        
        int sumRange(int left, int right) {
            return prefix_sums[right] - (left > 0 ? prefix_sums[left - 1] : 0);
        }
};