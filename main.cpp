#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            std::vector<int> answer(2);
            std::unordered_map<int, int> mappers;
            for (int i = 0; i < nums.size(); ++i) {
                if (mappers.find(nums[i]) != mappers.end()) {
                    answer[0] = mappers[nums[i]];
                    answer[1] = i;
                    break;
                }
                mappers[target - nums[i]] = i;
            }
            return answer;
        }
};

int main(void) {
    std::ios::sync_with_stdio(0);
    std::cout.tie(0);
    Solution s;
    std::vector<int> nums = {2, 7, 11, 15};
    std::vector<int> results = s.twoSum(nums, 9);
    std::cout << results[0] << " " << results[1] << std::endl;
    return 0;
}